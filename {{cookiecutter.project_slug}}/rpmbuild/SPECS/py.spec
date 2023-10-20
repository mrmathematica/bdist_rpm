# Allow building noarch packages that contain binaries
%define _binaries_in_noarch_packages_terminate_build 0

# Use md5 file digest method. 
# The first macro is the one used in RPM v4.9.1.1
%define _binary_filedigest_algorithm 1
# This is the macro I find on OSX when Homebrew provides rpmbuild (rpm v5.4.14)
%define _build_binary_file_digest_algo 1

# Use gzip payload compression
%define _binary_payload w9.gzdio 

%undefine __brp_mangle_shebangs

Name: python-{{ cookiecutter.package_name }}
Version: {{ cookiecutter.package_version }}
Release: 1
Summary: Python package numpy as RPM

License: {{ cookiecutter.license }}
AutoReqProv: no

Requires: {{ cookiecutter.python_rpm_install }}
%description
Python package {{ cookiecutter.package_name }}=={{ cookiecutter.package_version }} as RPM

%prep
# noop

%build
# noop

%install
python3 -m pip install -U pip setuptools wheel
pip install -t $RPM_BUILD_ROOT/usr/local/lib/python3.11/site-packages {{ cookiecutter.package_name }}=={{ cookiecutter.package_version }}
if [ -d "$RPM_BUILD_ROOT/usr/local/lib/python3.11/site-packages/bin" ]; then
  mv $RPM_BUILD_ROOT/usr/local/lib/python3.11/site-packages/bin $RPM_BUILD_ROOT/usr/local/
fi

%clean
# noop

%files
/usr/local

%changelog

