%define theme zephyrus
%define Name Zephyrus
%define codename Aurora
%define status alpha
%define version 1.0.0

%define gtk_theme Adwaita
%define icon_theme SimpleSL
%define xfwm4_theme Adwaita

# Enable compositing on x86_64 only

%define def_desktop_wallpaper zephyrus_programming_16x9_1920x1080.png
%define web_browser firefox
%define media_player vlc
%define mail_reader sylpheed-claws
%define file_manager pcmanfm
%define lo_icon_theme auto
%define alterator_browser_weight 52
%define artworks_weight 12

Name: branding-zephyrus
Version: %version
Release: alt1
Summary: Branding for Zephyrus, a lightweight ALT Linux distro for programming
License: GPLv2+ and CC-BY-NC-SA-3.0+
Group: System/Configuration/Other
BuildArch: noarch

BuildRequires: rpm-build fonts-ttf-dejavu fonts-ttf-google-droid-serif fonts-ttf-google-droid-sans fonts-ttf-google-droid-sans-mono
BuildRequires: ImageMagick fontconfig bc qt6-base-devel
BuildRequires: distro-licenses >= 1.3-alt1
Source: %name-%version.tar

%description
Branding package for Zephyrus, a lightweight ALT Linux distribution optimized for programming on low-end PCs.

%description -l ru_RU.UTF-8
Пакеты для дистрибутива Zephyrus, лёгкого дистрибутива на основе ALT Linux для программирования на слабых ПК.

%package bootloader
Summary: Graphical boot logo for grub2, lilo, and syslinux
Group: System/Configuration/Boot and Init
Requires: coreutils
Provides: design-bootloader-%theme
Conflicts: branding-simply-linux-bootloader

%description bootloader
Graphical boot logo for Zephyrus, suitable for grub2, lilo, and syslinux.

%package bootsplash
Summary: Theme for splash animations during bootup
Group: System/Configuration/Boot and Init
Provides: plymouth-theme-%theme
Requires: plymouth plymouth-plugin-label fonts-ttf-dejavu
Conflicts: branding-simply-linux-bootsplash

%description bootsplash
Graphics for boot process for Zephyrus.

%package alterator
Summary: Design for alterator for Zephyrus
Group: System/Configuration/Other
Provides: design-alterator-%theme
Requires: alternatives >= 0.2 alterator
Conflicts: branding-simply-linux-alterator

%description alterator
Design for QT and web alterator for Zephyrus.

%package graphics
Summary: Design for Zephyrus
Group: Graphics
Provides: design-graphics-%theme
Requires: alternatives >= 0.2
Conflicts: branding-simply-linux-graphics

%description graphics
Graphics for Zephyrus design.

%package release
Summary: Zephyrus release file
Group: System/Configuration/Other
Requires: alt-os-release
Provides: altlinux-release-%theme
Conflicts: branding-simply-linux-release altlinux-release-sisyphus

%description release
Zephyrus release file.

%package notes
Summary: Distribution license and release notes
Group: Documentation
Provides: alt-notes-%theme
Conflicts: branding-simply-linux-notes alt-notes-sisyphus

%description notes
Distribution license and release notes for Zephyrus.

%package xfce-settings
Summary: Default settings for Xfce for Zephyrus
Group: Graphical desktop/XFce
Requires: PolicyKit-gnome etcskel gtk-theme-adwaita gnome-themes-standard gnome-icon-theme icon-theme-simple-sl xfce4-datetime-plugin xfce4-places-plugin xfce4-pulseaudio-plugin xfce4-whiskermenu-plugin xfce4-xkb-plugin
Conflicts: branding-simply-linux-xfce-settings

%description xfce-settings
Default settings for Xfce for Zephyrus.

%package slideshow
Summary: Slideshow for Zephyrus installer
Group: System/Configuration/Other
Conflicts: branding-simply-linux-slideshow

%description slideshow
Slideshow for Zephyrus installer.

%package indexhtml
Summary: Zephyrus HTML welcome page
Group: System/Base
Provides: indexhtml-%theme
Requires: xdg-utils
Conflicts: branding-simply-linux-indexhtml

%description indexhtml
Zephyrus HTML welcome page.

%package menu
Summary: Menu for Zephyrus
Group: Graphical desktop/Other
Requires: altlinux-freedesktop-menu-common
Conflicts: branding-simply-linux-menu

%description menu
Menu for Zephyrus.

%package system-settings
Summary: System settings for Zephyrus
Group: System/Base
Conflicts: branding-simply-linux-system-settings

%description system-settings
System settings for Zephyrus.

%prep
%setup -q
cp -a /usr/share/distro-licenses/ALT_Simply_License/license.ru.html.in notes/
cp -a /usr/share/distro-licenses/ALT_Simply_License/license.all.html.in notes/

%build
autoconf
THEME=%theme NAME='%Name' STATUS=%status VERSION=%version CODENAME='%codename' \
GTK_THEME=%gtk_theme ICON_THEME=%icon_theme XFWM4_THEME=%xfwm4_theme \
XFWM4_COMPOSITING=%xfwm4_compositing DEFAULT_WEB_BROWSER=%web_browser \
DEFAULT_MAIL_READER=%mail_reader DEFAULT_FILE_MANAGER=%file_manager \
LO_ICON_THEME=%lo_icon_theme MEDIA_PLAYER=%media_player \
ALTERATOR_BROWSER_WEIGHT=%alterator_browser_weight ./configure
make

