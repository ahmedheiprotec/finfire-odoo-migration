import requests

def fetch_finfire_data():
    """
    This function fetches data from the Finfire ERP API.

    Returns:
        dict: The fetched data in JSON format.

    Raises:
        requests.exceptions.RequestException: If an error occurs while making the request.
    """
    try:
        response = requests.get("https://finfire.de/services/login/api/swagger/")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Error occurred while fetching Finfire data:", str(e))
        return None

# Test the function
data = fetch_finfire_data()
print(data)   