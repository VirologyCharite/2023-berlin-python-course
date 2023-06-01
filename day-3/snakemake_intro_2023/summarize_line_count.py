

my_list = []
for fn in snakemake.input.txt_in:
    with open(fn) as fp:
        for line in fp:
            cols = line.strip().split(',')
            file_name, no_rows = cols[0], int(cols[1])
            my_list.append([file_name, no_rows])
with open(snakemake.output[0],'wt') as fp:
    for file_name,no_rows in my_list:
        fp.write(f"{file_name},{no_rows}\n")