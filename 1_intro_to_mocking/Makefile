define USAGE
Think-it moto workshop

Commands:
	init      Install Python dependencies with virtualenv
	test      Run linters, test db migrations and tests.

endef

export USAGE
help:
	@echo "$$USAGE"

.ONESHELL:
SHELL = /bin/bash
.SHELLFLAGS = -euo pipefail

all: init test

.PHONY: init test lint build

init:
	./init

test:
	./test
