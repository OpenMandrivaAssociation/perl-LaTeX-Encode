%define upstream_name    LaTeX-Encode
%define upstream_version 0.03

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Encode LaTeX special chars for typesetting
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/LaTeX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

%description
This module provides a function to encode text that is to be formatted with
LaTeX. It encodes characters that are special to LaTeX or that are
represented in LaTeX by LaTeX commands.

The special characters are: '\' (command character), '{' (open group), '}'
(end group), '&' (table column separator), '#' (parameter specifier), '%'
(comment character), '_' (subscript), '^' (superscript), '~' (non-breakable
space), '$' (mathematics mode).

Note that some of the LaTeX commands for characters are defined in the
LaTeX 'textcomp' package. If your text includes such characters, you will
need to include the following lines in the preamble to your LaTeX document.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README README
%{_mandir}/man3/*
%perl_vendorlib/*

