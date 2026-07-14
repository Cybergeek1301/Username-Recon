"""Mastodon provider that checks whether a Mastodon profile exists.

Note: Mastodon is federated, so usernames are instance-specific.
This checks the main instance (mastodon.social) by default.

This example uses a lightweight HTTP request and returns a standard result dict:
{
  "service": "mastodon",
  "url": "https://mastodon.social/@<username>",
  "found": True/False,
  "profile_data": { ... }
}

Extend profile_data scraping as needed (rate limiting, API usage, authentication).
"""

import requests

SERVICE = "mastodon"
INSTANCE = "mastodon.social"
BASE_URL = f"https://{INSTANCE}"


def check(username, timeout=5.0):
    url = f"{BASE_URL}/@{username}"
    try:
        # Use a HEAD request first to avoid downloading page body
        resp = requests.head(url, timeout=timeout, allow_redirects=True)
        found = resp.status_code == 200
    except requests.RequestException:
        # On network errors, mark as not found and attach no profile data
        return {"service": SERVICE, "url": url, "found": False, "profile_data": {}}

    profile_data = {}
    # Optionally, we could fetch more details with a GET request or Mastodon API
    return {"service": SERVICE, "url": url, "found": found, "profile_data": profile_data}
