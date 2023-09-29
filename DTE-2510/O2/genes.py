def find_genes(genome):
    triplets = ["ATG", "TAG", "TAA", "TGA"]
    index = 0
    to_add = 0
    genes = []
    #read in slices of 3
    [genome[i:3] for gene in zip(*(iter(genome),) * 3)]:
        print(gene)
        if gene == 'ATG' and to_add == 0:
            to_add = 1
        if gene in triplets and to_add == 1:
            to_add = 0
        elif to_add == 1:
            genes.append(gene)
    print(genes)

genome = "TTATGTTTTAAGGATGGGGCGTTAGTT"

find_genes(genome)