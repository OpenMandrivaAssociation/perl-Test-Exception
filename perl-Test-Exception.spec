%define upstream_name    Test-Exception
%define upstream_version 0.31

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Test exception based code
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(JSON::PP)
BuildRequires:	perl(Test::Builder) >= 0.13
BuildRequires:	perl(Test::Harness) >= 2.03
BuildRequires:	perl(Test::More) >= 0.44
BuildRequires:	perl(Sub::Uplevel) >= 0.06
BuildRequires:	perl(Test::Builder::Tester) >= 1.01
BuildArch:		noarch

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
%makeinstall_std
rm -f %{buildroot}%{perl_archlib}/perllocal.pod

%files
%doc Changes README
%{perl_vendorlib}/Test
%{_mandir}/man3/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.310.0-4mdv2012.0
+ Revision: 765678
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.310.0-3
+ Revision: 764203
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.310.0-2
+ Revision: 667325
- mass rebuild

* Sun Nov 07 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.310.0-1mdv2011.0
+ Revision: 594368
- update to new version 0.31

* Tue Jan 12 2010 Jérôme Quelin <jquelin@mandriva.org> 0.290.0-1mdv2011.0
+ Revision: 490196
- update to 0.29

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.270.0-1mdv2010.0
+ Revision: 405550
- rebuild using %%perl_convert_version

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.27-2mdv2009.0
+ Revision: 224135
- rebuild

* Sun Feb 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.27-1mdv2008.1
+ Revision: 169971
- update to new version 0.27

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Dec 11 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.26-1mdv2008.1
+ Revision: 117504
- update to new version 0.26


* Tue Mar 06 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.25-1mdv2007.0
+ Revision: 133688
- new version

* Tue Nov 14 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.24-1mdv2007.1
+ Revision: 84003
- new version
- Import perl-Test-Exception

* Wed Sep 06 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.22-1mdv2007.0
- New version 0.22

* Sun Jun 18 2006 Scott Karns <scottk@mandriva.org> 0.21-4mdv2007.0
- Updated spec to comply with Mandriva perl packaging policies
- Updated BuildRequires per Makefile.PL

* Tue Apr 04 2006 Buchan Milne <bgmilne@mandriva.org> 0.21-3mdk
- Rebuild
- use mkrel

* Wed Aug 31 2005 Gwenole Beauchesne <gbeauchesne@mandriva.com> 0.21-2mdk
- buildrequires: perl-Test-Builder-Tester

* Tue Jun 07 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.21-1mdk
- New release 0.21
- spec cleanup
- buildrequires

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.20-2mdk
- fix buildrequires in a backward compatible way

* Tue Aug 31 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.20-1mdk
- 0.20.

* Tue Aug 24 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.19-1mdk
- 0.19.

* Wed Aug 11 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.17-1mdk
- 0.17.

* Sat Jul 24 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.15-6mdk 
- rpmbuildupdate aware

