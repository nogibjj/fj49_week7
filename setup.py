from setuptools import setup

setup(
    name="easyfast-csv-splitter",
    version="1.0.0",
    author="Faraz Jawed",
    description="A tool to split CSV files",
    packages=["my_csv_splitter"],
    entry_points={
        "console_scripts": [
            "csv-splitter = my_csv_splitter.my_csv_splitter:main",
        ],
    },
)