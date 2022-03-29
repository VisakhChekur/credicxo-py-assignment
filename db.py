"""Saves the details of the products from the `output.json` file to a Postgres DB."""

from json import load
import os
import psycopg2
from data_handling import load_data_from_json


def insert_to_products_table(prdct_data):

    # creating the connection
    conn = psycopg2.connect(
        user="postgres",
        password=os.environ.get("POSTGRES_DB_PWD"),
        database="postgres",
    )

    # creating the cursor
    cur = conn.cursor()
    sql = """INSERT INTO products (title, price, product_details, image_link, product_url)
    VALUES (%(prdct_title)s, %(price)s, %(prdct_details)s, %(img_link)s, %(url)s)"""

    # inserting the details to the table
    for data in prdct_data:
        cur.execute(sql, data)

    # closing the cursor
    cur.close()
    # commiting the changes
    conn.commit()
    # closing the connection
    conn.close()


def main():

    prdct_data = load_data_from_json("output.json")
    prdct_data = prdct_data['products']
    insert_to_products_table(prdct_data)


if __name__ == "__main__":
    main()
