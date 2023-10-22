import os
import pytest
from main import split_csv

def test_split_csv():
    input_file = 'spotify.csv'  # Replace with the actual file path
    output_prefix = 'output_chunk'
    chunk_size = 1000  # Provide as an integer

    

    split_csv(input_file, output_prefix, chunk_size)

    # Check if the expected output files are generated
    for i in range(1, 4):  # Assuming it will create 3 output files for the test case
        output_file = f'{output_prefix}_{i}.csv'
        assert os.path.exists(output_file)

if __name__ == '__main__':
    test_split_csv()
