import os
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect
from midsem.functions.twitter_search import search as search_twitter
from midsem.functions.json_parser import fileParser
from midsem.functions.graphing import parseData

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

@method_decorator(csrf_exempt)
def search(request):
    if request.POST:
        filename = os.path.join(BASE_DIR, request.POST['term'] +'_search.json')
        search_twitter(request.POST['term'])
        data = fileParser(filename)
        print len(data)
        graph = parseData(data,filename)
        retweet_cdf_file = os.path.join(BASE_DIR, 'retweet_cdf.html')
        tweet_cdf_file = os.path.join(BASE_DIR, 'tweet_cdf.html')
        content = []
        with open(retweet_cdf_file) as f:
            content = f.readlines()
        retweet_cdf_html = ''
        for c in content:
            retweet_cdf_html += c+'\n'
        with open(tweet_cdf_file) as f:
            content = f.readlines()
        tweet_cdf_html = ''
        for c in content:
            tweet_cdf_html += c+'\n'
        return render_to_response('index.html', {
        'refresh_button': '<form action="/" method="post"><button type="submit" value="'+request.POST['term']+'" name="term">Refresh</button></form>',
        'result_retweet_cdf': retweet_cdf_html,
        'result_tweet_cdf': tweet_cdf_html})
    else:
        return render_to_response('index.html', RequestContext(request))
