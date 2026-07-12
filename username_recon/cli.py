import json
import csv
import sys
import click
from .providers import github as github_provider

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
