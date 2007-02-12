#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Module
%define		pnam	Load-Conditional
Summary:	Module::Load::Conditional - Looking up module information / loading at runtime
Summary(pl.UTF-8):   Module::Load::Conditional - wyszukiwanie informacji o modułach i wczytywanie
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

%description -l pl.UTF-8
Moduł Perla Module::Load::Conditional udostępnia prosty sposób na
odpytanie i ewentualne wczytanie w czasie działania programu dowolnego
z modułów zainstalowanych w systemie.

Pozwala wczytać wiele modułów naraz lub nie wczytać żadnego z nich,
jeśli jednego z nich nie da się załadować. Dba także o sprawdzanie
błędów itp.

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
