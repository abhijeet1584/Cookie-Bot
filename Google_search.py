# =====================
# SEARCHING ON YOUTUBE
# =====================

from googlesearch import search

# Here I've used a trick
# we are basically utilizing Google's search optimization


# Google Search
def search_on_google(query):
    for result in search(query, tld='com', stop=1, pause=1):
        return result


# YouTube Search
def search_on_youtube(query):
    for result in search(query + 'YouTube', tld='com', stop=1,pause=1):
        return result
    # This will add "YouTube" at the end of the search
