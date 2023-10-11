source_files = main.py model.py
installation_files = model.pkl vectorizer.pkl

.PHONY: build
build: $(source_files:%=src/%) $(installation_files)
	python3 src/main.py

.PHONY: clean
clean:
	del $(installation_files)
	
.PHONY: install
install: 
	pip install -U scikit-learn
	pip install pandas

src/%.py:
	$(error Missing file $@)

$(installation_files):
	python3 src/install.py
