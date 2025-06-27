install:
	@pip install -r requirements.txt
run:
	@python app_server.py

build-docker:
	@docker build -t pokemon-scout .

run-docker:
	@docker run -p 5000:5000 \
	-v `pwd`/data/default_pokemons.json:/app/data/default_pokemons.json \
	pokemon-scout

test:
	@python -m pytest

clean:
	@find . -type d -name '__pycache__' -exec rm -rf {} +
	@find . -type f -name '*.pyc' -delete
	@find . -type f -name '*.pyo' -delete
	@find . -type d -name '.pytest_cache' -exec rm -rf {} +
	@find . -type d -name '.mypy_cache' -exec rm -rf {} +
	@rm -rf .coverage htmlcov dist build