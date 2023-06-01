from pathlib import Path

data_dir=Path('data')
prefixes=[p.stem for p in data_dir.glob('*.txt')]

rule all:
    input:
        "output_data/overall_line_count.txt"

rule count_lines:
    input:
        text_file="data/{prefix}.txt"
    output:
        txt_out="output_data/{prefix}_counts.txt"
    shell:
        "wc -l {input.text_file} > {output.txt_out}"


rule summarize_line_count:
    input:
        txt_in=[f"output_data/{prefix}_counts.txt" for prefix in prefixes]
    output:
        "output_data/overall_line_count.txt"
    shell:
        "cat {input} > {output[0]}"