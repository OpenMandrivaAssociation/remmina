%define oname Remmina

Summary:	GTK+ remote desktop client
Name:		remmina
Version:	1.0.0
Release:	3
License:	GPLv2+
Group:		Networking/Remote access
Url:		http://remmina.sourceforge.net/
Source0:	https://github.com/downloads/FreeRDP/Remmina/%{oname}-%{version}.tar.gz
Patch0:		remmina-1.0-rosa-linkage.patch
Patch1:		remmina-1.0-rosa-datadir.patch
Patch2:		remmina-1.0-rosa-desktop.patch
Patch3:		remmina-1.0-rosa-libdir.patch

# Fix some linking errors
# https://github.com/FreeRDP/Remmina/commit/503a008e
Patch100:         remmina-1.0.0-fix-library-name.patch

# The following 4 patches are needed to add clipboard support (#818155)
# https://github.com/FreeRDP/Remmina/commit/3ebdd6e7
Patch102:         remmina-1.0.0-add-clipboard-support.patch
# https://github.com/FreeRDP/Remmina/commit/97c2af8c
Patch103:         remmina-1.0.0-clipboard-bugfix.patch
# https://github.com/FreeRDP/Remmina/commit/84327f81
Patch104:         remmina-1.0.0-some-more-clipboard-fixes.patch
# https://github.com/FreeRDP/Remmina/commit/c1ef3a16
Patch105:         remmina-1.0.0-disconnect-signal-handler-after-disconnect.patch

# https://github.com/FreeRDP/Remmina/commit/6ee20289
Patch110:        remmina-1.0.0-fix-crashes-in-some-cases.patch
# https://github.com/FreeRDP/Remmina/commit/b2277827
Patch111:        remmina-1.0.0-fix-memory-leak.patch

# Fedora bug:   https://bugzilla.redhat.com/show_bug.cgi?id=953678
# upstream bug: https://github.com/FreeRDP/Remmina/issues/63
# upstream fix: https://github.com/FreeRDP/Remmina/commit/1901a1e9
Patch112:        remmina-1.0.0-fix-typo-when-fitting-window.patch

# Fedora bug:   https://bugzilla.redhat.com/show_bug.cgi?id=834883
# upstream bug: https://github.com/FreeRDP/Remmina/issues/76
# upstream fix: https://github.com/FreeRDP/Remmina/commit/1901a1e9
Patch113:        remmina-1.0.0-trayicon.patch

# Fedora bug:   https://bugzilla.redhat.com/show_bug.cgi?id=830210
# upstream fix: https://github.com/FreeRDP/Remmina/commit/
Patch114:        remmina-1.0.0-fix-scrolling-in-vnc-plugin.patch
# upstream fix: https://github.com/FreeRDP/Remmina/commit/fe1b698e
Patch115:        remmina-1.0.0-Also-handle-GDK_SCROLL_SMOOTH.patch

# upstream bug: https://github.com/FreeRDP/Remmina/issues/77
# upstream fix: https://github.com/FreeRDP/Remmina/commit/bed49ad6
Patch116:        remmina-1.0.0-close-SSH-tunnel-on-disconnect.patch

# Fedora bug:   https://bugzilla.redhat.com/show_bug.cgi?id=864262
# upstream fix: https://github.com/FreeRDP/Remmina/commit/348e01d2
Patch117:        remmina-1.0.0-fix-fullscreen-with-multiple-monitors.patch

# From Debian. Thanks to Luca Falavigna <dktrkranz at debian dot org>
Patch135:        remmina-1.0.0-remove-inline-libvncserver.patch

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
BuildRequires:	pkgconfig(libssh)
BuildRequires:	pkgconfig(libvncserver)
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

%patch100 -p1 -b .fix-library-name

%patch102 -p1 -b .add-clipboard-support
%patch103 -p1 -b .clipboard-bugfix
%patch104 -p1 -b .some-more-clipboard-fixes
%patch105 -p1 -b .disconnect-signal-handler

%patch110 -p1 -b .fix-crashes-in-some-cases
%patch111 -p1 -b .fix-memory-leak

%patch112 -p1 -b .fitting-window

%patch113 -p1 -b .trayicon

%patch114 -p1 -b .vnc-scrolling

%patch115 -p1 -b .GDK_SCROLL_SMOOTH

%patch116 -p1 -b .ssh-disconnect

%patch117 -p1 -b .multiple-monitors

%patch135 -p1 -b .libvncserver



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

