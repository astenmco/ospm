"""Configuration manager : the one and only entrypoint to the configuration package.
"""

# Low level imports
import os
import logging
import textwrap

# Local import
from ospm.conf.configuration_file import ConfigurationFile, ConfigurationFileScope


class ConfigurationManager:
    """ **SINGLETON**
    Handle the module's configuration (controller).
    The one and only configuration interface users should use.
    """
    __instance = None # There may only be one instance of ConfigurationManager (Singleton)

    def __new__(cls):
        """ Overloading the __new__ dunder in order to make ConfigurationManager a Singleton.
        """
        if ConfigurationManager.__instance is None:
            ConfigurationManager.__instance = super(ConfigurationManager, cls).__new__(cls)
            ConfigurationManager.__instance.__init_singleton()
        return ConfigurationManager.__instance


    class _ConfigurationModel:
        """ Data Model for the module's configuration.
        """
        
        def __init__(self):
            self._configuration_files = {
                'SYSTEM': None,
                'UNIX_USER': None,
                'CURRENT_RUN': None,
            }
        
        @property
        def configuration_files(self) -> ConfigurationFile:
            return self._configuration_files


    def __init_singleton(self):
        """ The singleton's initializer
            (usual __init__ dunder is called evey time one refers to ConfigurationManager())
        """
        self._model = ConfigurationManager._ConfigurationModel()

        self._model.configuration_files['SYSTEM'] = \
            ConfigurationFile(ConfigurationFileScope.SYSTEM,
                              "/etc/ospm.conf")
        self._model.configuration_files['UNIX_USER'] = \
            ConfigurationFile(ConfigurationFileScope.UNIX_USER,
                              os.path.expandvars('$HOME/.conf/ospm.conf'))


    def set_configuration_file(self, conf_file_path) -> bool:
        """Specify a configuration file to use.

        Args:
            conf_file_path ([PATH]): Configuration file path.

        Returns:
            Bool: True if the operation was a success.
        """
        if conf_file_path:
            if os.path.isfile(conf_file_path):
                self._model._provided_configuration_file = \
                    ConfigurationFile(ConfigurationFileScope.CURRENT_RUN,
                                      os.path.expandvars(conf_file_path))
                return self._provided_configuration_file.parse()
            else:
                logging.error(f"Could not find configuration file at \"{conf_file_path}\".")
                exit(1)
    
    def __str__(self):
        result = "Settings can be set using :\n" \
               + "  - The system-wide configuration file\n" \
               + "  - The unix-user's configuration file\n" \
               + "  - A specified configuration file\n" \
               + "  - Environment variables\n" \
               + "  - The system-wide configuration file\n" \
                "Using the following configuration files (values are overrided by priority order) :\n" \
               + "  - System-wide configuration file :\n" \
               + textwrap.indent(str(self._model.configuration_files['SYSTEM']), '      ') +"\n" \
               + "  - Unix-user configuration file :\n" \
               + textwrap.indent(str(self._model.configuration_files['UNIX_USER']), '      ') +"\n" \
               + "  - Specified configuration file for this run :\n" \
               + textwrap.indent(str(self._model.configuration_files['CURRENT_RUN']), '      ')
        return result
    
    def __repr__(self):
        return self.__str__()
