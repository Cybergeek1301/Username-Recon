"""Facebook provider that checks whether a Facebook profile exists by username.

This example uses a lightweight HTTP request and returns a standard result dict:
{
  "service": "facebook",
  "url": "https://www.facebook.com/<username>",
  "found": True/False,
  "profile_data": { ... }
}

Extend profile_data scraping as needed (rate limiting, API usage, authentication).
"""

import requests

SERVICE = "facebook"
BASE_URL = "https://www.facebook.com"


def check(username, timeout=5.0):
    url = f"{BASE_URL}/{username}"
    try:
        # Use a HEAD request first to avoid downloading page body
        resp = requests.head(url, timeout=timeout, allow_redirects=True)
        # Facebook redirects unauthenticated requests to login or checkpoint pages.
        # Check status code and verify we didn't get redirected to login or checkpoint.
        found = resp.status_code == 200 and "login" not in resp.url and "checkpoint" not in resp.url
    except requests.RequestException:
        # On network errors, mark as not found and attach no profile data
        return {"service": SERVICE, "url": url, "found": False, "profile_data": {}}

    profile_data = {}
    return {"service": SERVICE, "url": url, "found": found, "profile_data": profile_data}
