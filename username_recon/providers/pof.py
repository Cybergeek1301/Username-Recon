import requests

def check(username):
    """
    Check if username exists on Plenty of Fish (POF)
    """
    url = f"https://www.pof.com/member.html?username={username}"
    try:
        response = requests.head(url, allow_redirects=False, timeout=5)
        found = response.status_code == 200
        return {
            "service": "POF",
            "url": url,
            "found": found,
            "profile_data": {}
        }
    except Exception as e:
        return {
            "service": "POF",
            "url": url,
            "found": False,
            "profile_data": {"error": str(e)}
        }
