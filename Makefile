source_files = main.py model.py


.PHONY: build
build: $(source_files:%=src/%) $(installation_files)
	python3 src/main.py
	
.PHONY: install
install: 
	pip install -U scikit-learn
	pip install pandas
	python3 src/install.py

src/%.py:
	$(error Missing file $@)
