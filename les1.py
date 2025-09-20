import googlesearch

def search_google(query):
    """Search Google and return a list of URLs."""
    return list(googlesearch.search(query))

print(search_google("Children's books"))