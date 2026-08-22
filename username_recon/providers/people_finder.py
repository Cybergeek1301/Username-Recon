import requests

def check(username):
    """
    Check if username/name exists on PeopleFinder
    """
    url = f"https://www.peoplefinder.com/find/results?fname={username}"
    try:
        response = requests.get(url, allow_redirects=False, timeout=5)
        found = response.status_code == 200
        return {
            "service": "People Finder",
            "url": url,
            "found": found,
            "profile_data": {}
        }
    except Exception as e:
        return {
            "service": "People Finder",
            "url": url,
            "found": False,
            "profile_data": {"error": str(e)}
        }
