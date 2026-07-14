import json
import csv
import sys
import click
from .providers import github as github_provider
from .providers import instagram as instagram_provider
from .providers import tiktok as tiktok_provider
from .providers import reddit as reddit_provider
from .providers import youtube as youtube_provider
from .providers import discord as discord_provider
from .providers import twitch as twitch_provider
from .providers import facebook as facebook_provider
from .providers import bluesky as bluesky_provider
from .providers import mastodon as mastodon_provider
from .providers import linkedin as linkedin_provider
from .providers import twitter_x as twitter_x_provider
from .providers import mewe as mewe_provider
from .providers import pinterest as pinterest_provider
from .providers import roblox as roblox_provider
from .providers import telegram as telegram_provider
from .providers import indeed as indeed_provider

@click.command()
@click.option("--username", "username", required=True, help="Username to check across providers")
@click.option("--output", "output", default=None, help="Output file path (defaults to stdout)")
@click.option("--format", "outfmt", default="json", type=click.Choice(["json","csv"]), help="Output format")
def main(username, output, outfmt):
    """Simple recon CLI that checks a username against example providers.

    This is intentionally small: add more providers under username_recon.providers.
    """
    results = []

    # Run providers
    results.append(github_provider.check(username))
    results.append(instagram_provider.check(username))
    results.append(tiktok_provider.check(username))
    results.append(reddit_provider.check(username))
    results.append(youtube_provider.check(username))
    results.append(discord_provider.check(username))
    results.append(twitch_provider.check(username))
    results.append(facebook_provider.check(username))
    results.append(bluesky_provider.check(username))
    results.append(mastodon_provider.check(username))
    results.append(linkedin_provider.check(username))
    results.append(twitter_x_provider.check(username))
    results.append(mewe_provider.check(username))
    results.append(pinterest_provider.check(username))
    results.append(roblox_provider.check(username))
    results.append(telegram_provider.check(username))
    results.append(indeed_provider.check(username))

    # Serialize
    if outfmt == "json":
        data = json.dumps(results, indent=2)
        if output:
            with open(output, "w", encoding="utf-8") as f:
                f.write(data)
        else:
            click.echo(data)
    else:
        # CSV: flatten profile_data as JSON string
        fieldnames = ["service","url","found","profile_data"]
        if output:
            f = open(output, "w", newline="", encoding="utf-8")
        else:
            f = sys.stdout
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for r in results:
            writer.writerow({
                "service": r.get("service"),
                "url": r.get("url"),
                "found": r.get("found"),
                "profile_data": json.dumps(r.get("profile_data", {}), ensure_ascii=False)
            })
        if output:
            f.close()

if __name__ == "__main__":
    main()
