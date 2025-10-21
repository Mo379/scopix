# Contributing to Scopix

Thank you for your interest in contributing to Scopix! We welcome contributions from the community.

## Development Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/scopix.git
   cd scopix
   ```

2. Install Poetry if you haven't:
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

3. Install dependencies:
   ```bash
   poetry install
   poetry install --with dev,docs
   ```

4. Install pre-commit hooks:
   ```bash
   pre-commit install
   ```

## Coding Standards

- Use `ruff` for linting and formatting
- Follow PEP 8 style guide
- Add type hints to all functions
- Write docstrings for classes and methods
- Use descriptive commit messages

## Testing

Run tests with:
```bash
poetry run pytest
```

## Pull Requests

- Create a feature branch from `main`
- Ensure all tests pass
- Update documentation if needed
- Follow conventional commit format

## Reporting Issues

Use GitHub issues to report bugs or request features. Provide detailed information including:
- Python version
- Operating system
- Steps to reproduce
- Expected vs actual behavior

## License

By contributing, you agree that your contributions will be licensed under the MIT License.