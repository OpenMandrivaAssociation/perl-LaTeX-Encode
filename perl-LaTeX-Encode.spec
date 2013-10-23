%define upstream_name    LaTeX-Encode
%define upstream_version 0.08

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Encode LaTeX special chars for typesetting
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/LaTeX/LaTeX-Encode-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires: perl(Readonly)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

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
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README README
%{_mandir}/man3/*
%{perl_vendorlib}/*
%{_bindir}/latex-encode
%{_mandir}/man1/latex-encode.1.xz

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.30.0-2mdv2011.0
+ Revision: 655039
- rebuild for updated spec-helper

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.30.0-1mdv2011.0
+ Revision: 401641
- rebuild using %%perl_convert_version
- fixed license field

* Fri May 15 2009 Jérôme Quelin <jquelin@mandriva.org> 0.03-2mdv2010.0
+ Revision: 375943
- rebuild

* Sat Apr 11 2009 Olivier Thauvin <nanardon@mandriva.org> 0.03-1mdv2009.1
+ Revision: 366281
- import perl-LaTeX-Encode


* Sat Apr 11 2009 cpan2dist 0.03-1mdv
- initial mdv release, generated with cpan2dist


