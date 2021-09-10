PYTHON = python3

.DEFAULT_GOAL = help

help:
	@echo "To install type: make install"
	@echo "To uninstall type: make uninstall"
	@echo "To run type: make run"

install:
	pip3 install .
	cp data/Encrypted\ Notepad.desktop /usr/share/applications
	cp data/encrypted_notepad_icon.png /usr/share/icons/hicolor/48x48/apps
	
uninstall:
	pip3 uninstall encrypted_notepad
	rm /usr/share/applications/Encrypted\ Notepad.desktop
	rm /usr/share/icons/hicolor/48x48/apps/encrypted_notepad_icon.png

run:
	python3 src/encrypted_notepad/main.py