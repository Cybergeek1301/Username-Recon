import requests

def check(username):
    """
    Check if username exists on Truth Social
    """
    url = f"https://truthsocial.com/@{username}"
    try:
        response = requests.get(url, allow_redirects=False, timeout=5)
        found = response.status_code == 200
        return {
            "service": "Truth Social",
            "url": url,
            "found": found,
            "profile_data": {}
        }
    except Exception as e:
        return {
            "service": "Truth Social",
            "url": url,
            "found": False,
            "profile_data": {"error": str(e)}
        }
