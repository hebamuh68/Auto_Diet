import os
import argparse
import toolchest_client as toolchest
from ReadBracken import Bracken_To_Csv


def GetAbundance():
    parser = argparse.ArgumentParser(description='Get the bacterial abundance from a metagenomic file...')
    parser.add_argument("infile", help='A metagenomic file in fastq format...')
    parser.add_argument("--output", help='A path to where you want the output file be...')
    args = parser.parse_args()

    toolchest.set_key("MTQ0NWE.NGUxMWFhMzctNGRkOS00OWM1LWJhMTUtNzg2NTU2NDE1OWJh")

    input_file = args.infile

    if args.output:
        output_folder = args.output
    else:
        output_folder = input_file[:input_file.find('.fastq')]
        os.mkdir(output_folder)

    toolchest.kraken2(
        inputs=input_file,
        output_path=output_folder,
        database_name="standard",
        database_version="1"
    )

    bracken_input_file_name = [name for name in os.listdir(output_folder) if name == 'kraken2_report.txt']

    toolchest.bracken(
        kraken2_report=os.path.join(output_folder, bracken_input_file_name[0]),
        output_path=output_folder,
        database_name="standard",
        database_version="1"
    )

    bracken_file_path = os.path.join(output_folder, 'output.bracken')
    csv_file_path = os.path.join(output_folder, 'abundance.csv')

    Bracken_To_Csv(bracken_file_path, csv_file_path)
