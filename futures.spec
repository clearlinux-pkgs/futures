#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : futures
Version  : 3.0.5
Release  : 19
URL      : https://pypi.python.org/packages/source/f/futures/futures-3.0.5.tar.gz
Source0  : https://pypi.python.org/packages/source/f/futures/futures-3.0.5.tar.gz
Summary  : Backport of the concurrent.futures package from Python 3.2
Group    : Development/Tools
License  : BSD-2-Clause
Requires: futures-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : setuptools

%description
No detailed description available

%package python
Summary: python components for the futures package.
Group: Default

%description python
python components for the futures package.


%prep
%setup -q -n futures-3.0.5

%build
python2 setup.py build -b py2

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python test_futures.py
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
