import importlib
from importlib.abc import MetaPathFinder


class ModuleFinder(MetaPathFinder):

    def __init__(self, loader):
        self._loader = loader

    def find_spec(self, fullname, path, target=None):

        if self._loader.has_module(fullname):
            return importlib.machinery.ModuleSpec(fullname, self._loader)
