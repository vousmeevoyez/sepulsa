clean: 
	find . -name \*.pyc -delete
	rm -rf build dist oy_client.egg-info

publish-staging:
	twine upload --repository-url https://test.pypi.org/legacy/ dist/* --verbose

build:
	python setup.py sdist bdist_wheel

publish:
	twine upload dist/* --verbose

check-coverage:
	pytest --cov=./ --cov-report=xml

check-cc:
	radon cc oy --total-average -s 

check-mi:
	radon mi oy -s

check-raw:
	radon raw oy -s

check-hal:
	radon hal oy -f
