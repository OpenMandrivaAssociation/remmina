Summary:	GTK+ remote desktop client
Name:		remmina
Version:	0.9.3
Release:	%mkrel 2
License:	GPLv2
Group:		Networking/Remote access
Url:		http://remmina.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/remmina/%{version}/%{name}-%{version}.tar.gz
Requires:	rdesktop
Requires:	x11-server-xephyr
BuildRequires:	rdesktop
BuildRequires:	gtk2-devel >= 2.16
BuildRequires:	zlib-devel
BuildRequires:	jpeg-devel
BuildRequires:	gnutls-devel
BuildRequires:	libssh-devel >= 0.4
BuildRequires:	libavahi-ui-devel
BuildRequires:	libvte-devel
BuildRequires:	libgcrypt-devel
BuildRequires:	unique-devel
BuildRequires:	intltool >= 0.35.0
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Remmina is a remote desktop client written in GTK+, aiming to be
useful for system administrators and travellers, who need to work with
lots of remote computers in front of either large monitors or tiny
netbooks. Remmina supports multiple network protocols in an integrated
and consistant user interface. Currently RDP, VNC, XDMCP and SSH are
supported.

%package devel
Summary:	Developmnet files for %{name}
Group:		Development/C++
Requires:	%{name} = %{version}-%{release}

%description devel
Development files and headers for %{name}.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std
%__rm -f %{buildroot}%{_iconsdir}/hicolor/icon-theme.cache

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README*
%_bindir/%{name}
%_datadir/applications/%{name}.desktop
%_datadir/locale/*/*/%{name}.mo
%_datadir/%{name}/*
%_iconsdir/hicolor/*/apps/%{name}.*

%files devel
%{_includedir}/%{name}/*.h
