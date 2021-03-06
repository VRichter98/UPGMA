# **UPGMA**


This implementation calculates sequences in fastafile format into the newick format. The distances between the sequences are calculated by [Hamming Distance](https://en.wikipedia.org/wiki/Hamming_distance)

## How to use:

### Prerequisite
- Python 3

### Installation
- Make new diretory
- Download and save UPGMA.py in your new directory
- Download and save your sequences of interest as a fasta file. [Here is an example for fasta file](http://www.cbs.dtu.dk/services/NetGene2/fasta.php)
- Make sure that the fasta file is also in your new directory

### Input
If you start running the program in command line, it needs the name of the fastafile. Please, insert this name in command line as follows: 

```bash
python3 UPGMA.py -input FILENAME.fasta
```

For help use this command:

```bash
python3 UPGMA.py -h
```

### Output
The output is in newick format. Now it is possible to copy the output and paste it in the field for newick format on this website: [Newick Treeviewer](http://etetoolkit.org/treeview/)

Example of newick format:
```bash
((((seqD:0.5,seqA:0.5):0.75,seqE:0.75):1.375,(seqC:0.5,seqB:0.5):1.375):3.0,seqF:3.0)
```

Finally press the button : _View tree!_ and and the tree gets visual.
