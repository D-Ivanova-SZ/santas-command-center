"""
API Helper Module
Contains helper function for making HTTP requests to external API services.
"""

import requests
from typing import Dict, Any, Optional


def get_json(url: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Makes an HTTP GET request and returns JSON data.

    Args:
        url (str): The URL of the API endpoint
        params (Optional[Dict[str, Any]]): Query parameters for the request (default None)

    Returns:
        Dict[str, Any]: Dictionary containing the data from the API

    Raises:
        requests.exceptions.Timeout: When the request takes too long
        requests.exceptions.ConnectionError: When there's no internet connection
        requests.exceptions.HTTPError: When the server returns an error (4xx or 5xx)
        requests.exceptions.RequestException: For any other network errors
        ValueError: When the response is not valid JSON
    """
    try:
        # Make GET request with 10 second timeout
        # timeout prevents indefinite waiting
        response = requests.get(url, params=params, timeout=10)
        print()

        # Check HTTP status code
        # raise_for_status() throws an exception for 4xx and 5xx errors
        response.raise_for_status()

        # Try to parse JSON response
        return response.json()

    except requests.exceptions.Timeout:
        # Request took more than 10 seconds
        raise requests.exceptions.Timeout(
            "Request timed out. The server took too long to respond."
        )

    except requests.exceptions.ConnectionError:
        # No internet connection or server is unreachable
        raise requests.exceptions.ConnectionError(
            "Failed to connect. Please check your internet connection."
        )

    except requests.exceptions.HTTPError as e:
        # Server returned a 4xx or 5xx error
        status_code = e.response.status_code
        raise requests.exceptions.HTTPError(
            f"HTTP error {status_code}: {e.response.reason}"
        )

    except ValueError:
        # Response is not valid JSON
        raise ValueError("Invalid JSON response received from server.")

    except requests.exceptions.RequestException as e:
        # Any other network errors
        raise requests.exceptions.RequestException(
            f"An error occurred while making the request: {str(e)}"
        )