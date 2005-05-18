Summary:	Program for controlling SCSI media changers and tape drives
Summary(pl):	Program do obsЁugi zmieniarek oraz robotСw ta╤mowych na SCSI
Summary(ru):	Управляет роботом в автозагрузчиках для ленточных устройств DDS
Summary(uk):	Керу╓ роботом в автозавантажувачах для стр╕чкових пристро╖в DDS
Name:		mtx
Version:	1.3.3
Release:	2
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/mtx/%{name}-%{version}.tar.gz
# Source0-md5:	069c47d2af6b057cf2a123e6e56f79e6
Patch0:		%{name}-Makefile.patch
Patch1:		%{name}-gkh.patch
URL:		http://mtx.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MTX is a set of programs for controlling tape drives and the robotic
mechanism of autoloaders and tape libraries.

%description -l pl
MTX jest zestawem programСw do kontrolowania napЙdСw ta╤mowych oraz
mechanizmСw robotСw Ёadowarek oraz bibliotek ta╤mowych.

%description -l ru
Программа MTX управляет роботизированным механизмом в автозагрузчиках
и ленточных библиотеках.

%description -l uk
Програма MTX керу╓ роботизованим механ╕змом в автозавантажувачах та
стр╕чкових б╕бл╕отеках.

%prep
%setup -q
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
