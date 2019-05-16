
seq1 = "AAAGGGTTT"

seq2 = "AAAGGTTTT"

def hammingDistance(seq1, seq2):
    distance = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            distance += 1
    return distance

print(hammingDistance(seq1, seq2))









