Name:           stenc
Version:        1.0.8
Release:        1%{?dist}
Summary:        SCSI Tape Encryption Manager

License:        GPLv2
URL:            https://github.com/scsitape/%{name}
Source0:        https://github.com/scsitape/%{name}/archive/%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  gcc-c++
BuildRequires:  autoconf
BuildRequires:  automake

%description
SCSI Tape Encryption Manager - Manages encryption on LTO 4 and newer tape
drives with hardware-based encryption

%prep
%setup -q

%build
./autogen.sh
%configure
make 

%install
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING README.md AUTHORS
%{_bindir}/stenc
%{_mandir}/man1/stenc.1*

%changelog
* Tue Sep 1 2020  Seth Tunstall <seth.tunstall@unipart.io> 1.0.8
- Initial SPEC file

