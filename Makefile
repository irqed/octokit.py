init:
	pip install -r requirements.txt

test:
	nosetests -xv --rednose tests

lint:
	pylint -r n octokit

flake:
	flake8 octokit

coverage:
	nosetests --with-coverage --cover-package=octokit

clean:
	find . -type f -name '*.pyc' -delete -print
	rm -rf __pycache__
