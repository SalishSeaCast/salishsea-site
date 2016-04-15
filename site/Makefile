# Makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
BUILDDIR      = _build

# User-friendly check for sphinx-build
ifeq ($(shell which $(SPHINXBUILD) >/dev/null 2>&1; echo $$?), 1)
$(error The '$(SPHINXBUILD)' command was not found. Make sure you have Sphinx installed, then set the SPHINXBUILD environment variable to point to the full path of the '$(SPHINXBUILD)' executable. Alternatively you can add the directory with the executable to your PATH. If you don't have Sphinx installed, grab it from http://sphinx-doc.org/)
endif

# Internal variables.
ALLSPHINXOPTS = -d $(BUILDDIR)/doctrees $(SPHINXOPTS) .
EOAS_HOST = sable
EOAS_WEB = public_html/salishsea-site/

.PHONY: help clean html linkcheck

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  html       to make standalone HTML files"
	@echo "  linkcheck  to check all external links for integrity"
	@echo "  rsync      to rsync HTML files to /var/www/html/"

clean:
	rm -rf $(BUILDDIR)/*

html:
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html."

linkcheck:
	$(SPHINXBUILD) -b linkcheck $(ALLSPHINXOPTS) $(BUILDDIR)/linkcheck
	@echo
	@echo "Link check complete; look for any errors in the above output " \
	      "or in $(BUILDDIR)/linkcheck/output.txt."

rsync:
	# This target is typically only used on skookum
	# (where the site is served from).

	chmod -R g+w _build/html
	rsync -rltpDvh \
		--exclude bloomcast/spring_diatoms.html \
		--exclude _static/bloomcast/spring_diatoms/ \
		--exclude nemo/results/ \
		--exclude storm-surge/forecast.html \
		--exclude _static/nemo/results_figures/nowcast/ \
		--exclude _static/nemo/results_figures/forecast/ \
		--exclude _static/nemo/results_figures/forecast2/ \
		--exclude _static/storm-surge/ \
		_build/html/ /vasr/www/html/
	@echo "rsync to /var/www/html/ complete."
