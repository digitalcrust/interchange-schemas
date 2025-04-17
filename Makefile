all:
	poetry run python3 scripts/generate-schema.py


install:
	# Fail if graphviz is not installed
	# (it is needed for the PyGraphviz package)
	@command -v dot >/dev/null 2>&1 || { echo >&2 "Graphviz is not installed."; exit 1; }
	# Kind of desperate, but it works
	# https://github.com/pygraphviz/pygraphviz/issues/470
	poetry run python3 -m pip install \
		--config-settings="--global-option=build_ext" \
		--config-settings="--global-option=-I$(brew --prefix graphviz)/include/" \
		--config-settings="--global-option=-L$(brew --prefix graphviz)/lib/" \
		pygraphviz
	poetry install

test:
	poetry run pytest --tb=short -p no:warnings -v

fixtures:
	./scripts/download-fixtures.sh
