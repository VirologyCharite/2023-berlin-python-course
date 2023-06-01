


counter = 0
with open(snakemake.input.text_file) as fp:
    for line in fp:
        counter += 1
with open(snakemake.output.txt_out,'wt') as fp:
    fp.write(f"{snakemake.input.text_file},{counter}\n")