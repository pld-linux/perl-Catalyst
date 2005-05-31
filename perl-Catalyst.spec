#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	Catalyst - The Elegant MVC Web Application Framework
#Summary(pl):	
Name:		perl-Catalyst
Version:	5.22
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/M/MR/MRAMBERG/Catalyst-%{version}.tar.gz
# Source0-md5:	49a487ab1a4711980c50d98f0a0603c3
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Class-Accessor
BuildRequires:	perl-Class-Data-Inheritable
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-libwww
BuildRequires:	perl-Module-Pluggable-Fast >= 0.15
BuildRequires:	perl-Path-Class
BuildRequires:	perl-Template-Toolkit
BuildRequires:	perl-Text-ASCIITable
BuildRequires:	perl-Tree-Simple
BuildRequires:	perl-Tree-Simple-VisitorFactory
BuildRequires:	perl-UNIVERSAL-exports
BuildRequires:	perl-URI
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Catalyst is an elegant web application framework, extremely flexible
yet extremely simple. It's similar to Ruby on Rails, Spring (Java) and
Maypole, upon which it was originally based.

Catalyst follows the Model-View-Controller (MVC) design pattern,
allowing you to easily separate concerns, like content, presentation,
and flow control, into separate modules. This separation allows you to
modify code that handles one concern without affecting code that
handles the others. Catalyst promotes the re-use of existing Perl
modules that already handle common web application concerns well.

%package Engine-Apache
Summary:	Engine for Apache
Group:		Development/Languages/Perl

%description Engine-Apache
This is the Catalyst engine for mod_perl.

%package Engine-FastCGI
Summary:	Engine for Fast CGI
Group:		Development/Languages/Perl

%description Engine-FastCGI
This is the Catalyst engine for FastCGI.

%package Engine-SpeedyCGI
Summary:	Engine for Speedy CGI
Group:		Development/Languages/Perl

%description Engine-SpeedyCGI
This is the Catalyst engine for SpeedyCGI.


%prep
%setup -q -n Catalyst-%{version}

%build
%{__perl} Build.PL \
        destdir=$RPM_BUILD_ROOT \
        installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Catalyst.pm
%{perl_vendorlib}/Catalyst/*.pm
%{perl_vendorlib}/Catalyst/Engine
%exclude %{perl_vendorlib}/Catalyst/Engine/Apache*
%exclude %{perl_vendorlib}/Catalyst/Engine/FastCGI*
%exclude %{perl_vendorlib}/Catalyst/Engine/SpeedyCGI*

%{perl_vendorlib}/Catalyst/Request
%attr(755,root,root) %{_bindir}/catalyst.pl
%exclude %{_mandir}/man3/*Apache*
%exclude %{_mandir}/man3/*FastCGI*
%exclude %{_mandir}/man3/*SpeedyCGI*
%{_mandir}/man3/*
%{_mandir}/man1/*

%files Engine-Apache
%{perl_vendorlib}/Catalyst/Engine/Apache*
%{_mandir}/man3/Catalyst::Engine::Apache*

%files Engine-FastCGI
%{perl_vendorlib}/Catalyst/Engine/FastCGI*
%{_mandir}/man3/Catalyst::Engine::FastCGI*

%files Engine-SpeedyCGI
%{perl_vendorlib}/Catalyst/Engine/SpeedyCGI*
%{_mandir}/man3/Catalyst::Engine::SpeedyCGI*
