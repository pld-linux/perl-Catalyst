#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
Summary:	Catalyst - The Elegant MVC Web Application Framework
Summary(pl.UTF-8):	Catalyst - elegancki szkielet MVC dla aplikacji WWW
Name:		perl-Catalyst
Version:	5.90132
Release:	1
Source0:	https://www.cpan.org/authors/id/J/JJ/JJNAPIORK/Catalyst-Runtime-%{version}.tar.gz
# Source0-md5:	ce3b03cc998fcef45d5a0bd49d923caf
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
URL:		http://www.catalystframework.org/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(CGI::Simple::Cookie) >= 1.109
BuildRequires:	perl-CGI-Struct
BuildRequires:	perl-Class-C3-Adopt-NEXT >= 0.07
BuildRequires:	perl-Class-Load >= 0.12
BuildRequires:	perl-Data-Dump
BuildRequires:	perl-Data-OptList
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-HTTP-Body >= 1.22
BuildRequires:	perl-HTTP-Headers-ActionPack
BuildRequires:	perl(HTTP::Headers) >= 1.64
BuildRequires:	perl(HTTP::Request) >= 5.814
BuildRequires:	perl(HTTP::Response) >= 5.813
BuildRequires:	perl-Hash-MultiValue
BuildRequires:	perl-JSON-MaybeXS >= 1.000000
BuildRequires:	perl-MRO-Compat
BuildRequires:	perl-Module-Pluggable >= 4.7
BuildRequires:	perl-Moose >= 2.1400
BuildRequires:	perl-MooseX-Emulate-Class-Accessor-Fast >= 0.00903
BuildRequires:	perl-MooseX-Getopt >= 0.48
BuildRequires:	perl-MooseX-MethodAttributes >= 0.24
BuildRequires:	perl-Path-Class >= 0.09
BuildRequires:	perl-PerlIO-utf8_strict
BuildRequires:	perl-Plack >= 0.9991
BuildRequires:	perl-Plack-Middleware-FixMissingBodyInRedirect >= 0.09
BuildRequires:	perl-Plack-Middleware-MethodOverride >= 0.12
BuildRequires:	perl-Plack-Middleware-RemoveRedundantBody >= 0.03
BuildRequires:	perl-Plack-Middleware-ReverseProxy >= 0.04
BuildRequires:	perl-Plack-Test-ExternalServer
BuildRequires:	perl-Safe-Isa
BuildRequires:	perl-Stream-Buffered
BuildRequires:	perl-String-RewritePrefix >= 0.004
BuildRequires:	perl-Sub-Exporter
BuildRequires:	perl-Task-Weaken
BuildRequires:	perl-Test-Fatal
BuildRequires:	perl-Text-SimpleTable >= 0.03
BuildRequires:	perl-Tree-Simple >= 1.15
BuildRequires:	perl-Tree-Simple-VisitorFactory
BuildRequires:	perl-Try-Tiny >= 0.17
BuildRequires:	perl-Type-Tiny
BuildRequires:	perl-URI >= 1.65
BuildRequires:	perl-libwww >= 5.837
BuildRequires:	perl-namespace-clean >= 0.23
%endif
Requires:	perl(Term::Size::Any)
Requires:	perl-CGI-Struct
Requires:	perl-JSON-MaybeXS >= 1.000000
Requires:	perl-Type-Tiny
Requires:	perl-URI >= 1.65
Requires:	perl-libwww >= 5.837
Obsoletes:	perl-Catalyst-Engine-CGI-APR
Obsoletes:	perl-Catalyst-Engine-FastCGI
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

%prep
%setup -q -n Catalyst-Runtime-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
#: \	--skipdeps
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{perl_vendorlib}/Catalyst/{View/REST,Model,Plugin/HTML,Action}
install -d $RPM_BUILD_ROOT%{perl_vendorlib}/Catalyst/Helper/{View,Model}
install -d $RPM_BUILD_ROOT%{perl_vendorlib}/CatalystX

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Catalyst.pm
%dir %{perl_vendorlib}/Catalyst
%dir %{perl_vendorlib}/CatalystX
%{perl_vendorlib}/Catalyst/*.pm
%{perl_vendorlib}/Catalyst/*.pod
%{perl_vendorlib}/Catalyst/ActionRole
%{perl_vendorlib}/Catalyst/Component
%{perl_vendorlib}/Catalyst/DispatchType
%{perl_vendorlib}/Catalyst/Engine
%{perl_vendorlib}/Catalyst/Exception
%{perl_vendorlib}/Catalyst/Helper
%{perl_vendorlib}/Catalyst/Middleware
%{perl_vendorlib}/Catalyst/Model
%dir %{perl_vendorlib}/Catalyst/View
%dir %{perl_vendorlib}/Catalyst/View/REST
%dir %{perl_vendorlib}/Catalyst/Action
%{perl_vendorlib}/Catalyst/Plugin
%{perl_vendorlib}/Catalyst/Request
%{perl_vendorlib}/Catalyst/Response
%{perl_vendorlib}/Catalyst/Script
%attr(755,root,root) %{_bindir}/catalyst.pl
%{_mandir}/man3/*
%{_mandir}/man1/*
