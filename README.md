# Dynamic Import and  Remote HTTP/HTTPS Import in Memory from Storage

Dynamic Import and Remote HTTP/HTTPS Import is a Python module to import modules into memory without writing them to disk.

I will not suggest how this can be used. :shipit:
___
![](https://img.shields.io/badge/python-3.9-blueviolet)
![](https://img.shields.io/github/last-commit/OverPotter/RemoteImport?color=blueviolet)
![](https://img.shields.io/github/issues-pr/OverPotter/RemoteImport?color=blueviolet)
![](https://img.shields.io/github/forks/OverPotter/RemoteImport?style=social)
___
## Installation
Use the git to install remote import.
```bash
git clone https://github.com/OverPotter/RemoteImport.git
```
___
## Usage Dynamic Import

Set params in config file.

For Example:
```python
PATH_TO_MODULE_STORAGE = "Z:\\Users\\UrPCName\\Desktop\\storage\\"
```
Add import_test.py in storage with code.
```python
def test():
    print("[+] Import test -> Successful.")
    return True
```
After that check the connection with the storage.
```python
if __name__ == '__main__':
    test = DynamicImport()
    test.append_package_in_sys()
    test.test_import_module_from_spec()
```

## Usage Remote HTTP/HTTPS Import
Set params in config file.

For Example:
```python
URL_TO_MODULE_STORAGE = "http://127.0.0.1:8000/storage/"
```
_(if anything, you can run a test server from terminal with command `python -m http.server 8000` or `python3 -m http.server 8000`)_

Create test storage:
```bash
---storage
|   ---foo.py
|   ---bar.py
|   ---qwe.py
```
Import bar.py and qwe.py in foo.py.
```python
import bar
import qwe
```
After importing the foo module, it loads itself and its dependencies into memory without traces on the computer's hard disk. And we can use its dependencies.
```python
if __name__ == '__main__':
    HTTPImporterModule().run_importer('foo')

    import bar
    bar.bar()
    import foo
    from foo import Foo
    Foo()
    foo.foo()
    import qwe
    qwe.qwe()
```
___
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
___
## License
[MIT](https://choosealicense.com/licenses/mit/)