import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-input", "--file", required=True, help="please place the name of your fastafilename here")

a = parser.parse_args()


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





fasta_filename = a.file  #'sequence.fasta'
all_sequences = read_fasta(fasta_filename)
sequence_names = list(all_sequences.keys())
new_sequence_names = []


def Pairwise_Hamming(all_sequences):
    """
    Calculate distances by Hamming distances of sequences
    :param all_sequences:
    :return: distance dictionary
    """
    Distance = {}
    for seq in all_sequences:
        for seq1 in all_sequences:
            if seq == seq1:
                pass
            else:
                Distance[seq, seq1] = hammingDistance(all_sequences[seq], all_sequences[seq1])
    return Distance

Distance = Pairwise_Hamming(all_sequences)

replacingvalues = ['Omega','Psi','Chi', 'Phi', 'Ypsilon', 'Tau', 'Sigma', 'Rho', 'Pi','Omikron', 'Xi', 'Ny', 'My', 'Lambda', 'Kappa', 'Iota', 'Theta', 'Eta', 'Zeta', 'Epsilon', 'Delta', 'Gamma', 'Beta', 'Alpha']


def upgma(Distance, sequence_names):
    results = []
    while len(Distance) > 0:
        new_sequence_names = []
        new_Distance = {}
        min_pair = min(Distance, key=Distance.get)
        min_distance = Distance[min(Distance, key=Distance.get)]

        for annotation in sequence_names:
            if annotation != min_pair[0] and annotation != min_pair[1]:
                new_sequence_names.append(annotation)
        new_seq_name = replacingvalues.pop()
        new_sequence_names.append(new_seq_name)
        for seq1 in new_sequence_names:
            for seq2 in new_sequence_names:
                if seq1 == seq2:
                    pass
                elif (seq1,seq2) in Distance:
                    new_Distance[seq1,seq2] = Distance[seq1,seq2]
                else:
                    if seq1 in sequence_names:
                        new_Distance[seq1,seq2] = (Distance[seq1, min_pair[0]] + Distance[seq1, min_pair[1]])/2
                    else:
                        new_Distance[seq1, seq2] = (Distance[min_pair[0], seq2] + Distance[min_pair[1], seq2]) / 2
        results.append([min_pair[1],min_pair[0],new_seq_name,min_distance/2])
        Distance = new_Distance
        sequence_names = new_sequence_names

    return results

UPGMA = upgma(Distance, sequence_names)



def upgma_to_string(UPGMA):
    Newick = UPGMA[-1][2]
    while len(UPGMA)>0:
        last = UPGMA.pop()
        substring = '(' + last[0] + ':' + str(last[3]) + ',' + last[1] + ':' + str(last[3]) + ')'
        Newick = Newick.replace(last[2], substring)

    return Newick

print(upgma_to_string(UPGMA))

