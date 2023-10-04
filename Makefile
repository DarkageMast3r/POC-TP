build:


clean:


install: src/install.py
	python3 src/install.py


src/install.py:
	$(error Installation file does not exist!)
