from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404

from models import Council

def home(request, snac):
    snac = snac or '00CN'
    try:
        c = Council.objects.get(code=snac)
    except:
        raise Http404
    return render_to_response('base.html', {
        'council': c,
    })

def wkt(request, snac='00CN'):
    try:
        c = Council.objects.get(code=snac)
    except:
        raise Http404
    c.shape.transform(900913)
    return HttpResponse(c.shape.wkt, content_type='text/plain')

