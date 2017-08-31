DOCUMENTATION_DIRECTORY := docs

.PHONY: init
init:
	@pip install -r requirements.txt

.PHONY: install
install:
	@./setup.py install --optimize=1 --record=install_log.txt

.PHONY: build
build:
	@./setup.py build

.PHONY: check
check:
	@flake8 --show-source --statistics cmus_notify tests

.PHONY: coverage
coverage:
	@coverage run --source cmus_notify -m py.test
	@coverage report

.PHONY: test
test:
	@./setup.py test

.PHONY: doc
doc:
	@sphinx-apidoc --force -o $(DOCUMENTATION_DIRECTORY) ./cmus_notify/

.PHONY: html
html: doc
	@$(MAKE) -C $(DOCUMENTATION_DIRECTORY) html

.PHONY: doc
man: doc
	@$(MAKE) -C $(DOCUMENTATION_DIRECTORY) man

.PHONY: clean
clean:
	@rm -rf dist/
	@rm -rf build/
	@rm -rf cmus_notify.egg-info/
	@find . -name '*.pyc' -exec rm {} \;
	@find . -name '__pycache__' -exec rm -rf {} \;
	@rm -rf samples/
	@rm -rf data/
