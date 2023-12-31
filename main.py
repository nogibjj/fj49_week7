import click
import csv

# Define the core functionality of your script without the @click.command() decorator
def split_csv(input_file, output_prefix, chunk_size):
    # Your core functionality here
    with open(input_file, 'r') as infile:
        reader = csv.reader(infile)
        header = next(reader)  # Assuming the first row is the header
        rows = list(reader)  # Read all rows into a list

    total_rows = len(rows)

    if chunk_size > total_rows:
        error_message = (
        f"Error: Chunk size ({chunk_size}) is greater than the total number "
        f"of rows ({total_rows}) in the input CSV."
        )
        click.echo(error_message)
        return

    outfile = None
    for i, row in enumerate(rows):
        if i % chunk_size == 0:
            if i > 0:
                outfile.close()
            chunk_num = i // chunk_size + 1
            outfile = open(f'{output_prefix}_{chunk_num}.csv', 'w', newline='')
            writer = csv.writer(outfile)
            writer.writerow(header)
        writer.writerow(row)

# Define the command-line interface separately
@click.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.argument('output_prefix', type=click.STRING)
@click.argument('chunk_size', type=click.INT)
def main(input_file, output_prefix, chunk_size):
    split_csv(input_file, output_prefix, chunk_size)

if __name__ == '__main__':
    main()
