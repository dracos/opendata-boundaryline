from django.conf.urls import patterns

urlpatterns = patterns('boundaryline.views',
    (r'^wkt(?:/(?P<snac>.*?))$', 'wkt'),
    (r'^(?P<easting>\d+),(?P<northing>\d+)$', 'point'),
    (r'^brum$', 'brum'),
    (r'^(?:(?P<snac>.*?))$', 'home'),
)
