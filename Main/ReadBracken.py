import pandas

def Bracken_To_Csv(input_file_path, output_file_path):

    df = pandas.read_table(input_file_path, sep='\t')

    df.to_csv(output_file_path, index=False)
