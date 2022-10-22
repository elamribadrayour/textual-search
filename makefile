ci-init:
	pip install -r requirements.txt

ci-run:
	black --check . && \
	flake8 . && \
	mypy .

prod-requirements:
	cat \
	requirements/ml.txt \
	requirements/nlp.txt \
	requirements/fastapi.txt \
	>> requirements.txt

ci-requirements:
	cat \
	requirements/ml.txt \
	requirements/nlp.txt \
	requirements/fastapi.txt \
	requirements/ci.txt \
	>> requirements.txt