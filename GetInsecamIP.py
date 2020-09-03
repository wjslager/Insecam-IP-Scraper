# Insecam IP Scraper. 
# Discord: L3#0001

from urllib.request import urlopen, Request
import urllib.request
import re

# File to write to
filename = "new-on-insecam.txt"
# Regex to search for IP
# only scrape specific URL's
regex = re.compile(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})/mjpg/video.mjpg")

# HTTP Error 403: Forbidden without User Agent info. Add fake browser visit data. 
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) ' 
                      'AppleWebKit/537.11 (KHTML, like Gecko) '
                      'Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}

f = open(filename, "a")

# For each page 1 to x-1 
for i in range(1,999):
    # Change URL in " " to anything on www.insecam.org
    #reg_url = f"http://www.insecam.org/en/bytype/Defeway/?page={i}"
    reg_url = f"http://insecam.org/en/bynew/?page={i}"
    # Perform HTML Request
    req = Request(url=reg_url, headers=headers) 
    # Get HTML Source

    with urllib.request.urlopen(req) as response: 
        html = response.read().decode('utf-8')
    #print(html)

    # Perform regex on HTML Source to get IPs
    list = re.findall(regex, html)
    if list: 
        for ip, port in list:
            print("http://" + ip + ":" + port + "/mjpg/video.mjpg")
            f.write("http://" + ip + ":" + port +"/mjpg/video.mjpg\n")
    else:
        print("No IP Found on page " + str(i))

f.close()