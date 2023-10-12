# Ultimate IP Checker & Generator

This suite contains two main scripts:

1. **check.py**: This script checks provided IP addresses for a specific vulnerability, targeting `.env` endpoints. If any positive hits are found, it saves them in an `env` directory.
2. **gen.py**: This script generates a specified number of unique IP addresses and saves them in a file named `ip.txt`.

## Prerequisites

- Python 3.x
- aiohttp
- aiofiles
- rich

## Setup

1. Clone this repository:
2. Install the required libraries:
**
## Usage

### 1. IP Generator

To generate IP addresses:


This script will ask you how many IP addresses you want to generate. Once provided, it will generate the requested number of unique IP addresses and save them in `ip.txt`.

### 2. IP Checker

To check the IP addresses:


This script will pick IP addresses from `ip.txt` and check them. If there are any positive hits, they will be saved in the `env` directory.

## Contribution

Contributions are always welcome! If you have any suggestions, improvements, or issues, please open a pull request or an issue on GitHub.

## Support

If you need any help or have questions, join our [Telegram Group](https://t.ly/TVi50).

## License

This project is under the MIT License. See [LICENSE](./LICENSE) file for details.

---

**Disclaimer**: This tool is meant for educational purposes only. The developers are not responsible for any misuse or damage caused by this program.
