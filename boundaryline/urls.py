from django.conf.urls.defaults import *

urlpatterns = patterns('boundaryline.views',
    (r'^wkt(?:/(?P<snac>.*?))$', 'wkt'),
    (r'^(?:(?P<snac>.*?))$', 'home'),
)
