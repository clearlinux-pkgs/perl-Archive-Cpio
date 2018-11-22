#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Archive-Cpio
Version  : 0.10
Release  : 4
URL      : https://cpan.metacpan.org/authors/id/P/PI/PIXEL/Archive-Cpio-0.10.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/P/PI/PIXEL/Archive-Cpio-0.10.tar.gz
Source1  : http://http.debian.net/debian/pool/main/liba/libarchive-cpio-perl/libarchive-cpio-perl_0.10-1.debian.tar.xz
Summary  : 'module for manipulations of cpio archives'
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-Archive-Cpio-bin = %{version}-%{release}
Requires: perl-Archive-Cpio-license = %{version}-%{release}
Requires: perl-Archive-Cpio-man = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
No detailed description available

%package bin
Summary: bin components for the perl-Archive-Cpio package.
Group: Binaries
Requires: perl-Archive-Cpio-license = %{version}-%{release}
Requires: perl-Archive-Cpio-man = %{version}-%{release}

%description bin
bin components for the perl-Archive-Cpio package.


%package dev
Summary: dev components for the perl-Archive-Cpio package.
Group: Development
Requires: perl-Archive-Cpio-bin = %{version}-%{release}
Provides: perl-Archive-Cpio-devel = %{version}-%{release}

%description dev
dev components for the perl-Archive-Cpio package.


%package license
Summary: license components for the perl-Archive-Cpio package.
Group: Default

%description license
license components for the perl-Archive-Cpio package.


%package man
Summary: man components for the perl-Archive-Cpio package.
Group: Default

%description man
man components for the perl-Archive-Cpio package.


%prep
%setup -q -n Archive-Cpio-0.10
cd ..
%setup -q -T -D -n Archive-Cpio-0.10 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Archive-Cpio-0.10/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Archive-Cpio
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-Archive-Cpio/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.0/Archive/Cpio.pm
/usr/lib/perl5/vendor_perl/5.28.0/Archive/Cpio/Common.pm
/usr/lib/perl5/vendor_perl/5.28.0/Archive/Cpio/File.pm
/usr/lib/perl5/vendor_perl/5.28.0/Archive/Cpio/FileHandle_with_pushback.pm
/usr/lib/perl5/vendor_perl/5.28.0/Archive/Cpio/NewAscii.pm
/usr/lib/perl5/vendor_perl/5.28.0/Archive/Cpio/ODC.pm
/usr/lib/perl5/vendor_perl/5.28.0/Archive/Cpio/OldBinary.pm

%files bin
%defattr(-,root,root,-)
/usr/bin/cpio-filter

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Archive::Cpio.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Archive-Cpio/deblicense_copyright

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/cpio-filter.1
