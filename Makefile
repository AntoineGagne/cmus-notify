.PHONY: check
check: check-format lint test

.PHONY: check-format
check-format:
	@uv run ruff format --check --diff

.PHONY: format
format:
	@uv run ruff format

.PHONY: lint
lint:
	@uv run ruff check --quiet

.PHONY: test
test:
	@uv run pytest

.PHONY: clean
clean:
	@uv clean
