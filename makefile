ci-init:
	pip install -r requirements.txt

ci-run:
	black --check . && \
	flake8 . && \
	mypy .

prod-requirements:
	cat \
	requirements/nlp.txt \
	requirements/ml.txt \
	requirements/fastapi.txt \
	>> requirements.txt