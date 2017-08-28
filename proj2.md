# bee-project
Backend Engineer Project

## Scenario
A returning user asks the bot (working on behalf of the realtor) if there are any homes in a certain area code that he or she would be interested in and provides the realtor with a phone number where they can be reached to follow up. For instance, the query may be:

```
username: KHR10403
Hey, it's Zer - are there any homes in 10101 that we might want to look at? My phone's dying but you can reach me at 555-555-5555. Thanks, see you this weekend
```

The job of the bot in this scenario is to extract the zipcode, username, and phone-number from messages like this, find the users preferences in the user database, and find homes that fit the users previously given criteria in the zipcode extracted from the message.

## Goals: Extract, Retrieve, Filter, Report
Build a python tool(?) that will 
- extract the username (which will always be the first line of the message and will be in the format `username: ......`)
- Check if the message contains a phone number. If the message contains a phone number, extract it and add it to the user's data object
- Check if the message contains a zipcode. If the message contains a zipcode extract it 

If you extract a zipcode from the message, perfrom a public records search to retrieve houses in the zipcode which fit the parameters the user has previously given (as found in the users database, which we will provide).
Public searches can be performed using the [Retsly API](https://rets.ly/docs/platform.html). You may use our key (`RETSLY KEY VALUE`).

The tool you build should return a list of properties from Retsly and a dictionary of extracted elements (see the examples section at the end for reference).


## Resources
### `users.db`
A small mongo database(dataset?) containing a small set of users and their known preferences. A brief description of the fields in this database(dataset?):
-  `username`: the client's unique ID as found in the first line of every message. A character string containing letters and numbers (i.e., `KJV1020`, `14RR`)
-  `BEDS`: the exact number of bedrooms the client is interested in (integer values; may be `NA`)
-  `BATHS`: the exact number of bathrooms the client is interested in (decimal values; may include quarters, halfs, and three quarters; may be `NA`)
-  `LIVE-MIN`: the minimum approximate living area the client is interested in (integer values; may be `NA`)
-  `LIVE-MAX`: the maximum approximate living area the client is interested in (integer values; may be `NA`)

The only field that is guaranteed to exist is username. Here is the data for the first 5 users:

```
username, BEDS, BATHS, LIVE-MIN, LIVE-MAX
KHV1020,     3,      ,         , 
   14RR,      ,      ,         , 
FH14432,      ,      ,         , 
   MDMD,     1,     2,     1200,     1500
GH12345,      ,      ,         ,         
```

### Example Inputs and Returns

```
username: KHV1020
I am looking at houses in 50014 online and I think there may be some that look pretty good. Give me a call when you can at 904-212-2020
```

```
username: MDMD
My phone number is 233-9030 and I'm looking in 32225
```

```
username: KHV1020
Do you think it would be worth it to look at houses in 50014?
```

```
username: GH12345
Call me when you get a chance: 555-5555
```

```
username: GH12345
Call me when you get a chance: 434
```
