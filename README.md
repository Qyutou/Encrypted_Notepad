# Encrypted-Notepad
Simple notepad that can encrypt/decrypt text files.

![Example 1](https://github.com/Qyutou/Encrypted_Notepad/blob/edd69637fd2a2e355cbb2892db2460e402ea3236/example/encrypted_notepad_example.png)
## Installation
```bash
$ git clone https://github.com/Qyutou/encrypted-notepad.git
$ cd Encrypted_Notepad 
$ sudo make install 
```
`make install` also copy .desktop file and icon from data folder to /usr/share/ folder.
Instead of `make install` the `python3 setup.py install` or `pip3 install .` can be used to install application.
## Usage
If the application was installed using `make install` then you can start application from both menu and command-line. Starting from command-line:
```bash
# To open Encrypted_Notepad
$ encrypted_notepad
# To open the certain file in Encrypted_Notepad
$ encrypted_notepad <FILE_NAME>
```
Then you can create new file/open file that already exists and select "save as (encoded)" option under the "file" section to encrypt the file or select "open (encoded)" to open encrypted file.