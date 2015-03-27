%define modname	Test-Exception
%define modver 0.38

Summary:	Test exception based code
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Test/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl-JSON-PP
BuildRequires:	perl(Test::Builder) >= 0.13
BuildRequires:	perl(Test::Harness) >= 2.03
BuildRequires:	perl(Test::More) >= 0.44
BuildRequires:	perl(Sub::Uplevel) >= 0.06
BuildRequires:	perl(Test::Builder::Tester) >= 1.01

%description 
This module provides a few convenience methods for testing
exception-based code. It is built with Test::Builder and
plays happily with Test::Simple, Test::More and friends.

If you are not familiar with Test::Simple or Test::More
now would be the time to go take a look.

%prep
%setup -qn %{modname}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std
rm -f %{buildroot}%{perl_archlib}/perllocal.pod

%files
%doc Changes README
%{perl_vendorlib}/Test
%{_mandir}/man3/*
