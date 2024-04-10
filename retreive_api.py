import requests
import mysql.connector
from datetime import datetime


def format_datetime(datetime_str):
    return datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%d %H:%M:%S")


# Function to fetch orders from API
def fetch_orders_from_api():
    url = "http://127.0.0.1:8000/api/orders/"  # Replace 'API_URL_HERE' with the actual API URL
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data from API:", response.status_code)
        return None


# Function to fetch orderitem from API
def fetch_orderitem_from_api():
    url = "http://127.0.0.1:8000/api/orderitem/"  # Replace 'API_URL_HERE' with the actual API URL
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data from API:", response.status_code)
        return None


# Function to fetch orderitem from API
def fetch_customerdata_from_api():
    url = "http://127.0.0.1:8000/api/customerdata/"  # Replace 'API_URL_HERE' with the actual API URL
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data from API:", response.status_code)
        return None


# Function to fetch orderitem from API
def fetch_deliverdata_from_api():
    url = "http://127.0.0.1:8000/api/deliverdata/"  # Replace 'API_URL_HERE' with the actual API URL
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data from API:", response.status_code)
        return None


# Function to insert data into MySQL table
def insert_orders_into_mysql(data):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="cake_api",
            port="3306"
        )
        cursor = connection.cursor()

        # Define MySQL query to insert data into table
        insert_query = """
            INSERT INTO orders (id, created_on, price, is_paid, is_shipped)
            VALUES (%s, %s, %s, %s, %s)
        """

        # Iterate over data and insert each record into the table
        for record in data:
            id = record["id"]
            created_on = format_datetime(record["created_on"])
            price = record["price"]
            is_paid = record["is_paid"]
            is_shipped = record["is_shipped"]

            # Check if the record already exists in the table
            cursor.execute("SELECT id FROM orders WHERE id = %s", (id,))
            existing_record = cursor.fetchone()

            # If the record doesn't exist, insert it into the table
            if not existing_record:
                cursor.execute(insert_query, (id, created_on, price, is_paid, is_shipped))
                connection.commit()

        print("Data inserted successfully into MySQL table")
        cursor.close()
        connection.close()
    except mysql.connector.Error as error:
        print("Failed to insert data into MySQL table:", error)


# Function to insert orderitem into MySQL table
def insert_orderitem_into_mysql(data1):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="cake_api",
            port="3306"
        )
        cursor = connection.cursor()

        # Define MySQL query to insert data into table
        insert_query = """
            INSERT INTO orderitem (id, quantity, order_id, name_id)
            VALUES (%s, %s, %s, %s)
        """

        # Iterate over data and insert each record into the table
        for record in data1:
            id = record["id"]
            quantity = record['quantity']
            order = record['order']
            name = record['name']

            # Check if the record already exists in the table
            cursor.execute("SELECT id FROM orderitem WHERE id = %s", (id,))
            existing_record = cursor.fetchone()

            # If the record doesn't exist, insert it into the table
            if not existing_record:
                cursor.execute(insert_query, (id, quantity, order, name))
                connection.commit()
        print("Data inserted successfully into MySQL table")
        cursor.close()
        connection.close()
    except mysql.connector.Error as error:
        print("Failed to insert data into MySQL table:", error)


# Function to insert orderitem into MySQL table
def insert_customerdata_into_mysql(data2):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="cake_api",
            port="3306"
        )
        cursor = connection.cursor()

        # Define MySQL query to insert data into table
        insert_query = """
            INSERT INTO customerdata (id, deliver_date, deliver_time, cake_text, phone, order_id, zip_code, state, city, street, email, name)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        # Iterate over data and insert each record into the table
        for record in data2:
            id = record["id"]
            deliver_date = record['deliver_date']
            deliver_time = record['deliver_time']
            cake_text = record['cake_text']
            phone = record['phone']
            order = record['order']
            zip_code = record['zip_code']
            state = record['state']
            city = record['city']
            street = record['street']
            email = record['email']
            name = record['name']

            # Check if the record already exists in the table
            cursor.execute("SELECT id FROM customerdata WHERE id = %s", (id,))
            existing_record = cursor.fetchone()

            # If the record doesn't exist, insert it into the table
            if not existing_record:
                cursor.execute(insert_query, (id, deliver_date, deliver_time, cake_text, phone, order, zip_code, state, city, street, email, name))
                connection.commit()
        print("Data inserted successfully into MySQL table")
        cursor.close()
        connection.close()
    except mysql.connector.Error as error:
        print("Failed to insert data into MySQL table:", error)


# Function to insert orderitem into MySQL table
def insert_deliverdata_into_mysql(data3):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="cake_api",
            port="3306"
        )
        cursor = connection.cursor()

        # Define MySQL query to insert data into table
        insert_query = """
            INSERT INTO deliverdata (id, deliver_phone, order_id, deliver_zip_code, deliver_state, deliver_city, deliver_street, deliver_email, deliver_name)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        # Iterate over data and insert each record into the table
        for record in data3:
            id = record["id"]
            deliver_phone = record['deliver_phone']
            order = record['order']
            deliver_zip_code = record['deliver_zip_code']
            deliver_state = record['deliver_state']
            deliver_city = record['deliver_city']
            deliver_street = record['deliver_street']
            deliver_email = record['deliver_email']
            deliver_name = record['deliver_name']

            # Check if the record already exists in the table
            cursor.execute("SELECT id FROM deliverdata WHERE id = %s", (id,))
            existing_record = cursor.fetchone()

            # If the record doesn't exist, insert it into the table
            if not existing_record:
                cursor.execute(insert_query, (id, deliver_phone, order, deliver_zip_code, deliver_state, deliver_city, deliver_street, deliver_email, deliver_name))
                connection.commit()
        print("Data inserted successfully into MySQL table")
        cursor.close()
        connection.close()
    except mysql.connector.Error as error:
        print("Failed to insert data into MySQL table:", error)


# Main function
def main():
    # Fetch orders from API
    data = fetch_orders_from_api()
    if data:
        # Insert data into MySQL table
        insert_orders_into_mysql(data)

    # Fetch orderitems from API
    data1 = fetch_orderitem_from_api()
    if data1:
        insert_orderitem_into_mysql(data1)

    # Fetch orderitems from API
    data2 = fetch_customerdata_from_api()
    if data2:
        insert_customerdata_into_mysql(data2)

    # Fetch orderitems from API
    data3 = fetch_deliverdata_from_api()
    if data3:
        insert_deliverdata_into_mysql(data3)


if __name__ == "__main__":
    main()
