import requests

def check(username):
    """
    Check if username/name exists on WhitePages
    Note: WhitePages primarily searches by name and phone number, not username
    """
    url = f"https://www.whitepages.com/name/{username}"
    try:
        response = requests.get(url, allow_redirects=False, timeout=5)
        found = response.status_code == 200
        return {
            "service": "WhitePages",
            "url": url,
            "found": found,
            "profile_data": {}
        }
    except Exception as e:
        return {
            "service": "WhitePages",
            "url": url,
            "found": False,
            "profile_data": {"error": str(e)}
        }
