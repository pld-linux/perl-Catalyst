#
# Conditional build:
%bcond_with	tests		# perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	Catalyst - The Elegant MVC Web Application Framework
Summary(pl.UTF-8):	Catalyst - elegancki szkielet MVC dla aplikacji WWW
Name:		perl-Catalyst
Version:	5.80011
Release:	4
Source0:	http://www.cpan.org/modules/by-module/Catalyst/Catalyst-Runtime-%{version}.tar.gz
# Source0-md5:	96f09897079c6a13e1c0375b3a94ad4f
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
URL:		http://www.catalystframework.org/
BuildRequires:	perl(Class::C3::Adopt::NEXT) >= 0.07
BuildRequires:	perl(HTTP::Request::AsCGI) >= 0.8
BuildRequires:	perl(Module::Pluggable) >= 3.9
BuildRequires:	perl(MooseX::Emulate::Class::Accessor::Fast) >= 0.00801
BuildRequires:	perl(MooseX::MethodAttributes::Inheritable) >= 0.15
BuildRequires:	perl(String::RewritePrefix) >= 0.004
BuildRequires:	perl(namespace::autoclean)
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-B-Hooks-EndOfScope >= 0.08
BuildRequires:	perl-CGI-Simple
BuildRequires:	perl-Class-Data-Inheritable
BuildRequires:	perl-Class-MOP >= 0.83
BuildRequires:	perl-Data-Dump
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.42
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-HTTP-Body >= 1.04
BuildRequires:	perl-List-MoreUtils
BuildRequires:	perl-MRO-Compat
BuildRequires:	perl-Moose >= 0.78
BuildRequires:	perl-Path-Class >= 0.09
BuildRequires:	perl-Sub-Exporter
BuildRequires:	perl-Task-Weaken
BuildRequires:	perl-Test-Exception
BuildRequires:	perl-Text-SimpleTable >= 0.03
BuildRequires:	perl-Tree-Simple >= 1.15
BuildRequires:	perl-Tree-Simple-VisitorFactory
BuildRequires:	perl-URI >= 1.35
BuildRequires:	perl-libwww
BuildRequires:	perl-namespace-clean
%endif
Requires:	perl(Term::Size::Any)
Requires:	perl-HTTP-Request-AsCGI
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
%doc Changes README TODO
%{perl_vendorlib}/Catalyst.pm
%dir %{perl_vendorlib}/Catalyst
%dir %{perl_vendorlib}/CatalystX
%{perl_vendorlib}/Catalyst/*.pm
%{perl_vendorlib}/Catalyst/Component
%{perl_vendorlib}/Catalyst/DispatchType
%{perl_vendorlib}/Catalyst/Engine
%{perl_vendorlib}/Catalyst/Exception
%{perl_vendorlib}/Catalyst/Helper
%{perl_vendorlib}/Catalyst/Model
%dir %{perl_vendorlib}/Catalyst/View
%dir %{perl_vendorlib}/Catalyst/View/REST
%dir %{perl_vendorlib}/Catalyst/Model
%dir %{perl_vendorlib}/Catalyst/Action
%{perl_vendorlib}/Catalyst/Plugin
%{perl_vendorlib}/Catalyst/Component/ApplicationAttribute.pm
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
