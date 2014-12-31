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
	@echo "  html          to make standalone HTML files"
	@echo "  linkcheck     to check all external links for integrity"
	@echo "  rsync-eoas     to rsync HTML files to your EOAS web space"
	@echo "  rsync-shelob  to rsync HTML files from EOAS machine to EOAS web server"

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

rsync-eoas:
	rsync -rlpgoDvhz _build/html/ $(EOAS_HOST):$(EOAS_WEB)
	@echo "rsync to your $(EOAS_WEB) directory complete."

rsync-shelob:
	# This target can only be used from a machine on the EOAS network
	chmod -R g+w _build/html
	rsync -rltpDvh \
		--exclude bloomcast/spring_diatoms.html \
		--exclude _static/bloomcast/spring_diatoms/ \
		_build/html/ shelob:/www/salishsea/data/
	@echo "rsync to shelob web server complete."
