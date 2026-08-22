import requests

def check(username):
    """
    Check if username exists on Wave (Accounting/Payment platform)
    """
    url = f"https://www.waveapps.com/profile/{username}"
    try:
        response = requests.get(url, allow_redirects=False, timeout=5)
        found = response.status_code == 200
        return {
            "service": "Wave",
            "url": url,
            "found": found,
            "profile_data": {}
        }
    except Exception as e:
        return {
            "service": "Wave",
            "url": url,
            "found": False,
            "profile_data": {"error": str(e)}
        }
