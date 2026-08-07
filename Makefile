SHELL = /bin/sh
INSTALL = install -c
MKDIR = install -d 

destdir = $(WSGIDIR)/wsgi-scripts

srcdir = .

SRC =  	csv_gen.py templates_filters.py web_s2n.wsgi

VIEWS = views/layout.tpl \
	views/make_apf_form.tpl \
	views/make_deimos_form.tpl \
	views/make_hires_form.tpl \
	views/make_kast_form.tpl \
	views/make_lris_form.tpl 

CSS = views/css/bootstrap-responsive.min.css \
	views/css/bootstrap.min.css \
	views/css/busy.css 

JS = views/javascript/bootstrap.min.js \
	views/javascript/doublespec_plot.js \
	views/javascript/highcharts.js \
	views/javascript/jquery-1.12.4.min.js \
	views/javascript/jquery.dataTables.min.js

install: install_src install_views install_css install_javascript

install_src:
	$(MKDIR) $(destdir)
	$(INSTALL) $(SRC) $(destdir)

install_views:
	$(MKDIR) $(destdir)/views
	$(INSTALL) $(VIEWS) $(destdir)/views

install_css:
	$(MKDIR) $(destdir)/views/css
	$(INSTALL) $(CSS) $(destdir)/views/css

install_javascript:
	$(MKDIR) $(destdir)/views/javascript
	$(INSTALL) $(JS) $(destdir)/views/javascript
