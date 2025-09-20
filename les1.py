import googlesearch

def search_google(query, num_results=10):
    """Search Google and return a list of URLs."""
    return list(googlesearch.search(query))

print(search_google("OpenAI", num_results=5))