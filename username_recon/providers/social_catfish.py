import requests

def check(username):
    """
    Check if username exists on Social Catfish
    Note: Social Catfish is primarily a reverse search tool
    """
    url = f"https://www.socialcatfish.com/freetools/reverse-username-search/?username={username}"
    try:
        response = requests.get(url, allow_redirects=False, timeout=5)
        found = response.status_code == 200
        return {
            "service": "Social Catfish",
            "url": url,
            "found": found,
            "profile_data": {}
        }
    except Exception as e:
        return {
            "service": "Social Catfish",
            "url": url,
            "found": False,
            "profile_data": {"error": str(e)}
        }
