Summary:	Program for controlling SCSI media changers and tape drives
Summary(pl):	Program do obs³ugi zmieniarek oraz robotów ta¶mowych na SCSI
Name:		mtx
Version:	1.2.15
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		%{name}-Makefile.patch
URL:		http://mtx.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MTX is a set of programs for controlling tape drives and the robotic
mechanism of autoloaders and tape libraries.

%description -l pl
MTX jest zestawem programów do kontrolowania napêdów ta¶mowych oraz
mechanizmów robotów ³adowarek oraz bibliotek ta¶mowych.

%prep
%setup  -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COMPATABILITY CHANGES mtxl.README.html
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man1/*
