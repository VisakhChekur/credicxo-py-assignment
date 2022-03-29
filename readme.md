# Problem Statement

The aim is to scrape product details from an Amazon webpage of the following pattern: "https://www.amazon.{country}/dp/{asin}". The product deatils that were scraped were:
- product title
- product price
- product image URL
- product details

# Approach

I used a combination of `selenium` and `BeautifulSoup4` to get the HTML code of the page and to parse it for the necessary information. 

NOTE: Ideally, a single selenium driver would be used for all the URLs, but in this specific case a driver would be created and closed for each URL. This increased the runtime. The reason for doing it in this less optimal way was that an application on my laptop, Cold Turkey, was interfering with the driver's access to Chrome after it was kept open for a minute or so.

## Steps
1. Create a selenium driver
2. Get the HTML of the URL
3. Make soup using `BeautifulSoup4`
4. Parse the soup for the appropriate element using the IDs or classes of the needed element.
5. Grab the text, which is the necessary information, from the element and save it accordingly.
6. Once the data from all the URLs are scraped, save the data to a JSON file.
7. The data, from the JSON file, was then uploaded to a PostgreSQL database using the `psycopg2` module.

Steps 1 - 6 are executed in `main.py` while step 7 (adding to database) is executed in `db.py`.

# BONUS: Bypass Amazon Captcha

I was not able to write a script to bypass the captcha, but the simplified general approach to do so would be as follows. First, I would have to train a model to solve the captchas using some deep learning algorithm. Then this model could be used in the script to solve the captcha everytime it is seen.
