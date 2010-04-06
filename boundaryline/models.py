from django.contrib.gis.db import models

class Council(models.Model):
    name = models.CharField(max_length=60)
    area_code = models.CharField(max_length=3)
    number = models.IntegerField()
    unit_id = models.IntegerField()
    code = models.CharField(max_length=7)
    hectares = models.IntegerField()
    area = models.IntegerField()

    shape = models.MultiPolygonField(srid=27700)
    objects = models.GeoManager()

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name

