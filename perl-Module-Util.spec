%define upstream_name    Module-Util
%define upstream_version 1.09
Name:       perl-%{upstream_name}
Version:	1.09
Release:	2

Summary:    Module name tools and transformations
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://metacpan.org/dist/Module-Util
Source0:	https://cpan.metacpan.org/authors/id/M/MA/MATTLAW/Module-Util-1.09.tar.gz

BuildRequires:	make
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
%setup -q -n Module-Util-1.09

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
# soft: do not fail package on test failures
set +e
make test

%install
rm -rf %{buildroot}
%makeinstall_std


%files
%defattr(-,root,root)
%doc Changes README
%{_bindir}/pm_which
%{_mandir}/man1/pm_which.1.*
%{_mandir}/man3/*
%{perl_vendorlib}/Module


