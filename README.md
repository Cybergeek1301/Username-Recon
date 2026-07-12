# Quick start

This repository provides a small, extensible Python CLI to check username availability across online services.

Prerequisites
- Python 3.8+
- pip

Install (development)

```bash
git clone https://github.com/Cybergeek1301/Username-Recon.git
cd Username-Recon
python3 -m venv venv
source venv/bin/activate
pip install -e .[dev]
```

Usage

```bash
# Check a username and print JSON to stdout
recon --username octocat

# Save CSV
recon --username octocat --format csv --output octocat.csv
```

Development

- Add new providers under username_recon/providers/
- Tests live in tests/ and can be run with pytest

License
- MIT — see LICENSE file
