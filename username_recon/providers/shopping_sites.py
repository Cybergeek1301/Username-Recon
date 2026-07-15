"""Provider for checking username availability on popular online shopping sites.

This provider checks a variety of well-known e-commerce platforms to see if a
username or account has been registered or is publicly searchable.

Popular shopping sites checked:
- Amazon
- eBay
- Etsy
- AliExpress
- Wish
- Wayfair
- Target
- Walmart
- Shopify (generic store check)
"""

import requests

SERVICE = "shopping_sites"
BASE_URLS = {
    "amazon": "https://www.amazon.com/s?k={username}",
    "ebay": "https://www.ebay.com/sch/i.html?_nkw={username}",
    "etsy": "https://www.etsy.com/search?q={username}",
    "aliexpress": "https://www.aliexpress.com/wholesale?SearchText={username}",
    "wish": "https://www.wish.com/search/{username}",
    "wayfair": "https://www.wayfair.com/s/search/results/{username}",
    "target": "https://www.target.com/s?searchTerm={username}",
    "walmart": "https://www.walmart.com/search/?query={username}",
    "shopify": "https://{username}.myshopify.com/",
}


def check(username, timeout=5.0):
    """Check username availability across popular online shopping sites.
    
    Args:
        username: Username to check
        timeout: Request timeout in seconds
        
    Returns:
        dict: Standard result format with list of shopping site results
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
