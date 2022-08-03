import types
from importlib.abc import Loader


class ModuleLoader(Loader):

    def __init__(self, modules):
        self._modules = modules

    def has_module(self, fullname):
        return fullname in self._modules

    def create_module(self, spec):
        if self.has_module(spec.name):
            module = types.ModuleType(spec.name)
            exec(self._modules[spec.name], module.__dict__)
            return module

    def exec_module(self, module):
        pass
