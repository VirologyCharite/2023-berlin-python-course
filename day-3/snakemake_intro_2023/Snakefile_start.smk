
rule all:
    input: "output_data/my_output.txt"

rule rule1:
    input:
        text_file="data/1-karamazov.txt"
    output:
        txt_out="output_data/my_output.txt"
    shell:
        "wc -l {input.text_file} > {output.txt_out}"
