"""
generate_sft_dataset.py — Synthetic SFT Dataset Generator

Extracts Tcl command examples from semantic_chunks.jsonl and filters them
through multiple quality gates to produce a clean instruction-output dataset.

Quality Gates:
  1. Command allowlist — output must start with a known Synopsys command prefix
  2. Blocklist rejection — removes VCS, SAIF, SVF, Verilog, simulation content
  3. Structure check — must contain at least one valid -flag or [get_*] pattern
  4. Length limits — rejects trivially short or absurdly long outputs
  5. Shell prompt stripping — removes interactive shell prompts from output
  6. Deduplication — removes exact duplicates
"""

import json
import re

# ─────────────────────────────────────────────────────────────
# ALLOWLIST: Valid Synopsys EDA command prefixes
# Source: ICC2, DC, PT, Formality, StarRC user manuals
# An output must BEGIN with one of these to be accepted.
# ─────────────────────────────────────────────────────────────
SYNOPSYS_COMMAND_PREFIXES = {
    # IC Compiler II (ICC2) — Physical Design
    "initialize_floorplan", "create_floorplan", "set_floorplan",
    "place_cells", "place_opt", "refine_placement",
    "create_placement", "legalize_placement",
    "set_placement_status", "set_cell_location",
    "clock_opt", "synthesize_clock_trees", "compute_clock_latency",
    "route_auto", "route_global", "route_track", "route_detail",
    "route_opt",
    "check_routes", "check_drc", "check_design", "check_timing",
    "check_legality",
    "save_block", "open_block", "create_block", "copy_block",
    "create_lib", "open_lib",
    "create_voltage_area", "create_power_domain",
    "create_pg_ring", "create_pg_mesh", "create_pg_strap",
    "create_pg_std_cell_conn",
    "compile_pg",

    # Design Compiler (DC) — Logic Synthesis
    "compile", "compile_ultra", "compile_ultra_ungroup",
    "analyze", "elaborate", "link",
    "read_verilog", "read_sverilog", "read_vhdl", "read_sdc",
    "read_saif", "read_lib", "read_db",
    "write", "write_sdc", "write_sdf", "write_saif",
    "write_file", "write_verilog",
    "report_area", "report_timing", "report_power",
    "report_constraint", "report_qor", "report_cell",
    "report_net", "report_port", "report_design",
    "report_hierarchy",
    "set_max_area", "set_max_fanout", "set_max_transition",
    "set_max_capacitance",
    "group_path", "set_multicycle_path", "set_false_path",
    "set_input_delay", "set_output_delay",
    "set_load", "set_drive", "set_driving_cell",
    "set_dont_touch", "set_dont_use",
    "set_ideal_network", "set_ideal_latency",
    "uniquify", "ungroup", "group",
    "define_design_lib",

    # PrimeTime (PT) — Static Timing Analysis
    "create_clock", "create_generated_clock",
    "set_clock_groups", "set_clock_uncertainty",
    "set_clock_transition", "set_clock_latency",
    "set_propagated_clock",
    "update_timing", "report_clock",
    "get_timing_paths",

    # Common / Shared Commands
    "set_app_options", "get_app_options",
    "set_attribute", "get_attribute",
    "set_scenario_options", "create_scenario",
    "get_cells", "get_nets", "get_pins", "get_ports",
    "get_clocks", "get_libs", "get_lib_cells",
    "current_design", "current_instance",
    "remove_attribute", "remove_constraint",
    "reset_design",
    "get_license", "remove_license",
    "redirect",
    "set_svf", "set_verification_top",
    "verify_design",
    "source",
}

# ─────────────────────────────────────────────────────────────
# BLOCKLIST: Patterns that indicate contaminated / non-TCL content
# If ANY of these appear in the output, the example is rejected.
# ─────────────────────────────────────────────────────────────
BLOCKLIST_PATTERNS = [
    # Simulation / VCS
    r'%vcs', r'vcs\s+-', r'simv', r'sverilog', r'\.sv\b',
    r'SAIFILE', r'SAIFVERSION', r'TIMESCALE', r'DURATION',
    r'INSTANCE.*INSTANCE', r'\(T0\s+\d+\)', r'\(T1\s+\d+\)',
    # SVF / Formality contamination
    r'set_svf\s+\./',
    # Verilog / VHDL source constructs
    r'\bmodule\b', r'\bendmodule\b', r'\balways\b', r'\bwire\b',
    r'\breg\b\s+\[', r'\bbegin\b.*\bend\b',
    # C/Python/Shell code
    r'#include', r'def\s+\w+\(', r'import\s+\w+',
    r'\bif\s*\(', r'\bfor\s*\(',
    # Fabricated numerical results (model describing output, not commands)
    r'=\s*\d+\s*mW', r'=\s*\d+\s*MHz', r'TotalPower',
    # Shell meta-characters not valid in Tcl
    r'\$\(', r'&&', r'\|\|',
    # HTML / Markdown artifacts
    r'<[a-z]+>', r'&gt;', r'&lt;',
]

# ─────────────────────────────────────────────────────────────
# Shell prompt patterns to strip from outputs
# ─────────────────────────────────────────────────────────────
SHELL_PROMPT = re.compile(r'^[a-zA-Z0-9_]+>\s*', re.MULTILINE)
BLOCKLIST_RE = [re.compile(p, re.IGNORECASE | re.DOTALL) for p in BLOCKLIST_PATTERNS]


