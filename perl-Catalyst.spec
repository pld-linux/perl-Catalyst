#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	Catalyst - The Elegant MVC Web Application Framework
Summary(pl):	Catalyst - elegancki szkielet MVC dla aplikacji WWW
Name:		perl-Catalyst
Version:	5.23
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/M/MR/MRAMBERG/Catalyst-%{version}.tar.gz
# Source0-md5:	1c7884afec0b256ecb05f5bd5064f46a
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Class-Accessor
BuildRequires:	perl-Class-Data-Inheritable
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-Module-Pluggable-Fast >= 0.15
BuildRequires:	perl-Path-Class
BuildRequires:	perl-Template-Toolkit
BuildRequires:	perl-Test-Pod >= 1.14
BuildRequires:	perl-Test-Pod-Coverage >= 1.04
BuildRequires:	perl-Text-ASCIITable
BuildRequires:	perl-Tree-Simple
BuildRequires:	perl-Tree-Simple-VisitorFactory
BuildRequires:	perl-UNIVERSAL-exports
BuildRequires:	perl-URI
BuildRequires:	perl-libwww
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(Module::Build)'

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

%description -l pl
Catalyst to elegancki szkielet dla aplikacji WWW, ekstremalnie
elastyczny, ale i ekstremalnie prosty. Jest podobny do ¶rodowisk Ruby
on Rails, Spring (Java) czy Maypole, na którym by³ oryginalnie oparty.

Catalyst jest zgodny ze wzorem projektowym MVC (Model-View-Controller
- model-widok-kontroler), pozwalaj±c na ³atwe rozdzielenie rzeczy
takich jak tre¶æ, prezentacja i kontrola ruchu na oddzielne modu³y.
Ten podzia³ pozwala na modyfikowanie kodu obs³uguj±cego jedn± rzecz
bez wp³ywania na kod obs³uguj±cy co innego. Catalyst skutecznie
poszerza wielokrotn± u¿ywalno¶æ istniej±cych modu³ów perla
obs³uguj±cych ró¿ne aspekty aplikacji WWW.

%package Engine-Apache
Summary:	Engine for Apache
Summary(pl):	Silnik dla Apache'a
Group:		Development/Languages/Perl

%description Engine-Apache
This is the Catalyst engine for mod_perl.

%description Engine-Apache -l pl
Silnik Catalyst dla Apache'a.

%package Engine-CGI-APR
Summary:	Catalyst::Engine::CGI::APR - The CGI APR Engine
Group:		Development/Languages/Perl

%description Engine-CGI-APR
This is the Catalyst engine that uses Apache Portable Runtime for
parsing CGI parameters.

%package Engine-FastCGI-APR
Summary:	Catalyst::Engine::FastCGI::APR - The FastCGI APR Engine
Group:		Development/Languages/Perl

%description Engine-FastCGI-APR
This is the Catalyst FastCGI engine that uses Apache Portable Runtime for
parsing CGI parameters.


%package Engine-FastCGI
Summary:	Engine for FastCGI
Summary(pl):	Silnik dla FastCGI
Group:		Development/Languages/Perl

%description Engine-FastCGI
This is the Catalyst engine for FastCGI.

%description Engine-FastCGI -l pl
Silnik Catalyst dla FastCGI.

%package Engine-SpeedyCGI
Summary:	Engine for SpeedyCGI
Summary(pl):	Silnik dla SpeedyCGI
Group:		Development/Languages/Perl

%description Engine-SpeedyCGI
This is the Catalyst engine for SpeedyCGI.

%description Engine-SpeedyCGI -l pl
Silnik Catalyst dla SpeedyCGI.

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

install -d $RPM_BUILD_ROOT%{perl_vendorlib}/Catalyst/{Helper,Plugin}
install -d $RPM_BUILD_ROOT%{perl_vendorlib}/Catalyst/Helper/{Model,View}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Catalyst.pm
%dir %{perl_vendorlib}/Catalyst
%{perl_vendorlib}/Catalyst/*.pm
%{perl_vendorlib}/Catalyst/Engine
%{perl_vendorlib}/Catalyst/Helper
%dir %{perl_vendorlib}/Catalyst/Plugin
%exclude %{perl_vendorlib}/Catalyst/Engine/*/APR.pm
%exclude %{perl_vendorlib}/Catalyst/Engine/Apache*
%exclude %{perl_vendorlib}/Catalyst/Engine/FastCGI*
%exclude %{perl_vendorlib}/Catalyst/Engine/SpeedyCGI*

%{perl_vendorlib}/Catalyst/Request
%attr(755,root,root) %{_bindir}/catalyst.pl
%exclude %{_mandir}/man3/*Apache*
%exclude %{_mandir}/man3/*FastCGI*
%exclude %{_mandir}/man3/*SpeedyCGI*
%exclude %{_mandir}/man3/*APR*
%{_mandir}/man3/*
%{_mandir}/man1/*

%files Engine-Apache
%defattr(644,root,root,755)
%{perl_vendorlib}/Catalyst/Engine/Apache*
%{_mandir}/man3/Catalyst::Engine::Apache*

%files Engine-CGI-APR
%defattr(644,root,root,755)
%{perl_vendorlib}/Catalyst/Engine/CGI/APR.pm
%{_mandir}/man3/Catalyst::Engine::CGI::APR*

%files Engine-FastCGI
%defattr(644,root,root,755)
%{perl_vendorlib}/Catalyst/Engine/FastCGI*
%{_mandir}/man3/Catalyst::Engine::FastCGI*

%files Engine-FastCGI-APR
%defattr(644,root,root,755)
%{perl_vendorlib}/Catalyst/Engine/FastCGI/APR.pm
%{_mandir}/man3/Catalyst::Engine::FastCGI::APR*

%files Engine-SpeedyCGI
%defattr(644,root,root,755)
%{perl_vendorlib}/Catalyst/Engine/SpeedyCGI*
%{_mandir}/man3/Catalyst::Engine::SpeedyCGI*
