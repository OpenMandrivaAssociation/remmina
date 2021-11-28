%bcond_with appindicator
%bcond_without kwallet_plugin
%bcond_with nx_plugin
%bcond_with xdmcp_plugin
%bcond_with st_plugin

Name:		remmina
Version:	1.4.21
Release:	1
Summary:	GTK+ remote desktop client
Group:		Networking/Remote access
License:	GPLv2+
URL:		http://www.remmina.org/wp/
Source0:	https://gitlab.com/Remmina/Remmina/-/archive/v%{version}/Remmina-v%{version}.tar.bz2
#Mirror Source0:	https://github.com/FreeRDP/Remmina/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	cups-devel
BuildRequires:	pkgconfig(avahi-client) >= 0.6.3
BuildRequires:	pkgconfig(avahi-ui-gtk3) >= 0.6.30
BuildRequires:	pkgconfig(json-glib-1.0)
BuildRequires:	pkgconfig(gnutls)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(harfbuzz)
BuildRequires:	pkgconfig(appindicator3-0.1)
BuildRequires:	pkgconfig(libgcrypt)
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(libpcre2-8)
BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:	pkgconfig(libssh)
BuildRequires:	pkgconfig(libsodium)
BuildRequires:	pkgconfig(libvncserver)
BuildRequires:	pkgconfig(spice-client-gtk-3.0)
BuildRequires:	pkgconfig(TelepathyQt5)
BuildRequires:	pkgconfig(xkbfile)
BuildRequires:	pkgconfig(vte-2.91)
BuildRequires:	pkgconfig(webkit2gtk-4.0)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	qmake5
BuildRequires:	xdg-utils

%description
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travelers, who need to work with lots of remote
computers in front of either large monitors or tiny netbooks.

Remmina supports multiple network protocols in an integrated and consistent
user interface. Currently RDP, VNC, XDMCP and SSH are supported.

Please don't forget to install the plugins for the protocols you want to use.

%files -f %{name}.lang
%doc AUTHORS CHANGELOG.md README.md THANKS.md COPYING LICENSE
%{_bindir}/remmina-file-wrapper
%{_bindir}/%{name}
%{_bindir}/%{name}-gnome
%{_bindir}/gnome-session-%{name}
%{_datadir}/%{name}/
%{_datadir}/gnome-session/sessions/%{name}-gnome.session
%{_datadir}/xsessions/%{name}-gnome.desktop
%{_datadir}/applications/org.%{name}.Remmina.desktop
%{_datadir}/applications/org.%{name}.Remmina-file.desktop
%{_datadir}/applications/%{name}-gnome.desktop
%{_datadir}/metainfo/org.%{name}.Remmina.appdata.xml
%{_datadir}/mime/packages/%{name}-mime.xml
%{_iconsdir}/hicolor/*/apps/*%{name}*.svg
%{_iconsdir}/hicolor/*/apps/*%{name}*.png
%{_iconsdir}/hicolor/*/actions/org.%{name}.Remmina-*.svg
%{_iconsdir}/hicolor/*/emblems/org.%{name}.Remmina-sftp-*.svg
%{_iconsdir}/hicolor/*/emblems/org.%{name}.Remmina-ssh-*.svg
%{_iconsdir}/hicolor/*/emblems/org.%{name}.Remmina-tool-*.svg
%{_iconsdir}/hicolor/*/status/org.%{name}.Remmina-status.svg
#%{_iconsdir}/hicolor/*/actions/view-list.svg
%{_iconsdir}/hicolor/apps/org.%{name}.Remmina-symbolic.svg
%{_iconsdir}/hicolor/apps/remmina-symbolic.svg
#%{_iconsdir}/hicolor/scalable/panel/remmina-panel-inverted.svg
#%{_iconsdir}/hicolor/scalable/panel/remmina-panel.svg
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man1/%{name}-gnome.1.*
%{_mandir}/man1/gnome-session-%{name}.1.*
%{_mandir}/man1/remmina-file-wrapper.1.*

#----------------------------------------------------------------------------

