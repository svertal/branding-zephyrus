
install:
	install -d $(datadir)/alt-notes
	cp -a *.html $(datadir)/alt-notes
	for relnotes in release-notes.*.html; do \
		suffix="$${relnotes#release-notes.}"; \
		ln -s $$relnotes $(datadir)/alt-notes/livecd-finish.$$suffix; \
	done
