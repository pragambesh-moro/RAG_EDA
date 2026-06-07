<!-- image -->

Home &gt; VCS QuickStart &gt; Setting Up the Environment

## Setting Up the Environment

Before running Synopsys ®  tools, the Synopsys Common Licensing (SCL) software must be installed and configured the license key file retrieved, and the license file environment variable defined.

You must define the LM\_LICENSE\_FILE license environment variable to point to your license file using the followin command:

```
% setenv LM_LICENSE_FILE < path_to_the_license_file >
```

For detailed information about SCL installation and setup, see the Synopsys Common Licensing Administration Guide on SolvNetPlus ®  online support site.

For the list of supported platforms for VCS and Verdi, see VCS Release Notes and Verdi Release Notes respective Perform the following steps in C (CSH) shell to set up your environment:

- VCS
- ●

Set the VCS\_HOME environment variable to the path where VCS is installed: % setenv VCS\_HOME &lt; VCS\_installation\_path &gt; Set your UNIX PATH variable to $VCS\_HOME/bin : % set path = ($VCS\_HOME/bin $path) Verdi Set the VERDI\_HOME environment variable to point to the installation directory: % setenv VERDI\_HOME &lt; Verdi\_installation\_path &gt; Set your UNIX PATH variable to $VERDI\_HOME/bin : % set path = ($VERDI\_HOME/bin $path)

Note: Make sure to install the same release version of both VCS and Verdi.

SolvNetPlus | VCS Support | © 2017 Synopsys, Inc. All Rights Reserved Feedback