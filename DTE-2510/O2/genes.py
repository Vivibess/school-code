def main():
    genome = genome_input()
    genes = find_genes(genome)
    
    print(genes.replace(',','\n'))

def genome_input():
    while True:
        genome = str(input("Enter a genome string: "))
        if genome != '':
            break
        else:
            print("Please enter a not-empty string.")
    return genome.upper()

def find_genes(genome):
    triplets = ["ATG", "TAG", "TAA", "TGA"]
    genes = []
    tempgenes = ''
    # read in slices of 3
    for i in range(0, len(genome)):
        if genome[i:i+3] == 'ATG':
            for j in range(i+3, len(genome), 3):
                if genome[j:j+3] in triplets:
                    genes.append(tempgenes)
                    tempgenes = ''
                    break
                tempgenes = tempgenes + genome[j:j+3]
    return ','.join(genes)

main()