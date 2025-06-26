run:
	@python app_server.py

run-docker:
	@docker run -p 5000:5000 pokemon-scout

build-docker:
	@docker build -t pokemon-scout .

clean:
	@find . -type d -name '__pycache__' -exec rm -rf {} +
	@find . -type f -name '*.pyc' -delete
	@find . -type f -name '*.pyo' -delete
	@find . -type d -name '.pytest_cache' -exec rm -rf {} +
	@find . -type d -name '.mypy_cache' -exec rm -rf {} +
	@rm -rf .coverage htmlcov dist build