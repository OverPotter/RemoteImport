import importlib.util
import os
import sys
from typing import Union

from config import PATH_TO_MODULE_STORAGE


class DynamicImport:

    @staticmethod
    def check_path(path: str) -> bool:
        if path is not None:
            return True
        else:
            return False

    def append_package_in_sys(self) -> None:
        if self.check_path(PATH_TO_MODULE_STORAGE):
            module_path = os.path.abspath(PATH_TO_MODULE_STORAGE)
            if os.path.exists(module_path):
                sys.path.append(module_path)
            else:
                print(f'[-] File path: {module_path} not found.')

    @staticmethod
    def check_module(module_name: str = "import_test") -> Union[object, None]:
        module_spec = importlib.util.find_spec(module_name)
        if module_spec is None:
            print(f'[-] Module: {module_name} not found.')
            return None
        else:
            print(f'[+] Module: {module_name} can be imported!')
            return module_spec

    @staticmethod
    def test_import_module_from_spec(module_name: str = "import_test") -> bool:
        try:
            module = importlib.import_module(module_name)
            module.test()
            return True
        except Exception as e:
            print(f"[-] Exception: {e}")
            return False


if __name__ == '__main__':
    r = DynamicImport()
    r.append_package_in_sys()
    r.test_import_module_from_spec()
