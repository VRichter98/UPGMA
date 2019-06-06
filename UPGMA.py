



def hammingDistance(seq1, seq2):
    distance = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            distance += 1
    return distance


def read_fasta(filename):
    """
    Read sequences from FASTA file into dictionary, ignoring chain information.
    :param filename: path to FASTA file
    :return: dictionary with annotations as key
    """
    fasta_file = open(filename)
    sequences = {}                         # Initialize empty dictionary
    for line in fasta_file:
        line = line.replace("\r","").replace("\n","")
        if line.startswith(">"):
            annotation = line[1:]          # Get annotation from the line after ">"
            sequences[annotation] = ""     # Start new sequence with this annotation
        elif line.startswith(";"):
            pass                           # Ignore chain information after ";"
        else:
            sequences[annotation] += line  # Append sequence with this annotation
    fasta_file.close()
    return sequences


fasta_filename = 'sequence.fasta'
all_sequences = read_fasta(fasta_filename)

Distance = {}

def dict_Distance():
    for seq in all_sequences:
        for seq1 in all_sequences:
            if seq == seq1:
                pass
            else:
                if (seq1, seq) in Distance:
                    pass
                else:
                    Distance[seq, seq1] = hammingDistance(all_sequences[seq], all_sequences[seq1])
    return Distance
dict_Distance()
print(Distance)

temp = []
dictlist = []

def convert_dict_to_list():
    for key, value in Distance.items():
        temp = [key, value]
        dictlist.append(temp)

    for i in range(len(dictlist)):
        dictlist2 = []
        dictlist2 = list(dictlist[i][0])
        dictlist[i][0] = dictlist2
    return dictlist
convert_dict_to_list()

print(dictlist)

pair_1 = set(dictlist[0][0])
pair_2 = set(dictlist[3][0])
pair_3 = set(dictlist[1][0])

pair_ges = pair_1 | pair_2 | pair_3
print(pair_ges)















