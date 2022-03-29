from driver import create_driver, get_page_source
from scraper import scrape_data
from data_handling import get_url_details, save_data_to_json
import time

data = {"products": []}  # stores the scraped data dictionary
countries, asin = get_url_details()

# creating driver

# looping through all the urls to scrape the data
start_time = time.time()
times_100_urls = []
for i, country in enumerate(countries):

    driver = create_driver()
    # getting the scraped data
    url = f"https://www.amazon.{country}/dp/{asin[i]}"
    html = get_page_source(driver, url)
    scraped_data = scrape_data(html, url)
    if scraped_data:
        data['products'].append(scraped_data)

    # getting the time for every 100 URLs
    if (i+1) % 100 == 0:
        end_time = time.time()
        times_100_urls.append(end_time - start_time)
        start_time = time.time()

    print(f"Finished URL no. {i+1}.")

# saving the scraped data to JSON file
save_data_to_json(data)

# printing the times for every 100 URLs
print("\n\n---------\n\n")
print("The times:\n\n")
for t in times_100_urls:
    print(t)
