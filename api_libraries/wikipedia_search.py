import wikipedia
from multiprocessing.pool import ThreadPool
import concurrent.futures

# Search on Wikipedia
# This will return a list of search results
def wiki_search (query):
    def search(query):
        # Creating a new Thread
        search_result = wikipedia.search(query)
        return search_result[0:4]

    pool = ThreadPool(processes=1)
    result = pool.apply_async(search, (query))
    return result[0:4]

# Return one line summary of the search term
def wiki_summary_short (query):
    def summary(query):
        summary = wikipedia.summary(query)
        return summary[0:summary.find('.')]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(summary, query)
        return_value = future.result()
        return return_value

# Return the full summary of the search term
def wiki_summary (query):
    summary = wikipedia.summary(query)
    return summary

# Returns the full page handler, This can be used to print the whole content of the wikipedia page or gather links and images from the wikipedia page
def wiki_full_page (query):
    def handler (query):
        handler = wikipedia.page(query)
        return handler;

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(handler, query)
        result = future.result()
        return result
