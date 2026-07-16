"""Telegram provider that checks whether a Telegram profile exists by username.

Note: Telegram usernames are case-insensitive and can only contain alphanumeric characters and underscores.
This example uses a lightweight HTTP request and returns a standard result dict:
{
  "service": "telegram",
  "url": "https://t.me/<username>",
  "found": True/False,
  "profile_data": { ... }
}

Extend profile_data scraping as needed (rate limiting, API usage, authentication).
"""

import requests

SERVICE = "telegram"
BASE_URL = "https://t.me"


def check(username, timeout=5.0):
    url = f"{BASE_URL}/{username}"
    try:
        # Telegram's t.me/<username> pages always return 200 OK even if the username
        # does not exist (they display a generic page saying 'If you have Telegram, you can contact...').
        # We must use a GET request and check the response body to ensure this placeholder text is not present.
        resp = requests.get(url, timeout=timeout)
        found = resp.status_code == 200 and "If you have Telegram, you can contact" not in resp.text
    except requests.RequestException:
        # On network errors, mark as not found and attach no profile data
        return {"service": SERVICE, "url": url, "found": False, "profile_data": {}}

    profile_data = {}
    return {"service": SERVICE, "url": url, "found": found, "profile_data": profile_data}
