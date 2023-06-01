from pathlib import Path

data_dir=Path('data')
prefixes=[p.stem for p in data_dir.glob('*.txt')]

rule all:
    input:
        "output_data/overall_line_count_python_script.txt"

rule count_lines:
    input:
        text_file="data/{prefix}.txt"
    output:
        txt_out="output_data/{prefix}_counts_python_script.txt"
    script:
        "count_lines.py"


rule summarize_line_count:
    input:
        txt_in=[f"output_data/{prefix}_counts_python_script.txt" for prefix in prefixes]
    output:
        "output_data/overall_line_count_python_script.txt"
    script:
        "summarize_line_count.py"
