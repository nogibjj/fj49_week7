from setuptools import setup

setup(
    name="my-csv-splitter",
    version="1.0.0",
    author="Your Name",
    description="A tool to split CSV files",
    py_modules=["main"],
    install_requires=[
        'click',
    ],
    entry_points={
        "console_scripts": [
            "csv-splitter = main:split_csv",
        ],
    },
)


# [pypi]
#   username = __token__
#   password = pypi-AgEIcHlwaS5vcmcCJDkxMzFmNjc0LTA5OWUtNGJmYy1iZWE2LWZkY2U1YWQzNGIzYgACKlszLCIzOWI1NmYxYy03NmI5LTQ2YmUtOTJjNC1jNjQ5OWM1MjA4YTEiXQAABiCZBTz5bc8v94fnohezHMcFmH8n8en4GIoLr62QoUMySA