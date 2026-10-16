VENV := .venv
BIN  := $(VENV)/bin
PORT ?= 8000
IMAGE ?= portfolio:local

.DEFAULT_GOAL := help
.PHONY: help install run dev test clean docker-build docker-run docker-stop

help:
	@grep -E '^[a-z-]+:.*## ' Makefile | awk -F ':.*## ' '{printf "  make %-13s %s\n", $$1, $$2}'

$(VENV):
	python3 -m venv $(VENV)

install: $(VENV)
	$(BIN)/pip install -r requirements-dev.txt

run:
	$(BIN)/uvicorn app.main:app --host 0.0.0.0 --port $(PORT)

dev:
	$(BIN)/uvicorn app.main:app --host 0.0.0.0 --port $(PORT) --reload

test:
	$(BIN)/pytest -q

clean:
	find . -name __pycache__ -type d -prune -exec rm -rf {} +
	rm -rf .pytest_cache

lint:
	$(BIN)/ruff check .

docker-build:
	docker build -t $(IMAGE) .

docker-run:
	docker run --rm --name portfolio -p $(PORT):8000 $(IMAGE)

docker-stop:
	docker stop portfolio
