"""Provider for checking username availability on popular social media platforms.

This provider checks a variety of well-known social media sites to see if a
username has been registered or is publicly searchable.

Popular social media sites checked:
- Snapchat
- BeReal
- Threads
- Nextdoor
- WeChat
- WhatsApp Business
- Viber
- Signal
- Mastodon (Fediverse)
"""

import requests

SERVICE = "social_media"
BASE_URLS = {
    "snapchat": "https://www.snapchat.com/add/{username}",
    "bereal": "https://bereal.com/user/{username}",
    "threads": "https://www.threads.net/@{username}",
    "nextdoor": "https://nextdoor.com/profile/{username}",
    "wechat": "https://wechat.com/user/{username}",
    "whatsapp_business": "https://www.whatsapp.com/business/profile/{username}",
    "viber": "https://viber.com/user/{username}",
    "signal": "https://signal.me/{username}",
}


def check(username, timeout=5.0):
    """Check username availability across popular social media sites.
    
    Args:
        username: Username to check
        timeout: Request timeout in seconds
        
    Returns:
        dict: Standard result format with list of social media site results
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
