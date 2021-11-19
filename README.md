OSPM stands for "OpenShift Project Manager".

OSPM is **both** a python package (that you can use in your own Python scripts, modules and packages) **and** a Command Line Interface (CLI) that you can use in a shell prompt.

For now, the package is small and simple enough to rely merely on the docstrings, so this Readme will focus on the CLI usage.


# Settings

Settings can be set using :
  - The system-wide configuration file *(/etc/ospm.conf)*
  - The unix-user's configuration file *(~/.ospm/ospm.conf)*
  - A specified configuration file (using the dedicated option when using the CLI, or by calling the `set_configuration_file` method of the `ConfigurationManager`)
  - Environment variables (the list is provided hereafter)
  - The Command-Line options when using the CLI