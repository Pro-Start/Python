# 38 - Workout Tracking with Google Sheets

### Notes

#### `Step 1` - **Setup API Credentials and Google Spreadsheet**
1. Go to this [link](https://docs.google.com/spreadsheets/d/1DHL6Y8XAHSC_KhJsa9QMekwP8b4YheWZY_sxlH3i494/edit?usp=sharing) and create a copy of the My Workouts Spreadsheet. You may need to login/register.  e.g.: You can also create your own sheet if you like.

2. Go to the Nutritionix API [website](https://www.nutritionix.com/business/api) and select "Get Your API Key" to sign up for a free account. Double check your spam folder (and/or your gmail "promotions" tab) for the Nutritionix verification email.

3. Once logged in, you should be able to access your API key and App id:

4. Create a new project in PyCharm and in the main.py create 2 constants to store the APP_ID and API_KEY that you got from Nutritionix.


#### `Step 2` - **Get Exercise Stats with Natural Language Queries**
1. Using the Nutritionix "Natural Language for Exercise" API Documentation, figure out how to print the exercise stats for plain text input.

You can hard code the API key and the App Id for now. In step 6, we'll store the API key and app id as environment variables.

HINT 1:  Use what you have learnt about Authentication headers and the relevant part of the Nutritionix Authentication Documentation to authenticate your request.

HINT 2: Use what you have learnt about making POST requests and the relevant part of the Nutritionix Exercise Documentation to make your request with the required parameters.

#### `Step 3` - **Setup Your Google Sheet with Sheety**
1. Log into [Sheety](https://sheety.co/) with your Google Account (the same account that owns the Google Sheet you copied in step 1).

Make sure you give Sheety permission to access your Google sheets. If you miss this step, log out of Sheety and log in again.

Make sure the email matches between your Google Sheet and Sheety Account. e.g.

Under your Google Account Security settings, you should see that Sheety has access. Double-check that you see Sheety listed as an authorized app. Otherwise, your Python code can't access your spreadsheet.

2. In your project page, click on "New Project" and create a new project in Sheety with the name "Workout Tracking" and paste in the URL of your own "My Workouts" Google Sheet.

3. Click on the workouts API endpoint and enable GET and POST.

#### `Step 4` - **Saving Data into Google Sheets**
1. Using the Sheety [Documentation](https://sheety.co/docs/requests), write some code to use the Sheety API to generate a new row of data in your Google Sheet for each of the exercises that you get back from the Nutritionix API. The date and time columns should contain the current date and time from the Python datetime module.

HINT 1: Parameters have to be lower case. Also, pay special attention to this part in the documentation:

HINT 2: Remember you can generate text in title case by using the Python .title() method.

[w3schools](https://www.w3schools.com/python/ref_string_title.asp)

HINT 3: Remember you can format a datetime object using the .strftime() method.

[w3schools](https://www.w3schools.com/python/python_datetime.asp)

Debugging 🐞 Tip: If you're having any issues, double-check that you are logged in to Sheety with the same Google account that owns the spreadsheet you're trying to modify.

#### `Step 5` - **Authenticate Your Sheety API**
At the moment there is no authentication that's required to access your Sheety endpoint. That means anyone could read and write to your "My Workout" Google Sheet.

1. Add either "Basic Authentication" or "Bearer Token" to your Sheety endpoint to secure it.  You can hardcode the token in your code for now while you test your code. Once you're sure it works, we can add it to the environment variables in the next step.

What is Bearer authentication?

Bearer authentication (also known as token authentication) is an HTTP authentication scheme that involves security tokens. The name “Bearer authentication” basically means “give access to the bearer of this token.” The security token or “bearer token” is just a cryptic string. An example of a bearer token would be a string that could look something like this:

"AAAAAAAAAAAAAAAAAAAAAMLheAAAAAAA0%2BuSeid%2BULvsea4JtiGRiSDSJSI%3DEUifiRBkKG5E2XzMDjRfl76ZC9Ub0wnz4XsNiRVBChTYbJcE3F"

The idea is that whoever has the secret token, has permission to interact with the spreadsheet. A client - like your browser or mobile app - would then send this security token in the Authorization header when making requests to Sheety's server.


2. Using the Sheety documentation on authentication to update your Python code to authenticate your request.

HINT: You'll need to read the relevant section on the request module documentation to do this.

Basic Authentication: [requests](https://requests.readthedocs.io/en/master/user/authentication/#basic-authentication) 

Bearer Authentication: [stackoverflow](https://stackoverflow.com/questions/29931671/making-an-api-call-in-python-with-an-api-that-requires-a-bearer-token) 



### Materials

* [Python File](./038.py)

# Resources

* [Pixela](https://pixe.la/) & [Docs](https://docs.pixe.la/)

---

**[Home](../README.md)**