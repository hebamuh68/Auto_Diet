import os
import argparse
import toolchest_client as toolchest
from ReadBracken import Bracken_To_Csv


def Get_Abundance(input_file_path, output_folder_path):
    toolchest.set_key("MTQ0NWE.NGUxMWFhMzctNGRkOS00OWM1LWJhMTUtNzg2NTU2NDE1OWJh")

    toolchest.kraken2(
        inputs=input_file_path,
        output_path=output_folder_path,
        database_name="standard",
        database_version="1"
    )

    bracken_input_file_name = [name for name in os.listdir(output_folder_path) if name == 'kraken2_report.txt']

    toolchest.bracken(
        kraken2_report=os.path.join(output_folder_path, bracken_input_file_name[0]),
        output_path=output_folder_path,
        database_name="standard",
        database_version="1"
    )

    bracken_file_path = os.path.join(output_folder_path, 'output.bracken')
    csv_file_path = os.path.join(output_folder_path, 'abundance.csv')

    Bracken_To_Csv(bracken_file_path, csv_file_path)


# =======================================================================================
# Get the latest file uploaded
with open('PATH.txt') as f:
    for line in f:
        pass
    last_line = line

input_file = last_line.rstrip()
output_folder = input_file.split("/")[-1].split('.')[0]

Get_Abundance(input_file, output_folder)
