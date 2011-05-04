%define upstream_name    Test-Exception
%define upstream_version 0.31

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary: 	Test exception based code
License: 	GPL+ or Artistic
Group: 		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(Test::Builder) >= 0.13
BuildRequires:	perl(Test::Harness) >= 2.03
BuildRequires:	perl(Test::More) >= 0.44
BuildRequires:	perl(Sub::Uplevel) >= 0.06
BuildRequires:	perl(Test::Builder::Tester) >= 1.01
BuildArch: 	    noarch
BuildRoot: 	    %{_tmppath}/%{name}-%{version}-%{release}

%description 
This module provides a few convenience methods for testing
exception-based code. It is built with Test::Builder and
plays happily with Test::Simple, Test::More and friends.

If you are not familiar with Test::Simple or Test::More
now would be the time to go take a look.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}%{perl_archlib}/perllocal.pod

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Test
%{_mandir}/man3/*
