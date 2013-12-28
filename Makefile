init:
	pip install -r requirements.txt

test:
	py.test --verbose -x

lint:
	pylint -r n octokit

flake:
	flake8 octokit

coverage:
	py.test --verbose --cov-report term --cov=octokit test_octokit.py

publish:
	python setup.py sdist upload
	python setup.py bdist_wheel upload

clean:
	find . -type f -name '*.pyc' -delete -print
	rm -rf __pycache__
