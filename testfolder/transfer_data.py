import requests

def transfer_data_to_odoo(data, odoo_token):
    """
    This function transfers data to the Odoo ERP API.

    Args:
        data (list): The data to be transferred.
        odoo_token (str): The authentication token for accessing the Odoo API.

    Raises:
        requests.exceptions.HTTPError: If an error occurs during the data transfer.
    """
    for record in data:
        try:
            response = requests.post("https://odoo-erp-api.com/data", json=record, headers={'Authorization': odoo_token})
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print(f"Failed to transfer data. Error: {str(e)}")
        else:
            print("Data transferred successfully.")