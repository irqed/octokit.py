init:
	pip install -r requirements.txt

test:
	py.test --verbose

coverage:
	py.test --verbose --cov-report term --cov=octokit test_octokit.py

publish:
	python setup.py sdist upload
	python setup.py bdist_wheel upload
