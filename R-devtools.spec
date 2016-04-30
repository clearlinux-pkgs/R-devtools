#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-devtools
Version  : 1.10.0
Release  : 26
URL      : http://cran.r-project.org/src/contrib/devtools_1.10.0.tar.gz
Source0  : http://cran.r-project.org/src/contrib/devtools_1.10.0.tar.gz
Summary  : Tools to Make Developing R Packages Easier
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: R-withr
Requires: R-httr
Requires: R-git2r
Requires: R-rstudioapi
Requires: R-whisker
BuildRequires : R-git2r
BuildRequires : R-httr
BuildRequires : R-knitr
BuildRequires : R-roxygen2
BuildRequires : R-rstudioapi
BuildRequires : R-testthat
BuildRequires : R-whisker
BuildRequires : R-withr
BuildRequires : clr-R-helpers

%description
# devtools
[![Build Status](https://travis-ci.org/hadley/devtools.svg?branch=master)](https://travis-ci.org/hadley/devtools)
[![AppVeyor Build Status](https://ci.appveyor.com/api/projects/status/github/hadley/devtools?branch=master&svg=true)](https://ci.appveyor.com/project/hadley/devtools)
[![Coverage Status](https://codecov.io/github/hadley/devtools/coverage.svg?branch=master)](https://codecov.io/github/hadley/devtools?branch=master)
[![CRAN_Status_Badge](http://www.r-pkg.org/badges/version/devtools)](http://cran.r-project.org/package=devtools)

%prep
%setup -q -c -n devtools

%build

%install
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --build  -l %{buildroot}/usr/lib64/R/library devtools
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library devtools


%files
%defattr(-,root,root,-)
