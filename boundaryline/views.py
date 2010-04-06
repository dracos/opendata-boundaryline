from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404

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

