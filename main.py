import requests

from fetch_data import fetch_finfire_data
from transform_data import transform_data
from authenticate import authenticate_to_odoo
from transfer_data import transfer_data_to_odoo

# Example usage
try:
    finfire_data = fetch_finfire_data()
    if finfire_data is not None:
        transformed_data = transform_data(finfire_data)
        odoo_token = authenticate_to_odoo('your_username', 'your_password')
        transfer_data_to_odoo(transformed_data, odoo_token)
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")