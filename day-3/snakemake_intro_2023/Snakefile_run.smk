from pathlib import Path

data_dir=Path('data')
prefixes=[p.stem for p in data_dir.glob('*.txt')]

rule all:
    input:
        "output_data/overall_line_count_python.txt"

rule count_lines:
    input:
        text_file="data/{prefix}.txt"
    output:
        txt_out="output_data/{prefix}_counts_python.txt"
    run:
        counter = 0
        with open(input.text_file) as fp:
            for line in fp:
                counter += 1
        with open(output.txt_out,'wt') as fp:
            fp.write(f"{input.text_file},{counter}\n")


rule summarize_line_count:
    input:
        txt_in=[f"output_data/{prefix}_counts_python.txt" for prefix in prefixes]
    output:
        "output_data/overall_line_count_python.txt"
    run:
        my_list = []
        for fn in input.txt_in:
            with open(fn) as fp:
                for line in fp:
                    cols = line.strip().split(',')
                    file_name, no_rows = cols[0], int(cols[1])
                    my_list.append([file_name, no_rows])
        with open(output[0],'wt') as fp:
            for file_name,no_rows in my_list:
                fp.write(f"{file_name},{no_rows}\n")
