import requests

def check(username):
    """
    Check if username exists on Parler
    """
    url = f"https://parler.com/user/{username}"
    try:
        response = requests.get(url, allow_redirects=False, timeout=5)
        found = response.status_code == 200
        return {
            "service": "Parler",
            "url": url,
            "found": found,
            "profile_data": {}
        }
    except Exception as e:
        return {
            "service": "Parler",
            "url": url,
            "found": False,
            "profile_data": {"error": str(e)}
        }
