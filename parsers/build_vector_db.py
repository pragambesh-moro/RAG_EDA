################################################################################
# Copyright (c) 2026, Shiv Nadar University, Delhi NCR, India. All Rights
# Reserved. Permission to use, copy, modify and distribute this software for
# educational, research, and not-for-profit purposes, without fee and without a
# signed license agreement, is hereby granted, provided that this paragraph and
# the following two paragraphs appear in all copies, modifications, and
# distributions.
#
# IN NO EVENT SHALL SHIV NADAR UNIVERSITY BE LIABLE TO ANY PARTY FOR DIRECT,
# INDIRECT, SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES, INCLUDING LOST
# PROFITS, ARISING OUT OF THE USE OF THIS SOFTWARE.
#
# SHIV NADAR UNIVERSITY SPECIFICALLY DISCLAIMS ANY WARRANTIES, INCLUDING, BUT
# NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
# PARTICULAR PURPOSE. THE SOFTWARE PROVIDED HEREUNDER IS PROVIDED "AS IS". SHIV
# NADAR UNIVERSITY HAS NO OBLIGATION TO PROVIDE MAINTENANCE, SUPPORT, UPDATES,
# ENHANCEMENTS, OR MODIFICATIONS.
#
# Revision History:
# Date          By                     Change Notes
# ------------ ---------------------- ------------------------------------------ 
#               Pragambesh Moro        Initial commit
################################################################################

import json
import os
import time
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document

def build_local_vector_db(jsonl_path: str, persist_dir: str):
    print("Loading semantic chunks...")
    documents = []
    
    with open(jsonl_path, 'r', encoding='utf-8') as f:
        for line in f:
            data = json.loads(line)
            # Create LangChain Document objects
            documents.append(
                Document(
                    page_content=data["content"],
                    metadata=data["metadata"]
                )
            )
            
    print(f"Loaded {len(documents)} chunks.")
    
    # Initialize the high-performance BGE model configured for CPU
    print("Initializing BAAI/bge-small-en-v1.5 (CPU Optimized)...")
    # Using 'cpu' since RTX4070 is offline. The 24-core i9 will handle this easily.
    model_kwargs = {'device': 'cpu'}
    encode_kwargs = {'normalize_embeddings': True} # Cosine similarity requires normalized embeddings
    
    embeddings = HuggingFaceEmbeddings(
        model_name="BAAI/bge-small-en-v1.5",
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs
    )
    
    # Initialize ChromaDB
    print(f"Building Vector Database at {persist_dir}...")
    start_time = time.time()
    
    # Chroma processes in batches internally, but we can feed it the whole list.
    # It will embed the texts and save them directly to disk.
    vectorstore = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory=persist_dir,
        collection_name="synopsys_commands"
    )
    
    end_time = time.time()
    print(f"\nSuccess! Database fully built in {end_time - start_time:.2f} seconds.")
    print("Ready for Phase 3 Retrieval Testing.")

if __name__ == "__main__":
    INPUT_JSONL = "./semantic_chunks.jsonl"
    DB_DIRECTORY = "./chroma_db"
    
    build_local_vector_db(INPUT_JSONL, DB_DIRECTORY)
