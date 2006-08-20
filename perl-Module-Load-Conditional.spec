#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Module
%define		pnam	Load-Conditional
Summary:	Module::Load::Conditional - Looking up module information / loading at runtime
Summary(pl):	Module::Load::Conditional - wyszukiwanie informacji o modu³ach i wczytywanie
Name:		perl-Module-Load-Conditional
Version:	0.08
Release:	0.1
# "same as perl"
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9e2a706b6511651ca4eb6de0c4c89a12
URL:		http://search.cpan.org/dist/Module-Load-Conditional/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
BuildRequires:	perl-Locale-Maketext-Simple
BuildRequires:	perl-Module-Load
BuildRequires:	perl-Params-Check
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl module Module::Load::Conditional provides simple ways to query
and possibly load any of the modules you have installed on your system
during runtime.

It is able to load multiple modules at once or none at all if one of
them was not able to load. It also takes care of any error checking
and so forth.

%description -l pl
Modu³ Perla Module::Load::Conditional udostêpnia prosty sposób na
odpytanie i ewentualne wczytanie w czasie dzia³ania programu dowolnego
z modu³ów zainstalowanych w systemie.

Pozwala wczytaæ wiele modu³ów naraz lub nie wczytaæ ¿adnego z nich,
je¶li jednego z nich nie da siê za³adowaæ. Dba tak¿e o sprawdzanie
b³êdów itp.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{perl_vendorlib}/Module/Load
%{perl_vendorlib}/Module/Load/Conditional.pm
%{_mandir}/man3/*
