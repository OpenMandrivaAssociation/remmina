%define oname Remmina

Summary:	GTK+ remote desktop client
Name:		remmina
Version:	1.0.0
Release:	1
License:	GPLv2+
Group:		Networking/Remote access
Url:		http://remmina.sourceforge.net/
Source0:	https://github.com/downloads/FreeRDP/Remmina/%{oname}-%{version}.tar.gz
Patch0:		remmina-1.0-rosa-linkage.patch
Patch1:		remmina-1.0-rosa-datadir.patch
Patch2:		remmina-1.0-rosa-desktop.patch
Patch3:		remmina-1.0-rosa-libdir.patch
Requires:	rdesktop
# We don't have x11-server-xephyr so try to live without it
#Requires:	x11-server-xephyr
BuildRequires:	cmake
BuildRequires:	rdesktop
BuildRequires:	pkgconfig(gdk-3.0)
BuildRequires:	pkgconfig(vte-2.90)
BuildRequires:	pkgconfig(appindicator3-0.1)
BuildRequires:	pkgconfig(avahi-ui-gtk3)
BuildRequires:	pkgconfig(avahi-client)
BuildRequires:	pkgconfig(xkbfile)
BuildRequires:	pkgconfig(freerdp) >= 1.0
BuildRequires:	pkgconfig(gnome-keyring-1)
BuildRequires:	zlib-devel
BuildRequires:	jpeg-devel
BuildRequires:	gnutls-devel
BuildRequires:	libssh-devel >= 0.4
BuildRequires:	libavahi-ui-devel
BuildRequires:	pkgconfig(vte)
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

%package plugins
Summary:	A set of plugins for remmina
Requires:	%{name} = %{version}

%description plugins
A set of plugins for remote desktop client - remmina.

%package devel
Summary:	Developmnet files for %{name}
Group:		Development/C++
Requires:	%{name} = %{version}-%{release}

%description devel
Development files and headers for %{name}.

%prep
%setup -q -n FreeRDP-Remmina-356c033
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
# FIXME: telepathy plugin is broken
%cmake -DWITH_TELEPATHY:BOOL=OFF
%make

%install
pushd build
%makeinstall_std
popd

%__rm -f %{buildroot}%{_iconsdir}/hicolor/icon-theme.cache

# FIXME: includedir is empty
rm -rf %{buildroot}/%{_includedir}

%find_lang %{name}
%find_lang %{name}-plugins

%files -f %{name}.lang
%doc remmina/AUTHORS remmina/ChangeLog remmina/NEWS remmina/README*
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
#%{_datadir}/%{name}/*
%{_iconsdir}/hicolor/*/apps/%{name}.*
%{_iconsdir}/hicolor/*/actions/%{name}*

%files plugins -f %{name}-plugins.lang
%doc remmina-plugins/AUTHORS remmina-plugins/ChangeLog remmina-plugins/NEWS remmina-plugins/README*
%{_libdir}/remmina/plugins
%{_iconsdir}/hicolor/*/emblems/%{name}*

%files devel
%{_libdir}/pkgconfig/*.pc
#%{_includedir}/%{name}/*.h

