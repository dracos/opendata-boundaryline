from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404
from django.contrib.gis.geos import Point

from models import Council

def home(request, snac):
    snac = snac or '00CN'
    try:
        c = Council.objects.get(code=snac)
    except:
        raise Http404
    return render_to_response('council.html', {
        'council': c,
    })

def brum(request):
    consts = Council.objects.filter(code='999999').exclude(name='Greater London Authority')
    if request.GET.get('wkt'):
        out = []
        for c in consts:
            c.shape.transform(900913)
            out.append(c.shape.wkt)
        out = 'GEOMETRYCOLLECTION(' + ','.join(out) + ')'
        return HttpResponse(out, content_type='text/plain')
    return render_to_response('brum.html', {
        'consts': consts,
    })

def wkt(request, snac='00CN'):
    try:
        c = Council.objects.get(code=snac)
    except:
        raise Http404
    c.shape.transform(900913)
    return HttpResponse(c.shape.wkt, content_type='text/plain')

def point(request, easting, northing):
    point = Point(int(easting), int(northing), srid=27700)
    c = Council.objects.filter(shape__contains=point).exclude(code='999999')
    if not c:
        raise Http404
    return render_to_response('council.html', {
        'council': c[0],
    })

