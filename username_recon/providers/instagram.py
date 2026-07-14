"""Instagram provider that checks whether an Instagram profile exists by username.

This example uses a lightweight HTTP request and returns a standard result dict:
{
  "service": "instagram",
  "url": "https://www.instagram.com/<username>",
  "found": True/False,
  "profile_data": { ... }
}

Extend profile_data scraping as needed (rate limiting, API usage, authentication).
"""

import requests

SERVICE = "instagram"
BASE_URL = "https://www.instagram.com"


def check(username, timeout=5.0):
    url = f"{BASE_URL}/{username}"
    try:
        # Use a HEAD request first to avoid downloading page body
        resp = requests.head(url, timeout=timeout, allow_redirects=True)
        found = resp.status_code == 200
    except requests.RequestException:
        # On network errors, mark as not found and attach no profile data
        return {"service": SERVICE, "url": url, "found": False, "profile_data": {}}

    profile_data = {}
    # Optionally, we could fetch more details with a GET request or Instagram API
    return {"service": SERVICE, "url": url, "found": found, "profile_data": profile_data}
