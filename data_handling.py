import csv
import json


def get_url_details():
    """Returns the URL details: 'country' and 'asin' as lists.

    Returns
    -------
    countries: list
               The list of the `country` to be placed in the URL.

    asin: list
          The list of the `asin` to be placed in the URL.
    """

    countries, asin = [], []
    # opening and reading from the csv file
    with open("url_details.csv", 'r') as csv_file:
        csv_values = csv.DictReader(csv_file)
        for row in csv_values:
            countries.append(row['country'])
            asin.append(row['Asin'])
    return countries, asin


def save_data_to_json(data):
    """Saves the given data in JSON."""

    with open("output.json", "w") as output_json:
        json.dump(data, output_json)


def load_data_from_json(filename):
    """Loads the data and returns it as a list from the given JSON file."""
    with open(filename, "r") as json_file:
        contents = json.load(json_file)

    return contents
