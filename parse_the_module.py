import importlib
import sys
from typing import Union

import re
import requests

from config import HEADERS
from loader import ModuleLoader
from finder import ModuleFinder
from path_constructor import StorageViewCreater


class ImporterModule(StorageViewCreater):
    def __init__(self):
        super().__init__()
        self._modules_for_import: list = []

    # todo: handler for - from foo import Foo ... and so on
    def _get_modules_for_import(self, code) -> None:
        import_list = re.findall(r"(import\s[a-zA-Z0-9]{,20}\r\n|"
                                 r"from\s[a-zA-Z0-9]{,20}\simport\s[a-zA-Z0-9]{,10}\r\n)", code)
        for m in import_list:
            module = m.split(" ")[1].replace("\r\n", "")
            self._modules_for_import.append(module)

    def _download_module_in_memory(self, module_name: str) -> tuple[str, dict[str, str]]:
        module_url = self.dict_of_modules_url[module_name]
        response = requests.get(module_url, headers=HEADERS, verify=False)
        if response.ok:
            module = {module_name: response.text}
            return module_name, module
        else:
            print(f"[-] Response: {response}.\n"
                  f"[-] Trouble with download.")

    @staticmethod
    def _import_module(module_name: str, module: dict) -> None:
        finder_object = ModuleFinder(ModuleLoader(module))
        sys.meta_path.append(finder_object)
        importlib.import_module(module_name)

    def run_importer(self, module_name: str) -> None:
        module_name, module = self._download_module_in_memory(module_name)
        try:
            self._import_module(module_name, module)
        except ModuleNotFoundError:
            self._get_modules_for_import(module[module_name])
            print(self._modules_for_import)
            for m in self._modules_for_import:
                self.run_importer(m)


if __name__ == '__main__':
    g = ImporterModule()

    g.run_importer('foo')
    # print(g.is_module_imported("foo"))
    import bar

    bar.bar()
    import foo

    # from foo import Foo
    # Foo()
    foo.foo()
    import qwe
    qwe.qwe()
