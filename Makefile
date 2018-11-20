venv:
	python3.6 -m venv venv

test:
	PYTHONPATH=src/ python -m unittest discover tests/

coverage:
	PYTHONPATH=src/ coverage run --source src/ -m unittest discover tests/
	coverage html