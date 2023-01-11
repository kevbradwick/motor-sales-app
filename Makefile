.PHONY: fmt
fmt:
	poetry run python -m isort .
	poetry run python -m black .

.PHONY: requirements.txt
requirements.txt:
	poetry export --without-hashes > requirements.txt