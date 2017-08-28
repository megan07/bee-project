# bee-project
Backend Engineer Project

## Scenario
A returning user asks the bot (working on behalf of the realtor) if there are any homes in a certain area code that he or she would be interested in and provides the realtor with a phone number where they can be reached to follow up. For instance, the query may be:
```
username: KHR10403
Hey, it's Zer - are there any homes in 10101 that we might want to look at? My phone's dying but you can reach me at 555-555-5555. Thanks, see you this weekend
```
The job of the bot in this scenario is to extract the zipcode, username, and contact information, use the extract the zipcode and phone-number from messages like this, find the users preferences in the user database, and check homes in the zipcode that fit the user's previous criteria.

## Goals: Extract, Retrieve, Update, Filter, Report
Build a python tool(?) that will 
- extract the username (which will always be the first line of the message and will be in the format `username: ......`)
- Check if the message contains a phone number. If the message contains a phone number, extract it and add it to the user's data object
- Check if the message contains a zipcode. If the message contains a zipcode 
   - extract it 
   - perform a public records search that retrieves houses in the zipcode using the [Retsly API](https://rets.ly/docs/platform.html)
   - filter the results based on the users previously know preferences

## Resources
### `users.db`
A small mongo database(dataset?) containing a small set of users and their known preferences. A brief description of the fields in this database(dataset?):
-  `username`: the client's unique ID as found in the first line of every message. A character string containing letters and numbers (i.e., `KJV1020`, `14RR`)
-  `BEDS`: the exact number of bedrooms the client is interested in (integer values; is always `NA` if either `BEDS-MIN` or `BEDS-MAX` exists)
-  `BEDS-MIN`: the minimum number of bedrooms the client is interested in (integer values; is always `NA` if `BEDS` is known)
-  `BEDS-MAX`: the maximum number of bedrooms the client is interested in (integer values; is always `NA` if `BEDS` is known))
-  `BATHS`: the exact number of bathrooms the client is interested in (decimal values; may include quarters, halfs, and three quarters; is always `NA` if either `BATHS-MIN` or `BATHS-MAX` is known)
-  `BATHS-MIN`: the minimum number of bathrooms the client is interested in (decimal values; may include quarters, halfs, and three quarters; is always `NA` if `BATHS` is known)
-  `BATHS-MAX`: the maximum number of bathrooms the client is interested in (decimal values; may include quarters, halfs, and three quarters; is always `NA` if `BATHS` is known)
-  `LIVE`: the approximate living area the client is interested in (integer values; is always `NA` if either `LIVE-MIN` or `LIVE-MAX` is known)
-  `LIVE-MIN`: the minimum approximate living area the client is interested in (integer values; is always `NA` if either `LIVE` is known)
-  `LIVE-MAX`: the maximum approximate living area the client is interested in (integer values; is always `NA` if either `LIVE` is known)

The only field that is guaranteed to exist is username. Here is the data for the first 5 users:
```
username, BEDS, BEDS-MIN, BEDS-MAX, BATHS, BATHS-MIN, BATHS-MAX,  LIVE, LIVE-MIN, LIVE-MAX
KHV1020,     3,         ,         ,      ,          ,          ,      ,         , 
   14RR,      ,        2,        3,      ,       1.5,       2.5,  3000,         , 
FH14432,      ,        4,         ,      ,       3.5,          ,  6500,         , 
   MDMD,     1,         ,         ,     2,          ,          ,      ,     1200,     1500
GH12345,      ,         ,         ,      ,          ,          ,      ,         ,         
```

### Some example messages and the target extraction
```
username: KHV1020
I am looking at houses in 50014 online and I think there may be some that look pretty good. Give me a call when you can at 904-212-2020

username: MDMD
My phone number is 233-9030 and I'm looking in 32225

username: KHV1020
Do you think it would be worth it to look at houses in 50014?

username: GH12345
Call me when you get a chance: 555-5555

username: GH12345
Call me when you get a chance: 434
```
*Note*: in the last message, only the username nothing should be extracted since `434` isn't a valid phone number
