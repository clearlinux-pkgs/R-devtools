#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-devtools
Version  : 1.12.0
Release  : 37
URL      : https://cran.r-project.org/src/contrib/devtools_1.12.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/devtools_1.12.0.tar.gz
Summary  : Tools to Make Developing R Packages Easier
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+ MIT
Requires: R-devtools-lib
Requires: R-git2r
Requires: R-httr
Requires: R-markdown
Requires: R-memoise
Requires: R-rstudioapi
Requires: R-whisker
Requires: R-withr
BuildRequires : R-git2r
BuildRequires : R-httr
BuildRequires : R-knitr
BuildRequires : R-markdown
BuildRequires : R-memoise
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

%package lib
Summary: lib components for the R-devtools package.
Group: Libraries

%description lib
lib components for the R-devtools package.


%prep
%setup -q -c -n devtools

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1492796173

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1492796173
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library devtools
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library devtools || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/devtools/DESCRIPTION
/usr/lib64/R/library/devtools/INDEX
/usr/lib64/R/library/devtools/Meta/Rd.rds
/usr/lib64/R/library/devtools/Meta/features.rds
/usr/lib64/R/library/devtools/Meta/hsearch.rds
/usr/lib64/R/library/devtools/Meta/links.rds
/usr/lib64/R/library/devtools/Meta/nsInfo.rds
/usr/lib64/R/library/devtools/Meta/package.rds
/usr/lib64/R/library/devtools/Meta/vignette.rds
/usr/lib64/R/library/devtools/NAMESPACE
/usr/lib64/R/library/devtools/NEWS.md
/usr/lib64/R/library/devtools/R/devtools
/usr/lib64/R/library/devtools/R/devtools.rdb
/usr/lib64/R/library/devtools/R/devtools.rdx
/usr/lib64/R/library/devtools/doc/dependencies.Rmd
/usr/lib64/R/library/devtools/doc/dependencies.html
/usr/lib64/R/library/devtools/doc/index.html
/usr/lib64/R/library/devtools/help/AnIndex
/usr/lib64/R/library/devtools/help/aliases.rds
/usr/lib64/R/library/devtools/help/devtools.rdb
/usr/lib64/R/library/devtools/help/devtools.rdx
/usr/lib64/R/library/devtools/help/paths.rds
/usr/lib64/R/library/devtools/html/00Index.html
/usr/lib64/R/library/devtools/html/R.css
/usr/lib64/R/library/devtools/libs/symbols.rds
/usr/lib64/R/library/devtools/templates/CONDUCT.md
/usr/lib64/R/library/devtools/templates/NEWS.md
/usr/lib64/R/library/devtools/templates/README.Rmd
/usr/lib64/R/library/devtools/templates/README.md
/usr/lib64/R/library/devtools/templates/appveyor.yml
/usr/lib64/R/library/devtools/templates/codecov.yml
/usr/lib64/R/library/devtools/templates/cran-comments.md
/usr/lib64/R/library/devtools/templates/mit-license.txt
/usr/lib64/R/library/devtools/templates/packagename-package.r
/usr/lib64/R/library/devtools/templates/readme-rmd-pre-commit.sh
/usr/lib64/R/library/devtools/templates/revdep.R
/usr/lib64/R/library/devtools/templates/template.Rproj
/usr/lib64/R/library/devtools/templates/test-example.R
/usr/lib64/R/library/devtools/templates/testthat.R
/usr/lib64/R/library/devtools/templates/travis.yml

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/devtools/libs/devtools.so
