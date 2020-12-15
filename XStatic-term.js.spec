#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : XStatic-term.js
Version  : 0.0.7.0
Release  : 26
URL      : http://pypi.debian.net/XStatic-term.js/XStatic-term.js-0.0.7.0.tar.gz
Source0  : http://pypi.debian.net/XStatic-term.js/XStatic-term.js-0.0.7.0.tar.gz
Summary  : term.js 0.0.7 (XStatic packaging standard)
Group    : Development/Tools
License  : MIT
Requires: XStatic-term.js-python = %{version}-%{release}
Requires: XStatic-term.js-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
--------------
        
        term.js javascript library packaged for setuptools (easy_install) / pip.

%package python
Summary: python components for the XStatic-term.js package.
Group: Default
Requires: XStatic-term.js-python3 = %{version}-%{release}
Provides: xstatic-term.js-python

%description python
python components for the XStatic-term.js package.


%package python3
Summary: python3 components for the XStatic-term.js package.
Group: Default
Requires: python3-core
Provides: pypi(xstatic_term.js)

%description python3
python3 components for the XStatic-term.js package.


%prep
%setup -q -n XStatic-term.js-0.0.7.0
cd %{_builddir}/XStatic-term.js-0.0.7.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603409173
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
