# Live Data TEst
# 
# # 
## Interview test
Write code that takes name of active band and returns the next concert date.

There are APIs available for Google Search Results, or Ticketmaster, or many other ticketing sites, but they are not free.
This is a simple tool that will search a small ticket site and return the first date if there is a result. There will be no
result if there is no tour for whatever the query may be. Either the band doens't exist, or they aren't touring. As I said,
it is a simple implementation.

STEPS:

Install required packages by running "pip install -r requirements.txt" from terminal<br>
Run live_data_test.py

**Existing Band Touring**<br>
When prompted **Enter Band Name:**, type in "the cure" and hit *enter* key<br>
Program will return with the first tour date of 10/6/22 in readable format

**Existing Band Touring #2**<br>
When prompted **Enter Band Name:**, type in "imagine dragons" and hit *enter*<br>
Program will return with the first tour date of 06/01/22 readable format

**Non-existing Band**<br>
When prompted **Enter Band Name:**, type in "scooby" and hit 'enter'<br>
Program will return **No concerts for this band exist, try again**<br>
Program will prompt **Enter Band Name:** again<br>
Enter nothing into prompt and hit *enter* key<br>
Program will return **Thanks for visiting! Goodbye**