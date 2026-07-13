# Username Recon

![CI](https://github.com/Cybergeek1301/Username-Recon/actions/workflows/ci.yaml/badge.svg)

A lightweight, extensible Python CLI to check username availability across online services.

## Features

- ✅ Enumerate username availability across multiple platforms
- ✅ Collect publicly available profile metadata
- ✅ Export results to JSON/CSV
- ✅ Extensible — add new providers with simple adapters

## Quick start

### Prerequisites

- Python 3.10+
- pip

### Install (development)

```bash
git clone https://github.com/Cybergeek1301/Username-Recon.git
cd Username-Recon
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -e .[dev]
```

## Usage

```bash
# Check a username and print JSON to stdout
recon --username octocat

# Save as CSV
recon --username octocat --format csv --output octocat.csv
```

## Output Format

Results are returned as a list of objects:

```json
[
  {
    "service": "github",
    "url": "https://github.com/octocat",
    "found": true,
    "profile_data": {
      "id": 1,
      "name": "The Octocat",
      "company": "GitHub"
    }
  }
]
```

CSV export flattens `profile_data` as a JSON string.

## Development

### Adding new providers

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

Quick start:
1. Create a new file under `username_recon/providers/` (e.g., `twitter.py`)
2. Implement a `check(username)` function that returns a dict with:
   - `service` (str): Name of the service
   - `url` (str): Profile URL
   - `found` (bool): Whether username exists
   - `profile_data` (dict): Public profile info or empty dict

3. Import and add it to `username_recon/cli.py`

### Running tests

```bash
pytest              # Run all tests
pytest -v           # Verbose output
pytest --cov        # With coverage report
```

## Security & Responsible Use

This tool is designed for **legitimate security research and account verification only**. Users are responsible for:

- Respecting rate limits and platform terms of service
- Obtaining proper authorization before using on third-party accounts
- Complying with local laws regarding data collection and privacy
- Not using this for spam, harassment, or unauthorized profiling

## Configuration

No API keys required for the default GitHub provider. Additional providers may require configuration — see their documentation in [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT — see LICENSE file
