# Dynamic Import and  Remote HTTP/HTTPS Import in Memory from Storage v2.0

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

```python
if __name__ == '__main__':
    sys.meta_path.append(HTTPImporter("https://test.com"))
    print(sys.meta_path)
```
___
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
___ 
## License
[MIT](https://choosealicense.com/licenses/mit/)