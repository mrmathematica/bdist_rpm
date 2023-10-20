# Build rpm from pypthon package

Python used to have a build-in API named
[bdist_rpm](https://docs.python.org/3.11/distutils/apiref.html?highlight=bdist_rpm#module-distutils.command.bdist_rpm).
From python 3.12 on, it is removed. bdist_rpm only works with setup.py-style source trees, which is being replaced by
PEP 517 anyway.

So here is a [Cookiecutter template](https://cookiecutter.readthedocs.io/en/stable/) that I created, which should help
to build a rpm out of any python package. It will allow user to select base docker image and python rpm name, as well
as pypi package name and version. At the end, simply run `make` will create a rpm for the selected python package,
including all dependencies.
