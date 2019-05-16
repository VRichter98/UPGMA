

filename = 'sequence.fasta'

def read_concat_sequences(filename):
    """
    Read all sequences from FASTA file into single string.
    :param filename: path to FASTA file
    :return: a string containing the concatenated sequences
    """
    fasta_file = open(filename)
    sequences = ""                      # Initialize empty sequence
    for line in fasta_file:
        line = line.replace("\r", "").replace("\n", "")  # Remove carriage return and newline
        if line.startswith(">"):
            pass                        # Ignore annotation after ">"
        elif line.startswith(";"):
            pass                        # Ignore chain information after ";"
        else:
            sequences += line           # Append sequence with line
    fasta_file.close()
    return sequences

print(read_concat_sequences(filename))