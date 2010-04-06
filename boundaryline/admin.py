from django.contrib.gis import admin
from models import Council

admin.site.register(Council, admin.OSMGeoAdmin)
