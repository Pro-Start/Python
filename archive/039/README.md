# 39 - Flights SMS

### Notes

#### APIs Required

- Google Sheet Data Management - [Sheety](https://sheety.co/)

- [Kiwi Partners Flight Search API](https://partners.kiwi.com/) (Free Signup, Requires Credit Card Details) 

- [Tequila Flight Search API](https://tequila.kiwi.com/portal/docs/tequila_api) Documentation 

- [Twilio SMS API](https://www.twilio.com/docs/sms) 

#### Program Requirements

- Use the Flight Search and Sheety API to populate your own copy of the Google Sheet with International Air Transport Association (IATA) codes for each city. Most of the cities in the sheet include multiple airports, you want the city code (not the airport code see here).

- Use the Flight Search API to check for the cheapest flights from tomorrow to 6 months later for all the cities in the Google Sheet.

- If the price is lower than the lowest price listed in the Google Sheet then send an SMS to your own number with the Twilio API.

- The SMS should include the departure airport IATA code, destination airport IATA code, departure city, destination city, flight price and flight dates. e.g

- Toggle these options when setting up with the API providers

- Avoid making too many unnecessary requests with the Sheety API while testing your code. The free tier for the Sheety API only allows 200 requests per month.

- Also, enable the PUT option so that you can write to your Google sheet

- Register with the Kiwi Partners Flight Search API

- Your account name should be the same as what you used later in "First name" and "Last name".

- There is no need to provide a credit card or billing information (you can skip that section) when you create your "Solution" (previously called "Application").

- When registering for your API key choose Meta Search as your product type.

- Then choose One-Way and Return.


### Materials

* [Python File](./039.py)


---

**[Home](../README.md)**