%package devel
Summary:	Development files for %{name}
Group:		Development/GNOME and GTK+
Requires:	%{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains header files for developing plugins for
%{name}.

%files devel
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/%{name}.pc

#----------------------------------------------------------------------------

%package plugins-common
Summary:	Common files for Remmina Remote Desktop Client plugins
Group:		Networking/Remote access
Requires:	%{name} = %{version}-%{release}

%description plugins-common
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travelers, who need to work with lots of remote
computers in front of either large monitors or tiny netbooks.

This package contains files shared among all plugins for the Remmina remote
desktop client.

%files plugins-common
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/plugins/

#----------------------------------------------------------------------------

%package plugins-exec
Summary:	External execution plugin for Remmina Remote Desktop Client
Group:		Networking/Remote access
Requires:	%{name}-plugins-common = %{version}-%{release}

%description plugins-exec
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travelers, who need to work with lots of remote
computers in front of either large monitors or tiny netbooks.

This package contains the plugin to execute external processes (commands or
applications) from the Remmina window.

%files plugins-exec
%{_libdir}/%{name}/plugins/%{name}-plugin-exec.so

#----------------------------------------------------------------------------

%if %{with kwallet_plugin}
%package plugins-kwallet
Summary:	KWallet integration for Remmina Remote Desktop Client
Group:		Networking/Remote access
BuildRequires:	lib64KF5Wallet-devel
Requires:	%{name}-plugins-common = %{version}-%{release}

Obsoletes:	remmina-plugins-kwallet < 1.2.0-0.rcgit.24.2
Provides:	remmina-plugins-kwallet = %{version}-%{release}

%description plugins-kwallet
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travelers, who need to work with lots of remote
computers in front of either large monitors or tiny netbooks.

This package contains the plugin with kwallet support for the Remmina remote
desktop client.

%files plugins-kwallet
%{_libdir}/%{name}/plugins/%{name}-plugin-kwallet.so
%endif

#----------------------------------------------------------------------------

%if %{with nx_plugin}
%package plugins-nx
Summary:	NX plugin for Remmina Remote Desktop Client
Group:		Networking/Remote access
Requires:	%{name}-plugins-common = %{version}-%{release}
Requires:	nxproxy

%description plugins-nx
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travelers, who need to work with lots of remote
computers in front of either large monitors or tiny netbooks.

This package contains the NX plugin for the Remmina remote desktop client.

%files plugins-nx
%{_libdir}/%{name}/plugins/%{name}-plugin-nx.so
#%{_iconsdir}/hicolor/*/emblems/org.%{name}.Remmina-nx-*.svg
%endif

#----------------------------------------------------------------------------

%package plugins-secret
Summary:	Keyring integration for Remmina Remote Desktop Client
Group:		Networking/Remote access
BuildRequires:	pkgconfig(libsecret-1)
Requires:	%{name}-plugins-common = %{version}-%{release}

Obsoletes:	remmina-plugins-gnome < 1.2.0-0.rcgit.24.2
Provides:	remmina-plugins-gnome = %{version}-%{release}

%description plugins-secret
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travelers, who need to work with lots of remote
computers in front of either large monitors or tiny netbooks.

This package contains the plugin with keyring support for the Remmina remote
desktop client.

%files plugins-secret
%{_libdir}/%{name}/plugins/%{name}-plugin-secret.so

#----------------------------------------------------------------------------

%package plugins-rdp
Summary:	RDP plugin for Remmina Remote Desktop Client
Group:		Networking/Remote access
BuildRequires:	pkgconfig(freerdp2) >= 2.0
Requires:	%{name}-plugins-common = %{version}-%{release}
Requires:	freerdp >= 2.0

%description plugins-rdp
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travelers, who need to work with lots of remote
computers in front of either large monitors or tiny netbooks.

This package contains the Remote Desktop Protocol (RDP) plugin for the Remmina
remote desktop client.

%files plugins-rdp
%{_libdir}/%{name}/plugins/%{name}-plugin-rdp.so
%{_iconsdir}/hicolor/*/emblems/org.%{name}.Remmina-rdp-*.svg

#----------------------------------------------------------------------------

%package plugins-spice
Summary:	SPICE plugin for Remmina Remote Desktop Client
Group:		Networking/Remote access
Requires:	%{name}-plugins-common = %{version}-%{release}

%description plugins-spice
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travelers, who need to work with lots of remote
computers in front of either large monitors or tiny netbooks.

This package contains the SPICE plugin for the Remmina remote desktop client.

%files plugins-spice
%{_libdir}/%{name}/plugins/%{name}-plugin-spice.so
%{_iconsdir}/hicolor/*/emblems/org.%{name}.Remmina-spice-*.svg

#----------------------------------------------------------------------------

%if %{with st_plugin}
%package plugins-st
Summary:	Socket Terminal plugin for Remmina Remote Desktop Client
Group:		Networking/Remote access
Requires:	%{name}-plugins-common = %{version}-%{release}

%description plugins-st
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travelers, who need to work with lots of remote
computers in front of either large monitors or tiny netbooks.

This package contains the Socket Terminal plugin for the Remmina remote
desktop client.

%files plugins-st
%{_libdir}/%{name}/plugins/%{name}-plugin-st.so
%endif

#----------------------------------------------------------------------------

%package plugins-vnc
Summary:	VNC plugin for Remmina Remote Desktop Client
Group:		Networking/Remote access
BuildRequires:	pkgconfig(gnutls)
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(libvncserver)
Requires:	%{name}-plugins-common = %{version}-%{release}

%description plugins-vnc
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travelers, who need to work with lots of remote
computers in front of either large monitors or tiny netbooks.

This package contains the VNC plugin for the Remmina remote desktop
client.

%files plugins-vnc
%{_libdir}/%{name}/plugins/%{name}-plugin-vnc.so
%{_iconsdir}/hicolor/*/emblems/org.%{name}.Remmina-vnc-*.svg

#----------------------------------------------------------------------------

%if %{with xdmcp_plugin}
%package plugins-xdmcp
Summary:	XDMCP plugin for Remmina Remote Desktop Client
Group:		Networking/Remote access
Requires:	%{name}-plugins-common = %{version}-%{release}
Requires:	x11-server-xephyr

%description plugins-xdmcp
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travelers, who need to work with lots of remote
computers in front of either large monitors or tiny netbooks.

This package contains the XDMCP plugin for the Remmina remote desktop
client.

%files plugins-xdmcp
%{_libdir}/%{name}/plugins/%{name}-plugin-xdmcp.so
%{_iconsdir}/hicolor/*/emblems/org.%{name}.Remmina-xdmcp-*.svg
%endif

#----------------------------------------------------------------------------

%package plugins-www
Summary:	www plugin for Remmina Remote Desktop Client
Group:		Networking/Remote access
Requires:	%{name}-plugins-common = %{version}-%{release}
Requires:	x11-server-xephyr
Obsoletes:	remmina-plugins-telepathy 

%description plugins-www
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travelers, who need to work with lots of remote
computers in front of either large monitors or tiny netbooks.

This package contains the www plugin for the Remmina remote desktop
client.

%files plugins-www
%{_libdir}/remmina/plugins/remmina-plugin-www.so
%{_iconsdir}/hicolor/scalable/emblems/org.%{name}.Remmina-www-symbolic.svg

#----------------------------------------------------------------------------

%prep
%autosetup  -p1 -n Remmina-v%{version}

%build
%cmake \
	-DWITH_KF5WALLET:BOOL=%{?with_kwallet_plugin:ON}%{?!with_kwallet_plugin:OFF} \
	-DWITH_NX:BOOL=%{?with_nx_plugin:ON}%{?!with_nx_plugin:OFF} \
	-DWITH_XDMCP:BOOL=%{?with_nxdmcp_plugin:ON}%{?!with_xdmcp_plugin:OFF} \
	-DWITH_ST:BOOL=%{?with_st_plugin:ON}%{?!with_st_plugin:OFF} \
	-DWITH_KIOSK_SESSION=ON \
	-DWITH_APPINDICATOR:BOOL=%{?with_appindicator:ON}%{?!with_appindicator:OFF} \
	-G Ninja
cd ..
%ninja_build -C build

%install
%ninja_install -C build

# .desktop
desktop-file-install \
	--remove-category="X-GNOME-NetworkSettings" \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/org.%{name}.Remmina.desktop

# locales
%find_lang %{name}
