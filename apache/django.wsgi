#!/usr/local/bin/python

import os, sys

# Custom path for location of project - think this should work.
for path in (os.path.dirname(__file__), "/srv/boundaryline.dracos.vm.bytemark.co.uk/project", "/srv/boundaryline.dracos.vm.bytemark.co.uk"):
    if path not in sys.path:
        sys.path.insert(0, path)

import wsgi_monitor
wsgi_monitor.start(interval=1.0)
# wsgi_monitor.track(os.path.join(os.path.dirname(__file__), 'site.cf'))

os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
