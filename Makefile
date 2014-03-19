init:
	pip install -r requirements.txt

test:
	nosetests -xv tests

lint:
	pylint -r n octokit

flake:
	flake8 octokit

coverage:
	nosetests --with-coverage tests

publish:
	python setup.py sdist upload
	python setup.py bdist_wheel upload

clean:
	find . -type f -name '*.pyc' -delete -print
	rm -rf __pycache__
