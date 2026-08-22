import requests

def check(username):
    """
    Check if username exists on Tumblr
    """
    url = f"https://{username}.tumblr.com"
    try:
        response = requests.get(url, allow_redirects=False, timeout=5)
        found = response.status_code == 200
        return {
            "service": "Tumblr",
            "url": url,
            "found": found,
            "profile_data": {}
        }
    except Exception as e:
        return {
            "service": "Tumblr",
            "url": url,
            "found": False,
            "profile_data": {"error": str(e)}
        }
