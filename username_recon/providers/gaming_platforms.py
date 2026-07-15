"""Provider for checking username availability on popular gaming platforms and forums.

This provider checks a variety of well-known gaming sites to see if a
username has been registered or is publicly searchable.

Popular gaming platforms checked:
- Steam
- Epic Games
- PlayStation Network (PSN)
- Xbox Live
- Nintendo Network
- Minecraft
- Valorant
- League of Legends
- Dota 2
- Counter-Strike
"""

import requests

SERVICE = "gaming_platforms"
BASE_URLS = {
    "steam": "https://steamcommunity.com/search/users/{username}",
    "epic_games": "https://www.epicgames.com/id/user/{username}",
    "playstation": "https://www.playstation.com/en-us/psn/profile/{username}",
    "xbox_live": "https://www.xbox.com/en-US/xbox-live/gamertag/{username}",
    "nintendo": "https://www.nintendo.com/search/users/{username}",
    "minecraft": "https://www.minecraft.net/en-us/profile/{username}",
    "valorant": "https://tracker.gg/valorant/profile/pc/{username}",
    "league_of_legends": "https://www.leagueoflegends.com/en-us/summoner/{username}",
    "dota2": "https://www.dota2.com/profile/{username}",
    "counter_strike": "https://www.cs.money/account/{username}",
}


def check(username, timeout=5.0):
    """Check username availability across popular gaming platforms.
    
    Args:
        username: Username to check
        timeout: Request timeout in seconds
        
    Returns:
        dict: Standard result format with list of gaming platform results
    """
    results = []
    
    for platform_name, url_template in BASE_URLS.items():
        url = url_template.format(username=username)
        try:
            resp = requests.head(url, timeout=timeout, allow_redirects=True)
            found = resp.status_code == 200
            results.append({
                "platform": platform_name,
                "url": url,
                "found": found,
                "status_code": resp.status_code
            })
        except requests.RequestException as e:
            results.append({
                "platform": platform_name,
                "url": url,
                "found": False,
                "error": str(e)
            })
    
    return {
        "service": SERVICE,
        "username": username,
        "platforms_checked": len(results),
        "found_on": sum(1 for r in results if r.get("found", False)),
        "profile_data": results
    }
