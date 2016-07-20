try:
    import requests
    import urllib3
    import sys
    import os
except ImportError:
    print("A base library was not found. Please be sure you are running this on python 3 (via the python3 command on Unix-like systems)")

# Directory where the xkcd files will be saved
directory = "xkcd-comics/"
if sys.argv[1]=='':
    print("Saving in /xkcd-comics/ directory by default")
else:
    directory = str(sys.argv[1])
    print("Saving in " + directory)

# Starting from 1
init_url = "http://xkcd.com/"
init_comic_number = 1
# Loop through all the comics
while init_comic_number < 3:
    r = requests.get(init_url + str(init_comic_number)) # Look at the http response of each comic
    if r.text.find("404"): # This is a tricky one. I could have checked for the presence of 404, but that would have caused an issue if there was 404 in the alternate text or title of a comic. This was probably not the best check. TODO, fix this later.
        print("No comic found with link " + init_url + str(init_comic_number) + ". Download complete. Exiting ") 
        print(r.text)
    else:
        pos = r.text.find('<div id="comic">')
        print(pos)
    init_comic_number = init_comic_number + 1
