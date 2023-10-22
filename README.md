# CSV Splitter - Split your large CSV files into smaller chunks

[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/yourusername/your-repo/blob/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/my-csv-splitter.svg)](https://pypi.org/project/my-csv-splitter/)
[![CiCd](https://github.com/nogibjj/fj49_week7/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/fj49_week7/actions/workflows/cicd.yml)

This is a project for week 7 for my IDS706 - Data Engineering class. This is a python package hosted on PyPi and a Command Line tool for splitting large csv files into smaller csv files which can then be processed and used. 

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)  
- [Command Line Interface](#command-line-interface)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Installation

    pip install my-csv-splitter

## Usage

    csv-splitter input.csv output_prefix 100  

## Command Line Interface

- `input.csv` - Path to input CSV file (just file name if the file is in the same path)
- `output_prefix` - Prefix for output files (eg, if you write output, all files will be generated as output_1.csv, output_2.csv and so on)
- `100` - Number of rows per output file (you can customize how many rows you want each splitted file to have)

## Examples  

Split large CSV into 1000 row files  

    csv-splitter large.csv output 1000

Split into 500 row files  

    csv-splitter data.csv output 500

## Contributing

I welcome contributions and improvements! To contribute to this project, please follow these guidelines:

Fork the repository.
Create a new branch for your feature or bug fix.
Write clear, concise code with comments as needed.
Write tests for your code.
Make sure the existing tests pass.
Submit a pull request with a clear description and reference to the related issue (if applicable).
I appreciate your help in making this tool better!

To reach me please email me at faraz.jawed@duke.edu

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
