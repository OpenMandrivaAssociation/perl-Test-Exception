%define module  Test-Exception
%define name	perl-%{module}
%define	modprefix Test
%define version 0.27
%define release %mkrel 2

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Summary: 	Test exception based code
License: 	GPL or Artistic
Group: 		Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Test/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(Test::Builder) >= 0.13
BuildRequires:	perl(Test::Harness) >= 2.03
BuildRequires:	perl(Test::More) >= 0.44
BuildRequires:	perl(Sub::Uplevel) >= 0.06
BuildRequires:	perl(Test::Builder::Tester) >= 1.01
BuildArch: 	    noarch
BuildRoot: 	    %{_tmppath}/%{name}-%{version}

%description 
This module provides a few convenience methods for testing
exception-based code. It is built with Test::Builder and
plays happily with Test::Simple, Test::More and friends.

If you are not familiar with Test::Simple or Test::More
now would be the time to go take a look.

%prep
%setup -q -n %{module}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}%{perl_archlib}/perllocal.pod

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/%{modprefix}
%{_mandir}/man3/*


