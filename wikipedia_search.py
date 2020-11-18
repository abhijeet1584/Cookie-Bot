import wikipedia

# Search on Wikipedia
# This will return a list of search results
def wiki_search (query):
    search_result = wikipedia.search(query)
    return search_result[0:4]

# Return one line summary of the search term
def wiki_summary_short (query):
    summary = wikipedia.summary(query)
    return summary[0:summary.find('.')]

# Return the full summary of the search term
def wiki_summary (query):
    summary = wikipedia.summary(query)
    return summary

# Returns the full page handler, This can be used to print the whole content of the wikipedia page or gather links and images from the wikipedia page
def wiki_full_page (query):
    handler = wikipedia.page(query)
    return handler;
