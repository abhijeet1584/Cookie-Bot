# =====================
# SEARCHING ON YOUTUBE
# =====================

from googlesearch import search

# Here I've used a trick
# When we search anything on Google, If we add YouTube at the end of it
# we are basically utilizing Google's searching power


# Google Search
def search_on_google(Keyword):
    query = Keyword
    
    for result in search(query, tld='com', stop=1, pause=1):
        return result


# YouTube Search
def search_on_youtube(Keyword):
    query = Keyword

    for result in search(query + 'YouTube', tld='com', stop=1,pause=1):
        return result
    # This will add "YouTube" at the end of the search
