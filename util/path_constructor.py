import requests
from bs4 import BeautifulSoup

from config import URL_TO_MODULE_STORAGE, HEADERS


class StorageViewCreater:
    def __init__(self):
        self._url = URL_TO_MODULE_STORAGE

        self._storage: list = []
        self._modules_in_storage: list = []
        self._packages_in_storage: list = []
        self.dict_of_modules_url: dict = {}

        self.run_constructor()

    def _get_data(self, new_url: str = None) -> bytes:
        if new_url:
            self._url = new_url

        response = requests.get(self._url, headers=HEADERS, verify=False)
        if response.ok:
            return response.content
        else:
            print(f"[-] Response: {response}.\n"
                  f"[-] Check url to storage in config.")

    def _make_infrastructure(self, data: bytes) -> None:
        soup = BeautifulSoup(data, 'html.parser')
        for href in soup.find_all('a'):
            file_path = self._url + href.text
            self._storage.append(file_path)
        self._sort_storage()

    def _sort_storage(self) -> None:
        for file in self._storage:
            if "__pycache__" in file:
                continue
            elif "__init__.py" in file:
                continue
            elif file.endswith("/"):
                self._packages_in_storage.append(file)
            else:
                self._modules_in_storage.append(file)
        self._storage = []

    def _check_package_in_storage(self) -> None:
        if self._packages_in_storage:
            for pkg_url in self._packages_in_storage:
                self._make_infrastructure(self._get_data(pkg_url))

    def _create_module_dict(self) -> None:
        modules_names_list = []
        for url in self._modules_in_storage:
            modules_names_list.append(url.replace(URL_TO_MODULE_STORAGE, "").replace(".py", "").replace("/", "."))
        self.dict_of_modules_url = dict(zip(modules_names_list, self._modules_in_storage))

    def run_constructor(self):
        result = self._get_data()
        self._make_infrastructure(result)
        self._check_package_in_storage()
        self._create_module_dict()
