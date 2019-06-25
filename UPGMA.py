import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-input", "--file",  required=True, help="Please place the name of your fasta filename here and make sure that the file is in the same directory as the program ")

fastafile = parser.parse_args()

def hammingDistance(seq1, seq2):
    """
    Calculates the distance between 2 sequences for each sequence against each sequence
    :param seq1: sequence 1
    :param seq2: sequence 2
    :return: distance between two sequences
    """
    sequence_list = list(all_sequences.values())        # Initialize list of all sequences
    longest_sequence = len(max(sequence_list, key=len)) # Get the length of longest sequence

    while len(seq1) < longest_sequence:                 # Fill up the other sequences till all sequences have the same length
        seq1 += "-"
    while len(seq2) < longest_sequence:
        seq2 += "-"
    distance = 0                                        # Set Distance to 0
    for i in range(len(seq1)):                          # Check for each base in the sequences if the same base is in identical locations
        if seq1[i] != seq2[i]:
            distance += 1                               # If not then add +1 to distance
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

fasta_filename = fastafile.file
all_sequences = read_fasta(fasta_filename)

def Pairwise_Hamming(all_sequences):
    """
    Calculate distances by Hamming distances of sequences
    :param all_sequences:
    :return: distance dictionary
    """
    Distance = {}                               # Initialize empty dictionary
    for seq in all_sequences:
        for seq1 in all_sequences:
            if seq == seq1:                     # Ignore the calculation for indentical annotations
                pass
            else:
                Distance[seq, seq1] = hammingDistance(all_sequences[seq], all_sequences[seq1])
    return Distance                             # Append for not identical annotations the hamming distance for each pair

Distance = Pairwise_Hamming(all_sequences)


replacingvalues = ['Omega','Psi','Chi', 'Phi', 'Ypsilon', 'Tau', 'Sigma', 'Rho', 'Pi','Omikron', 'Xi', 'Ny', 'My', 'Lambda', 'Kappa', 'Iota', 'Theta', 'Eta', 'Zeta', 'Epsilon', 'Delta', 'Gamma', 'Beta', 'Alpha']
                                                # List of node names

sequence_names = list(all_sequences.keys())     # List of annotations from fasta file

def upgma(Distance, sequence_names):
    """
    Merges sequences to nodes and calculates their path length
    :param Distance: distance dictionary
    :param sequence_names: list with name of the sequences
    :return: results: list of sequences, with merged name of two paths, with calculated path length
    """
    results = []                                                            # Initialize empty list for final output
    while len(Distance) > 0:
        new_sequence_names = []                                             # Initialize empty list
        new_Distance = {}                                                   # Initialize empty Dictionary
        min_pair = min(Distance, key=Distance.get)                          # Name of both annotaions with the smallest hamming distance
        min_distance = Distance[min(Distance, key=Distance.get)]            # smallest hamming distance

        for annotation in sequence_names:
            if annotation != min_pair[0] and annotation != min_pair[1]:
                new_sequence_names.append(annotation)                       # Append all annotation pairs to new list that are not match with the min_pair
        new_seq_name = replacingvalues.pop()                                # If Word from list of nodes (replacingvalues) is used, pop it
        new_sequence_names.append(new_seq_name)                             # Replace the min_pair annotation with last value from replacingvalue list in new list
        for seq1 in new_sequence_names:
            for seq2 in new_sequence_names:
                if seq1 == seq2:
                    pass                                                    # Ignore identical annotations
                elif (seq1,seq2) in Distance:
                    new_Distance[seq1,seq2] = Distance[seq1,seq2]           # Transfer old annotations to new dictionary
                else:
                    if seq1 in sequence_names:                              # Calculate for sequence with both min_pairs the new distance
                        new_Distance[seq1,seq2] = (Distance[seq1, min_pair[0]] + Distance[seq1, min_pair[1]]) / 2
                    else:
                        new_Distance[seq1, seq2] = (Distance[min_pair[0], seq2] + Distance[min_pair[1], seq2]) / 2
        results.append([min_pair[1],min_pair[0],new_seq_name,min_distance/2])   # Append new annotations to list and compute the path length for for both sequences
        Distance = new_Distance                                             # Reset the old distance dictionary with the new distance dictionary
        sequence_names = new_sequence_names                                 # Reset the old annotaion names with new annotaion names
    return results

UPGMA = upgma(Distance, sequence_names)

def upgma_to_newick(UPGMA):
    """
    Compute from result list the newickformat
    :param UPGMA: list of results from upgma function
    :return: string in newickformat
    """
    Newick = UPGMA[-1][2]                                           # name of the node
    while len(UPGMA)>0:
        last = UPGMA.pop()                                          # last = last list in multilist of UPGMA
        substring = '(' + last[0] + ':' + str(last[3]) + ',' + last[1] + ':' + str(last[3]) + ')'  # Every annotaion gets first path length
        Newick = Newick.replace(last[2], substring)                 # Replacing node names
    return Newick

print(upgma_to_newick(UPGMA))
