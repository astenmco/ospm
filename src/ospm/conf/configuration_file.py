"""Configuration file handling (should be accessed over the ConfigurationManager)
"""
#Low-level imports
import os
from enum import Enum


class ConfigurationFileScope(Enum):
    SYSTEM = 1
    UNIX_USER = 2
    CURRENT_RUN = 3
        
class _ConfigurationFileModel:
    """Configuration File Model.
    """
    
    def __init__(self, scope: ConfigurationFileScope, path: os.path):
        """Initializer

        Args:
            scope (ConfigurationFileScope): Scope of the configuration file
            path (os.path): Path of the configuration file.
        """
        self._found = False
        self._parsed = False
        self._scope = scope
        self._path = path


    @property
    def path(self) -> os.path:
        """Path property

        Returns:
            [os.path]: The file's path.
        """
        return self._path
        
    @property
    def scope(self) -> ConfigurationFileScope:
        """Scope propery

        Returns:
            ConfigurationFileScope: The file's scope.
        """
        return self._scope
    

class ConfigurationFile:
    """Configuration File Handler (controller)
    """
    


    def __init__(self, scope, path):
        self._model = _ConfigurationFileModel(scope, path)
    
    def parse(self):
        pass
    
    def __str__(self) -> str:
        string = "Configuration file:\n" \
                +f"  Scope: {ConfigurationFileScope(self._model.scope).name}\n" \
                +f"  Priority: {ConfigurationFileScope(self._model.scope).value}\n" \
                +f"  Path: {self._model.path}"
        return string
    
    def __repr__(self) -> str:
        return self.__str__()
