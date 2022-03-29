from bs4 import BeautifulSoup


def scrape_data(html, url):
    """Scrapes the data."""
    # making the soup
    soup = BeautifulSoup(html, 'lxml')

    if not html:
        return None
    if is_error_404(soup, url):
        return None

    scraped_data = {
        "url": url,
        "prdct_title": get_product_title(soup),
        "price": get_price(soup),
        "img_link": get_img_link(soup),
        "prdct_details": get_prdct_details(soup)
    }
    return scraped_data


def get_product_title(soup):
    """Returns the product title."""

    product_title_element = soup.find('span', id="productTitle")
    if product_title_element:
        return product_title_element.text.strip()
    return None


def get_price(soup):
    """Returns the price of the product."""

    price_element = soup.find('span', id="price")
    if price_element:
        return price_element.text.strip()
    return None


def get_img_link(soup):
    """Returns the product image link."""

    img_element = soup.find('img', id="imgBlkFront")
    if img_element:
        return img_element['src']
    return None


def get_prdct_details(soup):
    """Returns the product details as a string with each detail being separated by a comma (,)."""

    prdct_details_element = soup.find('div', id="detailBullets_feature_div")
    if not prdct_details_element:
        return None
    return parse_prdct_details(prdct_details_element.find_all('li'))


def parse_prdct_details(items):
    """Parses the product details into a list from the list of the product details."""
    
    prdct_details = []
    for item in items:
        span_elements = item.find_all('span', class_="a-list-item")
        for span in span_elements:
            # cleaning the product details to get rid of whitespace and newlines
            details = span.text.split("\n")
            details = details[0].strip() + " : " + details[-1].strip()
        prdct_details.append(details)
    return ', '.join(prdct_details)


def is_error_404(soup, url):
    """Checks if the response status code is 404. Returns True if it's 404."""

    error_element = soup.find('a', href="/ref=cs_404_logo/")
    if error_element:
        print(f"{url} is not available")
        return True
    return False