def is_valid_tcl(code: str) -> bool:
    """
    Runs all quality gates against a candidate Tcl code block.
    Returns True only if the code passes every gate.
    """
    stripped = code.strip()

    # Gate 1: Length — reject trivially short or absurdly long examples
    if len(stripped) < 10 or len(stripped) > 800:
        return False

    # Gate 2: Allowlist — first token must be a known Synopsys command
    first_token = stripped.split()[0].lstrip("#").lower()
    # Also handle multi-line blocks where the first meaningful line matters
    first_meaningful = next(
        (l.strip() for l in stripped.splitlines()
         if l.strip() and not l.strip().startswith("#")),
        ""
    )
    first_command = first_meaningful.split()[0].lower() if first_meaningful else ""
    if first_command not in SYNOPSYS_COMMAND_PREFIXES and first_token not in SYNOPSYS_COMMAND_PREFIXES:
        return False

    # Gate 3: Blocklist — reject if any contamination pattern matches
    for pattern in BLOCKLIST_RE:
        if pattern.search(stripped):
            return False

    # Gate 4: Structure — must have at least one flag OR a [get_*] call
    has_flag = bool(re.search(r'\s-[a-z_]+', stripped))
    has_get  = bool(re.search(r'\[get_\w+', stripped))
    if not has_flag and not has_get:
        return False

    return True


def clean_code(code: str) -> str:
    """Strip shell prompts and normalise whitespace."""
    code = SHELL_PROMPT.sub('', code)
    # Normalise continuation backslashes (ensure space before them)
    code = re.sub(r'(?<! )\\$', r' \\', code, flags=re.MULTILINE)
    return code.strip()


def make_instruction(metadata: dict, code: str) -> str:
    """
    Generate a natural-language instruction from the chunk's header context.
    Falls back to inferring intent from the command name itself.
    """
    header = metadata.get("Header 2") or metadata.get("Header 1") or ""

    # Clean up header — remove markdown formatting characters
    header = re.sub(r'[#*`_]', '', header).strip().lower()

    if header and len(header) > 5:
        return f"Write the Tcl command for {header}."
    else:
        # Fall back to using the first command token as a hint
        first_cmd = code.strip().split()[0]
        return f"Write the Tcl command to use {first_cmd}."


def generate_dataset(input_jsonl: str, output_jsonl: str):
    print("=" * 60)
    print("Generating Cleaned SFT Dataset")
    print("=" * 60)

    total_chunks      = 0
    extracted_raw     = 0
    rejected_length   = 0
    rejected_allowlist= 0
    rejected_blocklist= 0
    rejected_structure= 0
    accepted          = 0

    dataset = []

    with open(input_jsonl, 'r', encoding='utf-8') as f:
        for line in f:
            total_chunks += 1
            data     = json.loads(line)
            content  = data.get("content", "")
            metadata = data.get("metadata", {})

            # Extract all fenced code blocks (``` or ```tcl)
            code_blocks = re.findall(
                r'```(?:tcl|shell|bash|sh)?\n(.*?)\n```',
                content, re.DOTALL | re.IGNORECASE
            )
            extracted_raw += len(code_blocks)

            for raw_code in code_blocks:
                cleaned = clean_code(raw_code)

                # Run gates individually for accurate rejection stats
                if len(cleaned) < 10 or len(cleaned) > 800:
                    rejected_length += 1
                    continue

                first_meaningful = next(
                    (l.strip() for l in cleaned.splitlines()
                     if l.strip() and not l.strip().startswith("#")),
                    ""
                )
                first_cmd = first_meaningful.split()[0].lower() if first_meaningful else ""
                if first_cmd not in SYNOPSYS_COMMAND_PREFIXES:
                    rejected_allowlist += 1
                    continue

                blocked = False
                for pattern in BLOCKLIST_RE:
                    if pattern.search(cleaned):
                        blocked = True
                        break
                if blocked:
                    rejected_blocklist += 1
                    continue

                has_flag = bool(re.search(r'\s-[a-z_]+', cleaned))
                has_get  = bool(re.search(r'\[get_\w+', cleaned))
                if not has_flag and not has_get:
                    rejected_structure += 1
                    continue

                # All gates passed — add to dataset
                instruction = make_instruction(metadata, cleaned)
                dataset.append({"instruction": instruction, "output": cleaned})
                accepted += 1

    # Deduplicate on exact output match
    seen = set()
    unique = []
    for item in dataset:
        key = item["output"].strip()
        if key not in seen:
            seen.add(key)
            unique.append(item)

    duplicates_removed = accepted - len(unique)

    # Write output
    with open(output_jsonl, 'w', encoding='utf-8') as out:
        for item in unique:
            out.write(json.dumps(item, ensure_ascii=False) + "\n")

    # Report
    print(f"\n  Total chunks scanned    : {total_chunks:,}")
    print(f"  Raw code blocks found   : {extracted_raw:,}")
    print(f"  Rejected (too short/long): {rejected_length:,}")
    print(f"  Rejected (not allowlisted): {rejected_allowlist:,}")
    print(f"  Rejected (contamination) : {rejected_blocklist:,}")
    print(f"  Rejected (no structure)  : {rejected_structure:,}")
    print(f"  Accepted (before dedup)  : {accepted:,}")
    print(f"  Duplicates removed       : {duplicates_removed:,}")
    print(f"  ─────────────────────────────")
    print(f"  Final clean examples     : {len(unique):,}")
    print(f"\n  Saved to: {output_jsonl}")
    print("=" * 60)


if __name__ == "__main__":
    INPUT_JSONL  = "./semantic_chunks.jsonl"
    OUTPUT_JSONL = "./dataset.jsonl"
    generate_dataset(INPUT_JSONL, OUTPUT_JSONL)
