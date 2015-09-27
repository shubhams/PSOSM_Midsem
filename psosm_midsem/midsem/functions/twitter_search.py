__author__ = 'shiv'

import twitter

consumer_key = '8N95FKR6I1Szb8E3UOVTaPCOA'
consumer_secret = 'MexOWPpC2wmyhT0miVseiT0FmuXMG5Og4uNFI318wJ61UcEUF2'
access_token = '3312125714-8HNXirtXDszT8HTiQnT6GuAfIOOr8YSQZMjHJ5G'
access_token_secret = '5yYjHkbwgoseK5i6012KJYMZQ0Y5EewuC9ECTvQpgeD2O'

api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token,
                  access_token_secret=access_token_secret)

def search(term):
    search_results = []
    results = api.GetSearch(term=term, count=100)
    for result in results:
        search_results.append(result.AsJsonString())

    filename = term+'_search.json'
    fw = open(filename, "w")
    for i in range(0, len(search_results), 1):
        fw.write(search_results[i])
        if i != len(search_results)-1:
            fw.write("\n")
    print "Stored data to "+filename
    return search_results
