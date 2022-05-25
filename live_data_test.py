import urllib.parse
import requests
from bs4 import BeautifulSoup as BS
from datetime import datetime

url = "https://www.viagogo.com/secure/search?q={band}"

# generate query

while True:
    band_name = input("Enter Band Name: ")

    if band_name is "":
        print("Thanks for visiting! Goodbye")
        break

    band_name_url = urllib.parse.quote(band_name)   # convert to URL format
    access_url = url.format(band=band_name_url)     # access url to scrape

    res = requests.get(access_url)  # grabs full HTML of the URL above
    soup = BS(res.content, 'html.parser')  # turns full HTML into a BS object

    page_times = soup.find("time")  # grabs the first time

    # makes sure the query exists, if not, will ask you to try again
    try:
        page_times.has_attr('datetime')
    except AttributeError:
        print("No concerts for this band exist, try again")
        continue

    concert_datetime = page_times['datetime']
    concert_datetime = concert_datetime.replace('T', ' ')

    dt_obj = datetime.strptime(concert_datetime, '%Y-%m-%d %H:%M:%S')   # grabs the time in datetime string format
    print(dt_obj.strftime("The next concert date for {band} is on %A, %B %d, %Y "   # convert to more readable
                          "at %I:%M %p".format(band=band_name.title())))
    break
