# 33 - API

### Topics Covered

* APIs

* Making HTTP Requests with the Requests module

* Sending Parameters with the Request

### Notes

* Types of responses - 
  * **1XX** - Hold on
  * **2XX** - Success
  * **3XX** - Go Away
  * **4XX** - You screwed up
  * **5XX** - I screwed up


### Syntax

* Basic `Request`
```python
import requests

response = requests.get(url="https://api.github.com/users/pratikkabade")

data = response.json()

print(data)
```

* Advanced `Request`
```python
SUNSET_URL = "https://api.sunrise-sunset.org/json"

MY_LAT = 36.7201600
MY_LONG = -4.4203400

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
}
response = requests.get(SUNSET_URL, params=parameters)
```

### Materials

* [Python File](./033.py)


### Resources

* [HTTP Status Codes Glossary](http://httpstatuses.com/)

---

**[Home](../README.md)**