Summary:	Program for controlling SCSI media changers and tape drives
Summary(pl.UTF-8):   Program do obsługi zmieniarek oraz robotów taśmowych na SCSI
Summary(ru.UTF-8):   Управляет роботом в автозагрузчиках для ленточных устройств DDS
Summary(uk.UTF-8):   Керує роботом в автозавантажувачах для стрічкових пристроїв DDS
Name:		mtx
Version:	1.2.17
Release:	1
Epoch:		1
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/mtx/%{name}-%{version}rel.tar.gz
# Source0-md5:	d60f7b003edc6f9d34753b8f6c447515
Patch0:		%{name}-Makefile.patch
Patch1:		%{name}-gkh.patch
URL:		http://mtx.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MTX is a set of programs for controlling tape drives and the robotic
mechanism of autoloaders and tape libraries.

%description -l pl.UTF-8
MTX jest zestawem programów do kontrolowania napędów taśmowych oraz
mechanizmów robotów ładowarek oraz bibliotek taśmowych.

%description -l ru.UTF-8
Программа MTX управляет роботизированным механизмом в автозагрузчиках
и ленточных библиотеках.

%description -l uk.UTF-8
Програма MTX керує роботизованим механізмом в автозавантажувачах та
стрічкових бібліотеках.

%prep
%setup -q -n %{name}-%{version}rel
%patch0 -p1
%patch1 -p1

%build
cp -f /usr/share/automake/config.sub .
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COMPATABILITY CHANGES mtxl.README.html
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man1/*
