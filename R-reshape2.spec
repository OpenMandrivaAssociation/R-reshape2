%global packname reshape2
%global rlibdir %{_libdir}/R/library

Name: R-%{packname}
Version: 1.2.2
Release: 1
Summary: Flexibly reshape data: a reboot of the reshape package
Group: Sciences/Mathematics
License: MIT
URL: https://cran.r-project.org/web/packages/%{packname}/index.html
Source0: http://cran.r-project.org/src/contrib/%{packname}_1.2.2.tar.gz
BuildArch: noarch
Requires: R-core R-plyr R-stringr R-lattice
BuildRequires: R-devel Rmath-devel R-plyr R-stringr R-lattice texlive-collection-latex

%description
Reshape lets you flexibly restructure and aggregate data
using just two functions: melt and cast.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/tests
