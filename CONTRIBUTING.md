# Contributing

Thank you for your interest in contributing to Username Recon!

## Adding New Providers

1. **Create the provider module** under `username_recon/providers/` with a `check(username)` function
2. **Follow the standard interface**:
   ```python
   def check(username):
       """Check username availability and return provider metadata."""
       return {
           "service": "service-name",
           "url": "https://...",
           "found": bool,
           "profile_data": {}  # Public metadata or empty dict
       }
   ```
3. **Add tests** in `tests/providers/test_<service_name>.py`
4. **Update cli.py** to import and call your provider
5. **Update README** with any configuration or rate-limit info

## Testing

- Write tests in `tests/` following pytest conventions
- Include both success and failure cases
- Mock HTTP requests to avoid external dependencies in CI

```bash
pytest -v
pytest tests/providers/test_github.py
```

## Code Style

- Follow PEP 8
- Use type hints where possible
- Add docstrings to functions

## Responsible Disclosure

- Do not submit providers that bypass authentication or violate ToS
- Consider rate limiting and respect platform guidelines
- Document any API keys or credentials required

## Pull Request Process

1. Fork the repository
2. Create a feature branch (`git checkout -b feat/new-provider`)
3. Commit your changes with clear messages
4. Push and open a PR with a description of what was added
5. Ensure all tests pass before requesting review

## Security & Ethics

This tool is for legitimate use only. By contributing, you agree that:
- Your code will not be used for spam, harassment, or unauthorized profiling
- You have considered and tested rate limiting
- You respect each platform's terms of service
