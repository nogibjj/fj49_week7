# CSV Splitter

[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/yourusername/your-repo/blob/main/LICENSE)
[![PyPI version](https://badge.fury.io/py/your-tool.svg)](https://badge.fury.com/py/your-tool)
[![Build Status](https://travis-ci.org/yourusername/your-repo.svg?branch=main)](https://travis-ci.org/yourusername/your-repo)

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)  
- [Command Line Interface](#command-line-interface)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Installation

    pip install csv-splitter

## Usage

    csv-splitter input.csv output_prefix --rows 100  

## Command Line Interface

- `input.csv` - Path to input CSV file  
- `output_prefix` - Prefix for output files
- `--rows` - Number of rows per output file

    csv-splitter --help

## Examples  

Split large CSV into 1000 row files  

    csv-splitter large.csv output_ --rows 1000

Split into 500 row files  

    csv-splitter data.csv output_ --rows 500

## Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.