FROM {{ cookiecutter.base_image }}

RUN yum update -y
RUN yum install -y gcc make rpm-build {{ cookiecutter.python_rpm_install }} {{ cookiecutter.python_rpm_extra }}
ADD rpmbuild rpmbuild

RUN rpmbuild -D "_topdir $(pwd)/rpmbuild" -bb rpmbuild/SPECS/py.spec
