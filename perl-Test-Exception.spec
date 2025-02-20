%define modname	Test-Exception

Summary:	Test exception based code
Name:		perl-%{modname}
Version:	0.43
Release:	10
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/pod/Test::Exception
Source0:	http://www.cpan.org/modules/by-module/Test/%{modname}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl-JSON-PP
BuildRequires:	perl(Test::Builder) >= 0.13
BuildRequires:	perl(Test::Harness) >= 2.03
BuildRequires:	perl(Test::More) >= 0.44
BuildRequires:	perl(Sub::Uplevel)
BuildRequires:	perl(Test::Builder::Tester) >= 1.01

%description 
This module provides a few convenience methods for testing
exception-based code. It is built with Test::Builder and
plays happily with Test::Simple, Test::More and friends.

If you are not familiar with Test::Simple or Test::More
now would be the time to go take a look.

%prep
%setup -qn %{modname}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std
rm -f %{buildroot}%{perl_archlib}/perllocal.pod

%files
%doc Changes
%{perl_vendorlib}/Test
%{_mandir}/man3/*
