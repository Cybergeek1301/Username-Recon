import requests

def check(username):
    """
    Check WhatsApp - Note: WhatsApp primarily uses phone numbers, not usernames
    This provides basic information only
    """
    # WhatsApp doesn't have public username profiles in traditional sense
    return {
        "service": "WhatsApp",
        "url": "https://www.whatsapp.com",
        "found": False,
        "profile_data": {"note": "WhatsApp uses phone numbers, not usernames"}
    }
