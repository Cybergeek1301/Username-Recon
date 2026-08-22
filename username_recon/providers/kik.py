import requests

def check(username):
    """
    Check if username exists on Kik Messaging
    """
    url = f"https://kik.me/{username}"
    try:
        response = requests.get(url, allow_redirects=False, timeout=5)
        found = response.status_code == 200
        return {
            "service": "Kik Messaging",
            "url": url,
            "found": found,
            "profile_data": {}
        }
    except Exception as e:
        return {
            "service": "Kik Messaging",
            "url": url,
            "found": False,
            "profile_data": {"error": str(e)}
        }
