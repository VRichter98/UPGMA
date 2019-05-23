


seq1 = "AAAGGGTTT"

seq2 = "AAAGGTTTT"

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
#Distance2 = {}

for annotation, sequence in all_sequences.items():
       for annotation2, sequence2 in all_sequences.items():
            if annotation != annotation2:
                #print(annotation, "vs", annotation2, ':',sequence, "vs", sequence2, ":", hammingDistance(sequence, sequence2))
                Distance[annotation, annotation2] = hammingDistance(sequence, sequence2)
                #Distance2[annotation2, annotation] = hammingDistance(sequence, sequence2)



print(Distance)




print(Distance["SeqD", "SeqA"])


min_key = min(Distance, key=Distance.get)
print(min_key)

min_value = min(Distance.values())
print(min_value)

#newDist = Distance.pop(min_key)
#print(Distance)




def replace_value(old_key, new_value):
    for key in Distance.keys():
        if key == old_key:
            Distance[key] = new_value
        return Distance


replace_value(min(Distance, key=Distance.get), '')
print(Distance)

distance_UPGMA = {}
lowest_value = min(Distance.values())
distance_UPGMA[min(Distance, key=Distance.get)] = lowest_value

print(distance_UPGMA)


def upgma(Distance):
    distance_UPGMA = {}
    lowest_value = min(Distance.values())
    distance_UPGMA[min(Distance, key=Distance.get)] = lowest_value
    Path_length = lowest_value / 2
    return Path_length

    new = Distance.pop

    #lowest_Sequences = min(Distance, key=Distance.get)
    #replace_value(lowest_Sequences, "--")

    newDist = Distance.pop()














