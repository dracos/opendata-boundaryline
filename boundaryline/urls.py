from django.conf.urls.defaults import *

urlpatterns = patterns('boundaryline.views',
    (r'^wkt(?:/(?P<snac>.*?))$', 'wkt'),
    (r'^brum$', 'brum'),
    (r'^(?:(?P<snac>.*?))$', 'home'),
)
