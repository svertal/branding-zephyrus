AC_INIT( [branding], [0.1], [http://bugzilla.altlinux.ru] )

# 00a1e4
PROGRESS_COLOR=0093d7 
TITLE_COLOR=5C96CC
LIGHT_COLOR_HEX=DFDFE0
MIDDLE_COLOR_HEX=C8C9CB
DARK_COLOR_HEX=909195
LIGHT_LABELS_HEX=FFFFFF
DARK_LABELS_HEX=000000
MIDDLE_LABELS_HEX=4d4d4f
YEAR="$(date +%Y)"

DOCDIR=documentation

AC_SUBST(THEME)
AC_SUBST(NAME)
AC_SUBST(STATUS)
AC_SUBST(VERSION)
AC_SUBST(CODENAME)
AC_SUBST(DOCDIR)
AC_SUBST(PROGRESS_COLOR)
AC_SUBST(LIGHT_COLOR_HEX)
AC_SUBST(MIDDLE_COLOR_HEX)
AC_SUBST(DARK_COLOR_HEX)
AC_SUBST(LIGHT_LABELS_HEX)
AC_SUBST(DARK_LABELS_HEX)
AC_SUBST(MIDDLE_LABELS_HEX)
AC_SUBST(TITLE_COLOR)
AC_SUBST(GTK_THEME)
AC_SUBST(ICON_THEME)
AC_SUBST(XFWM4_THEME)
AC_SUBST(XFWM4_COMPOSITING)
AC_SUBST(DEFAULT_WEB_BROWSER)
AC_SUBST(DEFAULT_MAIL_READER)
AC_SUBST(DEFAULT_FILE_MANAGER)
AC_SUBST(LO_ICON_THEME)
AC_SUBST(MEDIA_PLAYER)
AC_SUBST(ALTERATOR_BROWSER_WEIGHT)
AC_SUBST(YEAR)

AC_CONFIG_FILES([
		 Makefile
		 components/browser-qt/design/design.ini
		 notes/release-notes.ru.html
		 notes/release-notes.uk.html
		 notes/release-notes.all.html
		 notes/license.ru.html
		 notes/license.all.html
		 components/indexhtml/indexhtml.desktop
		 components/indexhtml/index-ru.html
		 components/indexhtml/index-en.html
		 components/systemd/os-release
		 system-settings/lightdm-gtk-greeter.conf
		 xfce-settings/etcskel/.config/libreoffice/4/user/registrymodifications.xcu
		 xfce-settings/etcskel/.config/xfce4/helpers.rc
		 xfce-settings/etcskel/.config/xfce4/xfconf/xfce-perchannel-xml/xfwm4.xml
		 xfce-settings/etcskel/.config/xfce4/xfconf/xfce-perchannel-xml/xsettings.xml
		 xfce-settings/etcskel/.config/xfce4/xfconf/xfce-perchannel-xml/thunar-volman.xml
		 xfce-settings/etcskel/.local/share/applications/mimeapps.list
])
AC_OUTPUT
