#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : futures
Version  : 3.1.1
Release  : 27
URL      : http://pypi.debian.net/futures/futures-3.1.1.tar.gz
Source0  : http://pypi.debian.net/futures/futures-3.1.1.tar.gz
Summary  : Backport of the concurrent.futures package from Python 3.2
Group    : Development/Tools
License  : Python-2.0
Requires: futures-legacypython
Requires: futures-python3
Requires: futures-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
No detailed description available

%package legacypython
Summary: legacypython components for the futures package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the futures package.


%package python
Summary: python components for the futures package.
Group: Default
Requires: futures-legacypython
Requires: futures-python3

%description python
python components for the futures package.


%package python3
Summary: python3 components for the futures package.
Group: Default
Requires: python3-core

%description python3
python3 components for the futures package.


%prep
%setup -q -n futures-3.1.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507153795
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python test_futures.py
%install
export SOURCE_DATE_EPOCH=1507153795
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
