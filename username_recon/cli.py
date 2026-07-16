import os
import sys
import click
import concurrent.futures
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
@click.option("--output", "output", default=None, help="Output file")
@click.option("--format", "outfmt", default="json", help="Output format: json or csv")
def main(username, output, outfmt):
    results = []

    # List of all provider modules
    providers = [
        github_provider,
        instagram_provider,
        tiktok_provider,
        reddit_provider,
        youtube_provider,
        discord_provider,
        twitch_provider,
        facebook_provider,
        bluesky_provider,
        mastodon_provider,
        linkedin_provider,
        twitter_x_provider,
        mewe_provider,
        pinterest_provider,
        roblox_provider,
        telegram_provider,
        indeed_provider,
    ]

    # Run providers in parallel using ThreadPoolExecutor
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        # Submit all provider checks
        futures = [executor.submit(p.check, username) for p in providers]
        
        # Collect results as they complete
        for future in concurrent.futures.as_completed(futures):
            try:
                result = future.result()
                results.append(result)
            except Exception as e:
                # Log error but don't crash the entire scan
                click.echo(f"Error in provider: {e}", err=True)

    # Serialize
    if outfmt == "json":
        import json
        output_str = json.dumps(results, indent=2)
    elif outfmt == "csv":
        import csv
        from io import StringIO
        output = StringIO()
        writer = csv.DictWriter(output, fieldnames=["service", "url", "found"])
        writer.writeheader()
        for result in results:
            writer.writerow(
                {"service": result.get("service"), "url": result.get("url"), "found": result.get("found")}
            )
        output_str = output.getvalue()
    else:
        click.echo(f"Unknown format: {outfmt}", err=True)
        sys.exit(1)

    if output:
        with open(output, "w") as f:
            f.write(output_str)
        click.echo(f"Results written to {output}")
    else:
        click.echo(output_str)
