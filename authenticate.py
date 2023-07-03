import requests

def authenticate_to_odoo(username, password):
    """
    This function authenticates to the Odoo ERP API.

    Args:
        username (str): The username for authentication.
        password (str): The password for authentication.

    Returns:
        str: The authentication token provided by the Odoo API.

    Raises:
        requests.exceptions.RequestException: If an error occurs while making the request.
    """
    odoo_auth = {
        'username': username,
        'password': password,
    }

    response = requests.post("https://odoo-erp-api.com/authenticate", json=odoo_auth)
    response.raise_for_status()
    return response.json()['token']