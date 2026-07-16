"""Discord provider that checks whether a Discord user exists by username.

This example uses a lightweight HTTP request and returns a standard result dict:
{
  "service": "discord",
  "url": "https://discord.com/users/<username>",
  "found": True/False,
  "profile_data": { ... }
}

Extend profile_data scraping as needed (rate limiting, API usage, authentication).
"""

import requests

SERVICE = "discord"
BASE_URL = "https://discord.com/users"


def check(username, timeout=5.0):
    """Check if Discord user exists via profile URL.
    
    Note: The public Discord API search endpoint requires authentication.
    This check uses the web profile URL pattern instead.
    """
    url = f"{BASE_URL}/{username}"
    try:
        # Use a HEAD request first to avoid downloading page body
        resp = requests.head(url, timeout=timeout, allow_redirects=True)
        found = resp.status_code == 200
    except requests.RequestException:
        # On network errors, mark as not found and attach no profile data
        return {"service": SERVICE, "url": url, "found": False, "profile_data": {}}

    profile_data = {}
    return {"service": SERVICE, "url": url, "found": found, "profile_data": profile_data}
