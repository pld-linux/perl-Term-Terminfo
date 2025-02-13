#
# Conditional build:
%bcond_with	tests
#
%define		pdir	Term
%define		pnam	Terminfo
Summary:	Term::Terminfo - Perl module for access the terminfo database
Summary(pl.UTF-8):	Term::Terminfo - moduł Perla do dostępu do bazy terminfo
Name:		perl-Term-Terminfo
Version:	0.09
Release:	1
License:	BSD-like
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Term/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1774d730bc18f0e9d99ad6aaff4d393a
URL:		https://metacpan.org/dist/Term-Terminfo
BuildRequires:	perl-ExtUtils-MakeMaker >= 3.5
BuildRequires:	perl-Module-Build-Using-PkgConfig
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
#BuildRequires:	rpmbuild(macros) >= 1.745
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Access the terminfo database

%prep
%setup -q -n Term-Terminfo-%{version}

%build
%{__perl} Build.PL \
	--installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install \
	--destdir=$RPM_BUILD_ROOT \
	--create_packlist=0

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorarch}/Term/Terminfo.pm
%dir %{perl_vendorarch}/auto/Term/Terminfo
# empty autosplit.ix
#%%{perl_vendorarch}/auto/Term/Terminfo/autosplit.ix
%attr(755,root,root) %{perl_vendorarch}/auto/Term/Terminfo/Terminfo.so
%{_mandir}/man3/Term::Terminfo.3pm*
