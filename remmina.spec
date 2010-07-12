%define name	remmina
%define version 0.7.5
%define release %mkrel 1

Summary:	GTK+ remote desktop client
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.gz
License:	GPLv2
Group:		Networking/Remote access
Url:		http://remmina.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
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

%description
Remmina is a remote desktop client written in GTK+, aiming to be
useful for system administrators and travellers, who need to work with
lots of remote computers in front of either large monitors or tiny
netbooks. Remmina supports multiple network protocols in an integrated
and consistant user interface. Currently RDP, VNC, XDMCP and SSH are
supported.

%prep
%setup -q

%build
aclocal
autoconf
%configure
%make

%install
%__rm -rf %{buildroot}
%makeinstall 
%__rm -f %{buildroot}%{_iconsdir}/hicolor/icon-theme.cache

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README*
%_bindir/%{name}
%_datadir/applications/%{name}.desktop
%_datadir/locale/*/*/%{name}.mo
%_datadir/%{name}/*
%_iconsdir/hicolor/*/apps/%{name}.*
