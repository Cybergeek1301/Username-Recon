"""Discord provider that checks whether a Discord user exists by username.

This example uses a lightweight HTTP request and returns a standard result dict:
{
  "service": "discord",
  "url": "https://discordapp.com/users/<username>",
  "found": True/False,
  "profile_data": { ... }
}

Extend profile_data scraping as needed (rate limiting, API usage, authentication).
"""

import requests

SERVICE = "discord"


def check(username, timeout=5.0):
    # Discord username validation is primarily API-based
    # This is a basic check using the Discord API
    url = f"https://discord.com/api/v10/users/search?q={username}"
    try:
        resp = requests.get(url, timeout=timeout)
        # Discord API typically returns 200 for valid requests
        found = resp.status_code == 200 and len(resp.json().get('users', [])) > 0
    except requests.RequestException:
        # On network errors, mark as not found and attach no profile data
        return {"service": SERVICE, "url": f"https://discord.com/users/{username}", "found": False, "profile_data": {}}

    profile_data = {}
    return {"service": SERVICE, "url": f"https://discord.com/users/{username}", "found": found, "profile_data": profile_data}