%install
%makeinstall

# Graphics
mkdir -p %buildroot/%_datadir/design/{%theme,backgrounds}
mkdir -p %buildroot/%_niconsdir
install -m644 graphics/icons/zephyrus.png %buildroot/%_niconsdir/zephyrus.png
install -m644 graphics/icons/mini/zephyrus.png %buildroot/%_iconsdir/altlinux.png
cp -ar graphics/* %buildroot/%_datadir/design/%theme
pushd %buildroot/%_datadir/design/%theme/backgrounds
ln -sf ../../../wallpapers more
popd
install -d %buildroot/etc/alternatives/packages.d
cat >%buildroot/etc/alternatives/packages.d/%name-graphics <<__EOF__
%_datadir/artworks	%_datadir/design/%theme %artworks_weight
%_datadir/design-current	%_datadir/design/%theme	%artworks_weight
%_datadir/design/current	%_datadir/design/%theme	%artworks_weight
__EOF__

# Release
install -pD -m644 /dev/null %buildroot%_sysconfdir/buildreqs/packages/ignore.d/%name-release
install -pD -m644 components/systemd/os-release %buildroot%_prefix/lib/os-release
echo "%Name %version %status (%codename)" >%buildroot%_sysconfdir/altlinux-release
ln -s altlinux-release %buildroot%_sysconfdir/fedora-release
ln -s altlinux-release %buildroot%_sysconfdir/redhat-release
ln -s altlinux-release %buildroot%_sysconfdir/system-release

# Notes
pushd notes
%makeinstall
popd
ln -s license.ru.html %buildroot%_datadir/alt-notes/license.uk.htm

# Slideshow
mkdir -p %buildroot/usr/share/install2/slideshow
mkdir -p %buildroot/etc/alterator
pushd slideshow
cp -a Slides*/ %buildroot/usr/share/install2/slideshow/
popd
ln -s Slides-en %buildroot/usr/share/install2/slideshow/Slides
install -m0644 slideshow/slideshow.conf %buildroot/etc/alterator/

# Menu
mkdir -p %buildroot/usr/share/zephyrus-style/applications
install -m644 menu/applications/* %buildroot/usr/share/zephyrus-style/applications/
mkdir -p %buildroot/etc/xdg/menus/xfce-applications-merged
cp menu/50-xfce-applications.menu %buildroot/etc/xdg/menus/xfce-applications-merged/
mkdir -p %buildroot/usr/share/desktop-directories
cp menu/altlinux-wine.directory %buildroot/usr/share/desktop-directories/

%post bootloader
[ "$1" -eq 1 ] || exit 0
. shell-config
shell_config_set /etc/sysconfig/grub2 GRUB_THEME /boot/grub/themes/%theme/theme.txt

%post indexhtml
%_sbindir/indexhtml-update

%post graphics
[ -e %_datadir/design/zephyrus/backgrounds/default.png ] || \
	ln -s default-16x9.png %_datadir/design/zephyrus/backgrounds/default.png
[ -e %_datadir/design/zephyrus/backgrounds/xdm.png ] || \
	ln -s xdm-16x9.png %_datadir/design/zephyrus/backgrounds/xdm.png

%post xfce-settings
if [ "$(readlink %_datadir/backgrounds/xfce/default-background)" != "%def_desktop_wallpaper" ]; then
	ln -sf "%def_desktop_wallpaper" %_datadir/backgrounds/xfce/default-background ||:
fi

%postun xfce-settings
if [ "$1" -eq 0 ] && \
		[ "$(readlink %_datadir/backgrounds/xfce/default-background)" = "%def_desktop_wallpaper" ] && \
		[ -e %_datadir/backgrounds/xfce/%xfce_default_background ]; then
	ln -sf %xfce_default_background %_datadir/backgrounds/xfce/default-background ||:
fi

%files alterator
%_altdir/*.rcc
/usr/share/alterator-browser-qt/design/*.rcc
/usr/share/alterator/design/*

%files graphics
/etc/alternatives/packages.d/%name-graphics
%_datadir/design
%_niconsdir/zephyrus.png
%_iconsdir/altlinux.png
%ghost %_datadir/design/zephyrus/backgrounds/default.png
%ghost %_datadir/design/zephyrus/backgrounds/xdm.png

%files bootloader
/boot/grub/themes/%theme

%files bootsplash
%dir /usr/share/plymouth/themes/%theme

%files release
%_sysconfdir/*-release
%_prefix/lib/os-release
%_sysconfdir/buildreqs/packages/ignore.d/*

%files notes
%_datadir/alt-notes/*

%files slideshow
/etc/alterator/slideshow.conf
/usr/share/install2/slideshow

%files indexhtml
%_defaultdocdir/indexhtml/*
%_desktopdir/indexhtml.desktop

%files menu
/usr/share/desktop-directories/*

%files system-settings
%_datadir/polkit-1/rules.d/*.rules
%_datadir/install3/*

%changelog
* Mon Jun 09 2025 Your Name <your.email@altlinux.org> 1.0.0-alt1
- Initial branding for Zephyrus, a lightweight ALT Linux distro for programming
