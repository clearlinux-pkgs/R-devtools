#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-devtools
Version  : 2.4.5
Release  : 106
URL      : https://cran.r-project.org/src/contrib/devtools_2.4.5.tar.gz
Source0  : https://cran.r-project.org/src/contrib/devtools_2.4.5.tar.gz
Summary  : Tools to Make Developing R Packages Easier
Group    : Development/Tools
License  : MIT
Requires: R-cli
Requires: R-desc
Requires: R-ellipsis
Requires: R-fs
Requires: R-lifecycle
Requires: R-memoise
Requires: R-miniUI
Requires: R-pkgbuild
Requires: R-pkgdown
Requires: R-pkgload
Requires: R-profvis
Requires: R-rcmdcheck
Requires: R-remotes
Requires: R-rlang
Requires: R-roxygen2
Requires: R-rversions
Requires: R-sessioninfo
Requires: R-testthat
Requires: R-urlchecker
Requires: R-usethis
Requires: R-withr
BuildRequires : R-cli
BuildRequires : R-desc
BuildRequires : R-ellipsis
BuildRequires : R-fs
BuildRequires : R-lifecycle
BuildRequires : R-memoise
BuildRequires : R-miniUI
BuildRequires : R-mockery
BuildRequires : R-pkgbuild
BuildRequires : R-pkgdown
BuildRequires : R-pkgload
BuildRequires : R-profvis
BuildRequires : R-rcmdcheck
BuildRequires : R-remotes
BuildRequires : R-rlang
BuildRequires : R-roxygen2
BuildRequires : R-rversions
BuildRequires : R-sessioninfo
BuildRequires : R-testthat
BuildRequires : R-urlchecker
BuildRequires : R-usethis
BuildRequires : R-withr
BuildRequires : buildreq-R

