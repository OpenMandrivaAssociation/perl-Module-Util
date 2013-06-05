%define upstream_name    Module-Util
%define upstream_version 1.07

Name:       perl-%{upstream_name}
Version:    %perl_convert_version 1.09
Release:    1

Summary:    Module name tools and transformations
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Module/Module-Util-1.09.tar.gz

BuildRequires: perl(Test::More)
BuildRequires: perl(Module::Build::Compat)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

%description
This module provides a few useful functions for manipulating module names.
Its main aim is to centralise some of the functions commonly used by
modules that manipulate other modules in some way, like converting module
names to relative paths.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{_bindir}/pm_which
%{_mandir}/man1/pm_which.1.*
%{_mandir}/man3/*
%{perl_vendorlib}/Module


%changelog
* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.70.0-1mdv2010.0
+ Revision: 404020
- rebuild using %%perl_convert_version

* Sat May 02 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.07-1mdv2010.0
+ Revision: 370493
- update to new version 1.07

* Sun Nov 09 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.05-1mdv2009.1
+ Revision: 301378
- update to new version 1.05

* Mon Jun 30 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.04-1mdv2009.0
+ Revision: 230278
- update to new version 1.04

* Sat May 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.03-1mdv2009.0
+ Revision: 213759
- import perl-Module-Util


* Sat May 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.03-1mdv2009.0
- first mdv release

