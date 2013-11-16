init:
	pip install -r requirements.txt

test:
	py.test

publish:
	python setup.py sdist upload
	python setup.py bdist_wheel upload