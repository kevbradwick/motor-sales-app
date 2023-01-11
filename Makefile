.PHONY: fmt
fmt:
	poetry run python -m isort .
	poetry run python -m black .

.PHONY: dev
dev:
	FLASK_APP=server:app poetry run flask run --debugger --reload