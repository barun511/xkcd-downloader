try:
    import requests
    import urllib.request
    import sys
    import os
except ImportError:
    print("A base library was not found. Please be sure you are running this on python 3 (via the python3 command on Unix-like systems)")

# Directory where the xkcd files will be saved
directory = "xkcd-comics/"
print("Saving in xkcd-comics/ by default")
# Starting from 1
init_url = "http://xkcd.com/"
init_comic_number = 1
# Loop through all the comics
while init_comic_number < 5:
    r = requests.get(init_url + str(init_comic_number)) # Look at the http response of each comic
    if r.text.find("404") != -1: # This is a tricky one. I could have checked for the presence of 404, but that would have caused an issue if there was 404 in the alternate text or title of a comic. This was probably not the best check. TODO, fix this later.
        print("No comic found with link " + init_url + str(init_comic_number) + ". Download complete. Exiting ") 
        print(r.text)
    else:
        title_init = r.text.find('<title>') + len('<title>xkcd: ')
        title_end = r.text.find('</title>')
        title = r.text[title_init:title_end]
        pos = r.text.find('<div id="comic">') # This is where the comic exists in the HTML area.
        pos = pos + len('<div id="comic">\n<img src="')
        pos_end = r.text.find(' ',pos) - 1 # Find the next whitespace. The '-1' is to ignore the next quotation mark. 
        image_path = "http:" + r.text[pos:pos_end]
        print(init_comic_number)
        print(title)
        print(image_path)
        pos = pos_end + 2 + len('title="')
        pos_end = r.text.find('alt',pos) - 2
        alt_text = (r.text[pos:pos_end]).replace("&#39;","'") 
        print(alt_text)
        urllib.request.urlretrieve(image_path, directory + str(init_comic_number) + ' : ' + title + '\n' + alt_text)
    init_comic_number = init_comic_number + 1
