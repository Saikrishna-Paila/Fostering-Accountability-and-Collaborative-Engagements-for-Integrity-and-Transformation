# Contributing to JurisAI

First off, thank you for considering contributing to JurisAI! It's people like you that make JurisAI such a great tool.

## Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to github@worldbank.org.

## License Information

JurisAI is licensed under the Mozilla Public License 2.0 (MPL-2.0). By contributing to JurisAI, you agree that your contributions will be licensed under the MPL-2.0.

### What does this mean for contributors?

- You can use the code commercially
- You can modify the code
- You can distribute the code
- You can use the code privately
- You must disclose the source code of any modifications
- You must include the license and copyright notice
- You must use the same license (MPL-2.0) for modifications
- You cannot use contributors' names without permission

### License Headers

All source code files should include the MPL-2.0 header:

```python
"""
This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0.
If a copy of the MPL was not distributed with this file, You can obtain one at
https://mozilla.org/MPL/2.0/.

Copyright (c) 2024 World Bank Group
"""
```

## How to Contribute

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Update documentation
6. Submit a pull request

### Development Process

1. **Setup Development Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -e ".[dev,docs]"
   ```

2. **Run Tests**:
   ```bash
   pytest
   ```

3. **Check Code Style**:
   ```bash
   black .
   flake8
   mypy src/
   ```

### Pull Request Process

1. Update the README.md with details of changes if needed
2. Update the documentation if you're introducing new features
3. Add tests for new functionality
4. Ensure all tests pass
5. Update the CHANGELOG.md
6. The PR will be merged once you have the sign-off of at least one maintainer

## Development Guidelines

- Follow PEP 8 style guide
- Write docstrings for all functions
- Maintain test coverage above 80%
- Use type hints
- Keep functions focused and small
- Comment complex logic

## Getting Help

If you need help, you can:
- Open an issue
- Email the maintainers
- Check the documentation

## Attribution

This Contributing Guide is adapted from the standard Mozilla Public License 2.0 contributing guidelines. 