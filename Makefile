clean: 
	find . -name \*.pyc -delete
	rm -rf build dist sepulsa_client.egg-info

publish-staging:
	twine upload --repository-url https://test.pypi.org/legacy/ dist/* --verbose

build-package:
	python setup.py sdist bdist_wheel

publish:
	twine upload dist/* --verbose

check-coverage:
	pytest --cov=./ --cov-report=xml

check-cc:
	radon cc sepulsa --total-average -s 

check-mi:
	radon mi sepulsa -s

check-raw:
	radon raw sepulsa -s

check-hal:
	radon hal sepulsa -f
