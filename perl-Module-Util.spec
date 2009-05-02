%define module   Module-Util
%define version    1.07
%define release    %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Module name tools and transformations
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Module/%{module}-%{version}.tar.gz
BuildRequires: perl(Test::More)
BuildRequires: perl(Module::Build::Compat)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
This module provides a few useful functions for manipulating module names.
Its main aim is to centralise some of the functions commonly used by
modules that manipulate other modules in some way, like converting module
names to relative paths.





%prep
%setup -q -n %{module}-%{version} 

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

