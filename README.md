# Encrypted-Notepad
Simple notepad that can encrypt/decrypt text files.
## Installation
```bash
$ git clone https://github.com/Qyutou/encrypted-notepad.git
$ cd Encrypted_Notepad 
$ sudo make install 
```
`make install` also copy .desktop file and icon from data folder to /usr/share/ folder.
Instead of `make install` the `python3 setup.py install` or `pip3 install .` can be used to install application.
## Usage
If the application was installed using `make install` then you can start application from both menu and command-line.
#### Start from command-line:
```bash
# To open Encrypted_Notepad
$ encrypted_notepad
# To open the certain file in Encrypted_Notepad
$ encrypted_notepad <FILE_NAME>
```