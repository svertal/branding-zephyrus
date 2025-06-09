.PHONY: browser-qt ahttpd graphics indexhtml grub-install system-settings-install

# browser-qt
components/browser-qt/design/bg.png: images/installer.png
	if [ -n "$(STATUS)" ]; then \
		magick $< -fill '#c62530' -font /usr/share/fonts/ttf/dejavu/DejaVuSansCondensed-Bold.ttf -style Normal -weight Normal -pointsize 20 -gravity northeast -draw 'text 25,25 "$(STATUS)"' $@; \
	else \
		cp -a $< $@; \
	fi

browser-qt: components/browser-qt/design/bg.png
	install -d $(datadir)/alterator-browser-qt/design
	cd components/browser-qt; `qtpaths-qt6 --query QT_HOST_LIBEXECS`/rcc -binary theme.qrc -o $(datadir)/alterator-browser-qt/design/$(THEME).rcc; cd -
	install -d $(sysconfdir)/alternatives/packages.d
	printf '/etc/alterator/design-browser-qt\t/usr/share/alterator-browser-qt/design/$(THEME).rcc\t$(ALTERATOR_BROWSER_WEIGHT)\n'>$(sysconfdir)/alternatives/packages.d/$(THEME).rcc

# ahttpd
ahttpd:
	install -d $(datadir)/alterator/design/styles
	cp -a components/ahttpd/images $(datadir)/alterator/design
#	install -Dpm644 images/product-logo.png $(datadir)/alterator/design/images/product-logo.png
	cp -a components/ahttpd/styles/*.css $(datadir)/alterator/design/styles

graphics:
	magick -colorspace YCbCr -sampling-factor 2x2 images/boot.png JPEG:images/boot.jpg
	for size in 1024x768 800x600 640x480; do \
		magick images/boot.jpg -quality 97 -resize "$$size!" -fill '#c62530' -font /usr/share/fonts/ttf/dejavu/DejaVuSansCondensed-Bold.ttf -style Normal -weight Normal -pointsize 20 -gravity northeast -draw 'text 25,25 "$(STATUS)"' boot-$$size.jpg ;\
	done
# background
	for w in images/wallpaper-*.png; do \
		f_name=`basename $$w`; \
		suff="$${f_name#wallpaper-}"; \
		size="$${f_name%.*}"; \
		magick $$w -fill '#c62530' -font /usr/share/fonts/ttf/google-droid/DroidSans-Bold.ttf -style Normal -weight Normal -pointsize 20 -gravity northeast -draw 'text 25,25 "$(STATUS)"' "$$f_name"; \
		cp -al "$$f_name" graphics/backgrounds/default-"$$suff"; \
		ln -s default-"$$suff" graphics/backgrounds/xdm-"$$suff"; \
	done
	ln -s default-16x9.png graphics/backgrounds/default.png
	ln -s xdm-16x9.png graphics/backgrounds/xdm.png

# index html page, start page for all local browsers
INDEXHTML_DIR=$(datadir)/doc/indexhtml
indexhtml:
	for i in components/indexhtml/*.html components/indexhtml/*.css;do \
	  install -Dpm644 $$i $(INDEXHTML_DIR)/`basename $$i`; \
	done
	install -Dpm644 /dev/null $(INDEXHTML_DIR)/index.html
	cp -a components/indexhtml/images $(INDEXHTML_DIR)
	if [ -d components/indexhtml/fonts ]; then \
		cp -a components/indexhtml/fonts $(INDEXHTML_DIR); \
	fi
	install -Dpm644 components/indexhtml/indexhtml.desktop $(datadir)/applications/indexhtml.desktop

#bootsplash
# Nothing to do

#grub
grub-install:
	install -d -m 755  $(sysconfdir)/../boot/grub/themes/$(THEME)
	cp -a components/grub2/* $(sysconfdir)/../boot/grub/themes/$(THEME)/
	install -m 644 images/boot.png $(sysconfdir)/../boot/grub/themes/$(THEME)/boot.png


system-settings-install:
	mkdir -p $(datadir)/polkit-1/rules.d/
	cp -a system-settings/polkit-rules/*.rules $(datadir)/polkit-1/rules.d/
	install -Dm644 system-settings/lightdm-gtk-greeter.conf $(datadir)/install3/lightdm-gtk-greeter.conf
