from django.core.management.base import LabelCommand
from django.contrib.gis.utils import LayerMapping
from boundaryline.models import Council

mapping = {
    'name': 'NAME',
    'area_code': 'AREA_CODE',
    'number': 'NUMBER',
    'unit_id': 'UNIT_ID',
    'code': 'CODE',
    'hectares': 'HECTARES',
    'area': 'AREA',
    'shape': 'MULTIPOLYGON',
}

class Command(LabelCommand):
    def handle_label(self,  filename, **options):
        lm = LayerMapping(Council, filename, mapping, transform=False, encoding='iso-8859-1')
        lm.save(fid_range=(36,46), strict=True, verbose=True)
        lm.save(fid_range=(508,509), strict=True, verbose=True)

