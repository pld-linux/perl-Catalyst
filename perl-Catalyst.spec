#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	Catalyst - The Elegant MVC Web Application Framework
Summary(pl.UTF-8):	Catalyst - elegancki szkielet MVC dla aplikacji WWW
Name:		perl-Catalyst
Version:	5.7010
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
URL:		http://www.catalystframework.org/
Source0:	http://www.cpan.org/modules/by-module/Catalyst/Catalyst-Runtime-%{version}.tar.gz
# Source0-md5:	3a88955a049b60bfa5a95ccee77f6fe2
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-CGI-Simple
BuildRequires:	perl-Class-Accessor
BuildRequires:	perl-Class-Data-Inheritable
BuildRequires:	perl-Data-Dump
BuildRequires:	perl-ExtUtils-AutoInstall
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-HTTP-Body >= 0.9
BuildRequires:	perl-HTTP-Request-AsCGI >= 0.5
BuildRequires:	perl-libwww
BuildRequires:	perl-Module-Pluggable >= 3.01
BuildRequires:	perl-Path-Class >= 0.09
BuildRequires:	perl-Text-SimpleTable >= 0.03
BuildRequires:	perl-Tree-Simple >= 1.15
BuildRequires:	perl-Tree-Simple-VisitorFactory
BuildRequires:	perl-UNIVERSAL-require >= 0.10
BuildRequires:	perl-URI >= 1.35
BuildRequires:	perl-YAML >= 0.55
%endif
Obsoletes:	perl-Catalyst-Engine-CGI-APR
Obsoletes:	perl-Catalyst-Engine-FastCGI-APR
Obsoletes:	perl-Catalyst-Engine-SpeedyCGI
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(Module::Build)' 'perl(Catalyst::.*)'

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

%description -l pl.UTF-8
Catalyst to elegancki szkielet dla aplikacji WWW, ekstremalnie
elastyczny, ale i ekstremalnie prosty. Jest podobny do środowisk Ruby
on Rails, Spring (Java) czy Maypole, na którym był oryginalnie oparty.

Catalyst jest zgodny ze wzorem projektowym MVC (Model-View-Controller
- model-widok-kontroler), pozwalając na łatwe rozdzielenie rzeczy
takich jak treść, prezentacja i kontrola ruchu na oddzielne moduły.
Ten podział pozwala na modyfikowanie kodu obsługującego jedną rzecz
bez wpływania na kod obsługujący co innego. Catalyst skutecznie
poszerza wielokrotną używalność istniejących modułów perla
obsługujących różne aspekty aplikacji WWW.


%package Engine-FastCGI
Summary:	Engine for FastCGI
Summary(pl.UTF-8):	Silnik dla FastCGI
Group:		Development/Languages/Perl

%description Engine-FastCGI
This is the Catalyst engine for FastCGI.

%description Engine-FastCGI -l pl.UTF-8
Silnik Catalyst dla FastCGI.

%prep
%setup -q -n Catalyst-Runtime-%{version}

%build
%{__perl} Makefile.PL \
        INSTALLDIRS=vendor \
	--skipdeps
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT 

install -d $RPM_BUILD_ROOT%{perl_vendorlib}/Catalyst/{View,Model,Plugin,Action}
install -d $RPM_BUILD_ROOT%{perl_vendorlib}/Catalyst/Helper/{View,Model}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Catalyst.pm
%dir %{perl_vendorlib}/Catalyst
%{perl_vendorlib}/Catalyst/*.pm
%{perl_vendorlib}/Catalyst/DispatchType
%{perl_vendorlib}/Catalyst/Engine
%{perl_vendorlib}/Catalyst/Helper
%{perl_vendorlib}/Catalyst/Model
%dir %{perl_vendorlib}/Catalyst/View
%dir %{perl_vendorlib}/Catalyst/Model
%dir %{perl_vendorlib}/Catalyst/Action
%{perl_vendorlib}/Catalyst/Plugin
%exclude %{perl_vendorlib}/Catalyst/Engine/FastCGI*

%{perl_vendorlib}/Catalyst/Request
%attr(755,root,root) %{_bindir}/catalyst.pl
%exclude %{_mandir}/man3/*FastCGI*
%{_mandir}/man3/*
%{_mandir}/man1/*


%files Engine-FastCGI
%defattr(644,root,root,755)
%{perl_vendorlib}/Catalyst/Engine/FastCGI*
%{_mandir}/man3/Catalyst::Engine::FastCGI*
