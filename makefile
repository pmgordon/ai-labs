TEST_PATH=./tests
MODULE_NAME="labs"

test:
	pytest --verbose --color=yes $(TEST_PATH)

coverage:
	pytest -vv --color=yes --cov-report term-missing  --cov=$(MODULE_NAME)

lint:
	pylint --rcfile=.pylintrc -f colorized */*py

init:
	python3 -m venv .pyenv

pipreq:
	pip install -r requirements.txt
