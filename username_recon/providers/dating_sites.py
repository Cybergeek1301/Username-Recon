"""Provider for checking username availability on popular dating sites.

This provider checks a variety of well-known dating platforms to see if a
username has been registered or is publicly searchable.

Popular dating sites checked:
- Match
- eHarmony
- OkCupid
- Bumble
- Tinder
- Hinge
- Badoo
- PlentyOfFish (POF)
- Zoosk
- EliteSingles
- JDate
- The League
- Coffee Meets Bagel
- Feeld
"""

import requests

SERVICE = "dating_sites"
BASE_URLS = {
    "match": "https://www.match.com/member/{username}",
    "eharmony": "https://www.eharmony.com/member/{username}",
    "okcupid": "https://www.okcupid.com/profile/{username}",
    "bumble": "https://www.bumble.com/en/profile/{username}",
    "tinder": "https://www.tinder.com/@{username}",
    "hinge": "https://www.hinge.co/people/{username}",
    "badoo": "https://badoo.com/profile/{username}",
    "plentyoffish": "https://www.plentyoffish.com/member/{username}",
    "zoosk": "https://www.zoosk.com/member/{username}",
    "elitesingles": "https://www.elitesingles.com/member/{username}",
    "jdate": "https://www.jdate.com/member/{username}",
    "the_league": "https://www.theleague.com/profile/{username}",
    "coffee_meets_bagel": "https://coffeemeetsbagelapp.com/profile/{username}",
    "feeld": "https://feeld.co/u/{username}",
}


def check(username, timeout=5.0):
    """Check username availability across popular dating sites.
    
    Args:
        username: Username to check
        timeout: Request timeout in seconds
        
    Returns:
        dict: Standard result format with list of dating site results
    """
    results = []
    
    for site_name, url_template in BASE_URLS.items():
        url = url_template.format(username=username)
        try:
            resp = requests.head(url, timeout=timeout, allow_redirects=True)
            found = resp.status_code == 200
            results.append({
                "site": site_name,
                "url": url,
                "found": found,
                "status_code": resp.status_code
            })
        except requests.RequestException as e:
            results.append({
                "site": site_name,
                "url": url,
                "found": False,
                "error": str(e)
            })
    
    return {
        "service": SERVICE,
        "username": username,
        "sites_checked": len(results),
        "found_on": sum(1 for r in results if r.get("found", False)),
        "profile_data": results
    }
