from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect


@method_decorator(csrf_exempt)
def search(request):
    if request.POST:
        return render_to_response('index.html', {
        'refresh_button': '<form action="/" method="post"><button type="submit" value="'+request.POST['term']+'" name="term">Refresh</button></form>',
        'result': request.POST['term']})
    else:
        return render_to_response('index.html', RequestContext(request))
