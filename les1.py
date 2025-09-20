import google

print(google.__version__)
search = google.search("Python programming", num=5, stop=5, pause=2.0)
for result in search:
    print(result)