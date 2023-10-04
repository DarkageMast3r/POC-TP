source_files = main.py
installation_files = model.pkl

.PHONY: build
build: $(source_files:%=src/%) $(installation_files)
	python3 src/main.py

.PHONY: clean
clean:
	del $(installation_files)

src/%.py:
	$(error Missing file $@)

$(installation_files):
	python3 src/install.py
