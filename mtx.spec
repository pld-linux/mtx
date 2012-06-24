Summary:	Program for controlling SCSI media changers and tape drives
Summary(pl):	Program do obs�ugi zmieniarek oraz robot�w ta�mowych na SCSI
Summary(ru):	��������� ������� � ��������������� ��� ��������� ��������� DDS
Summary(uk):	���դ ������� � ������������������ ��� ��Ҧ������ ������ϧ� DDS
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
MTX jest zestawem program�w do kontrolowania nap�d�w ta�mowych oraz
mechanizm�w robot�w �adowarek oraz bibliotek ta�mowych.

%description -l ru
��������� MTX ��������� ���������������� ���������� � ���������������
� ��������� �����������.

%description -l uk
�������� MTX ���դ ������������� ����Φ���� � ������������������ ��
��Ҧ������ ¦�̦������.

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