%description
# devtools <img src="man/figures/logo.svg" align="right" height = 150/>
<!-- badges: start -->
[![R-CMD-check](https://github.com/r-lib/devtools/actions/workflows/R-CMD-check.yaml/badge.svg)](https://github.com/r-lib/devtools/actions/workflows/R-CMD-check.yaml)
[![Codecov test coverage](https://codecov.io/gh/r-lib/devtools/branch/main/graph/badge.svg)](https://app.codecov.io/gh/r-lib/devtools?branch=main)
[![CRAN_Status_Badge](https://www.r-pkg.org/badges/version/devtools)](https://cran.r-project.org/package=devtools)
<!-- badges: end -->

%prep
%setup -q -n devtools
cd %{_builddir}/devtools

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1665526655

%install
export SOURCE_DATE_EPOCH=1665526655
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/devtools/DESCRIPTION
/usr/lib64/R/library/devtools/INDEX
/usr/lib64/R/library/devtools/LICENSE
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
/usr/lib64/R/library/devtools/WORDLIST
/usr/lib64/R/library/devtools/doc/dependencies.Rmd
/usr/lib64/R/library/devtools/doc/dependencies.html
/usr/lib64/R/library/devtools/doc/index.html
/usr/lib64/R/library/devtools/help/AnIndex
/usr/lib64/R/library/devtools/help/aliases.rds
/usr/lib64/R/library/devtools/help/devtools.rdb
/usr/lib64/R/library/devtools/help/devtools.rdx
/usr/lib64/R/library/devtools/help/figures/lifecycle-archived.svg
/usr/lib64/R/library/devtools/help/figures/lifecycle-defunct.svg
/usr/lib64/R/library/devtools/help/figures/lifecycle-deprecated.svg
/usr/lib64/R/library/devtools/help/figures/lifecycle-experimental.svg
/usr/lib64/R/library/devtools/help/figures/lifecycle-maturing.svg
/usr/lib64/R/library/devtools/help/figures/lifecycle-questioning.svg
/usr/lib64/R/library/devtools/help/figures/lifecycle-stable.svg
/usr/lib64/R/library/devtools/help/figures/lifecycle-superseded.svg
/usr/lib64/R/library/devtools/help/figures/logo.svg
/usr/lib64/R/library/devtools/help/paths.rds
/usr/lib64/R/library/devtools/html/00Index.html
/usr/lib64/R/library/devtools/html/R.css
/usr/lib64/R/library/devtools/rstudio/addins.dcf
/usr/lib64/R/library/devtools/tests/spelling.R
/usr/lib64/R/library/devtools/tests/testthat.R
/usr/lib64/R/library/devtools/tests/testthat/_snaps/active.md
/usr/lib64/R/library/devtools/tests/testthat/_snaps/build-readme.md
/usr/lib64/R/library/devtools/tests/testthat/_snaps/check-win.md
/usr/lib64/R/library/devtools/tests/testthat/_snaps/package.md
/usr/lib64/R/library/devtools/tests/testthat/_snaps/run-source.md
/usr/lib64/R/library/devtools/tests/testthat/_snaps/sitrep.md
/usr/lib64/R/library/devtools/tests/testthat/archive.rds
/usr/lib64/R/library/devtools/tests/testthat/check-results-note.log
/usr/lib64/R/library/devtools/tests/testthat/helper.R
/usr/lib64/R/library/devtools/tests/testthat/shallowRepo/HEAD
/usr/lib64/R/library/devtools/tests/testthat/shallowRepo/config
/usr/lib64/R/library/devtools/tests/testthat/shallowRepo/description
/usr/lib64/R/library/devtools/tests/testthat/shallowRepo/info/exclude
/usr/lib64/R/library/devtools/tests/testthat/shallowRepo/objects/pack/pack-c4e0f1d1d68408f260cbbf0a533ad5f6bfd5524e.idx
/usr/lib64/R/library/devtools/tests/testthat/shallowRepo/objects/pack/pack-c4e0f1d1d68408f260cbbf0a533ad5f6bfd5524e.pack
/usr/lib64/R/library/devtools/tests/testthat/shallowRepo/packed-refs
/usr/lib64/R/library/devtools/tests/testthat/shallowRepo/refs/tags/v1.10.0
/usr/lib64/R/library/devtools/tests/testthat/shallowRepo/shallow
/usr/lib64/R/library/devtools/tests/testthat/test-active.R
/usr/lib64/R/library/devtools/tests/testthat/test-build-readme.R
/usr/lib64/R/library/devtools/tests/testthat/test-build-site.R
/usr/lib64/R/library/devtools/tests/testthat/test-check-doc.R
/usr/lib64/R/library/devtools/tests/testthat/test-check-win.R
/usr/lib64/R/library/devtools/tests/testthat/test-check.R
/usr/lib64/R/library/devtools/tests/testthat/test-install.R
/usr/lib64/R/library/devtools/tests/testthat/test-package.R
/usr/lib64/R/library/devtools/tests/testthat/test-reload.R
/usr/lib64/R/library/devtools/tests/testthat/test-run-examples.R
/usr/lib64/R/library/devtools/tests/testthat/test-run-source.R
/usr/lib64/R/library/devtools/tests/testthat/test-sitrep.R
/usr/lib64/R/library/devtools/tests/testthat/test-test.R
/usr/lib64/R/library/devtools/tests/testthat/test-uninstall.R
/usr/lib64/R/library/devtools/tests/testthat/test-utils.R
/usr/lib64/R/library/devtools/tests/testthat/test-vignettes.R
/usr/lib64/R/library/devtools/tests/testthat/testCheckExtrafile/DESCRIPTION
/usr/lib64/R/library/devtools/tests/testthat/testCheckExtrafile/NAMESPACE
/usr/lib64/R/library/devtools/tests/testthat/testCheckExtrafile/R/a.R
/usr/lib64/R/library/devtools/tests/testthat/testCheckExtrafile/an_extra_file
/usr/lib64/R/library/devtools/tests/testthat/testCheckExtrafile/man/a.Rd
/usr/lib64/R/library/devtools/tests/testthat/testError/DESCRIPTION
/usr/lib64/R/library/devtools/tests/testthat/testError/R/error.R
/usr/lib64/R/library/devtools/tests/testthat/testHelp/DESCRIPTION
/usr/lib64/R/library/devtools/tests/testthat/testHelp/NAMESPACE
/usr/lib64/R/library/devtools/tests/testthat/testHelp/R/foofoo.R
/usr/lib64/R/library/devtools/tests/testthat/testHelp/man/foofoo.Rd
/usr/lib64/R/library/devtools/tests/testthat/testMarkdownVignettes/DESCRIPTION
/usr/lib64/R/library/devtools/tests/testthat/testMarkdownVignettes/vignettes/test.Rmd
/usr/lib64/R/library/devtools/tests/testthat/testMissingNsObject/DESCRIPTION
/usr/lib64/R/library/devtools/tests/testthat/testMissingNsObject/NAMESPACE
/usr/lib64/R/library/devtools/tests/testthat/testMissingNsObject/R/a.R
/usr/lib64/R/library/devtools/tests/testthat/testPkgdown/DESCRIPTION
/usr/lib64/R/library/devtools/tests/testthat/testPkgdown/NAMESPACE
/usr/lib64/R/library/devtools/tests/testthat/testPkgdown/R/pkgdown-test-test.R
/usr/lib64/R/library/devtools/tests/testthat/testPkgdown/_pkgdown.yml
/usr/lib64/R/library/devtools/tests/testthat/testPkgdown/man/pkgdown_test_test.Rd
/usr/lib64/R/library/devtools/tests/testthat/testPkgdown/vignettes/test.Rmd
/usr/lib64/R/library/devtools/tests/testthat/testTest/DESCRIPTION
/usr/lib64/R/library/devtools/tests/testthat/testTest/NAMESPACE
/usr/lib64/R/library/devtools/tests/testthat/testTest/R/dummy.R
/usr/lib64/R/library/devtools/tests/testthat/testTest/tests/testthat.R
/usr/lib64/R/library/devtools/tests/testthat/testTest/tests/testthat/test-dummy.R
/usr/lib64/R/library/devtools/tests/testthat/testTest/tests/testthat/test-envvar.R
/usr/lib64/R/library/devtools/tests/testthat/testTestWithDepends/DESCRIPTION
/usr/lib64/R/library/devtools/tests/testthat/testTestWithDepends/NAMESPACE
/usr/lib64/R/library/devtools/tests/testthat/testTestWithDepends/tests/testthat.R
/usr/lib64/R/library/devtools/tests/testthat/testTestWithDepends/tests/testthat/test-dummy.R
/usr/lib64/R/library/devtools/tests/testthat/testTestWithFailure/DESCRIPTION
/usr/lib64/R/library/devtools/tests/testthat/testTestWithFailure/NAMESPACE
/usr/lib64/R/library/devtools/tests/testthat/testTestWithFailure/R/dummy.R
/usr/lib64/R/library/devtools/tests/testthat/testTestWithFailure/tests/testthat.R
/usr/lib64/R/library/devtools/tests/testthat/testTestWithFailure/tests/testthat/test-fail.R
/usr/lib64/R/library/devtools/tests/testthat/testTestWithFailure/tests/testthat/test-warn.R
/usr/lib64/R/library/devtools/tests/testthat/testUseData/DESCRIPTION
/usr/lib64/R/library/devtools/tests/testthat/testUseData/NAMESPACE
/usr/lib64/R/library/devtools/tests/testthat/testUseData/R/a.R
/usr/lib64/R/library/devtools/tests/testthat/testVignetteExtras/DESCRIPTION
/usr/lib64/R/library/devtools/tests/testthat/testVignetteExtras/NAMESPACE
/usr/lib64/R/library/devtools/tests/testthat/testVignetteExtras/vignettes/a.R
/usr/lib64/R/library/devtools/tests/testthat/testVignetteExtras/vignettes/new.Rnw
/usr/lib64/R/library/devtools/tests/testthat/testVignettes/DESCRIPTION
/usr/lib64/R/library/devtools/tests/testthat/testVignettes/NAMESPACE
/usr/lib64/R/library/devtools/tests/testthat/testVignettes/vignettes/new.Rnw
/usr/lib64/R/library/devtools/tests/testthat/testVignettesBuilt/DESCRIPTION
/usr/lib64/R/library/devtools/tests/testthat/testVignettesBuilt/NAMESPACE
/usr/lib64/R/library/devtools/tests/testthat/testVignettesBuilt/R/code.R
/usr/lib64/R/library/devtools/tests/testthat/testVignettesBuilt/vignettes/new.Rnw
