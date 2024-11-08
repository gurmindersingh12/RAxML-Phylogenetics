# RAxML-Phylogenetics

## Exo70 Phylogenetic Analysis Workflow

This document outlines all steps, commands, and modifications used for analyzing the Exo70 gene family. Each step is explained in detail for reproducibility and to ensure clarity for anyone using this guide.

## Step 1: Setting Up the Environment

### 1.1 Download and Install Miniconda

Miniconda is a minimal version of Anaconda that simplifies managing Python environments and packages. We used Miniconda to install all necessary tools in a controlled environment, which avoids conflicts with other software.

1. Download Miniconda:
```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
```

2. Install Miniconda: This installation specifies a custom path for Miniconda, which can be particularly useful on shared systems.
```
bash Miniconda3-latest-Linux-x86_64.sh -b -p /mmfs1/home/g.singh/miniconda3

```

3. Add Miniconda to the system PATH:
```
echo 'export PATH="/mmfs1/home/g.singh/miniconda3/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

### 1.2 Verify Conda Installation
After installing Miniconda, verify the Conda installation:
```
conda --version
```

### 1.3 Create and Activate a Conda Environment
We create a Conda environment named RAxML to install all required packages:
```
conda create -n RAxML
conda activate RAxML
```


## Step 2: Installing Required Packages

### 2.1 Install RAxML and MUSCLE

To perform the phylogenetic analysis, we need RAxML (for tree construction) and MUSCLE (for sequence alignment):

```
conda install -c bioconda raxml muscle
```

### 2.2 Additional Python Packages

To handle node labeling and data processing, we install additional Python packages:

```
pip install biopython ete3
```

## Step 3: Sequence Alignment

Align the Exo70 sequences using MUSCLE.

#### Initial Attempt with PHYI Format:

```
muscle -in Exo70_HvTaOsOtZmSiSbBd_5_SH.fa -out Exo70_aligned.phy -phyi
```

However, PHYLIP format truncated sequence names to only the first 10 characters, which led to data loss in the labels. To prevent this truncation and retain full sequence names, we switched to the ALN format, which preserves the entire name:

```
muscle -in Exo70_HvTaOsOtZmSiSbBd_5_SH.fa -out Exo70_aligned.aln
```
The ALN format is more flexible and avoids this name-truncation issue, making it compatible with downstream tools and preserving the full identifiers.

## Step 4: Constructing a Phylogenetic Tree with RAxML
With the aligned sequences (Exo70_aligned.aln), we can now construct a phylogenetic tree using RAxML.
### 4.1 Run RAxML
```
raxmlHPC -f a -x 12345 -p 12345 -# 100 -m PROTGAMMAJTT -s Exo70_aligned.aln -n Exo70_tree -T 32
```
#### Explanation of Parameters:

1. `-f a`: Conducts a rapid bootstrap analysis and a search for the best-scoring tree.
2. `-x 12345`: Random seed for bootstrapping.
3. `-p 12345`: Random seed for parsimony starting tree.
4. `-# 100`: Number of bootstrap replicates to assess tree stability.
5. `-m PROTGAMMAJTT`: Specifies the evolutionary model (PROTGAMMAJTT for protein data).
6. `-s Exo70_aligned.aln`: Specifies the input alignment file.
7. `-n Exo70_tree`: Names the output files.
8. `-T 32`: Uses 32 threads for faster computation.

<b>Note:</b> Use `-m GTRGAMMA`: Sets the evolutionary model to GTRGAMMA, if using nucleotide data. This model:
For nucleotide data, use GTRGAMMA as shown above instead of PROTGAMMAJTT, which is specific to protein data.


### 4.2 Output Files

RAxML produces several files:
1. `RAxML_bestTree.Exo70_tree`: Best-scoring maximum likelihood tree.
2. `RAxML_bootstrap.Exo70_tree`: Contains all bootstrap trees.
3. `RAxML_bipartitions.Exo70_tree`: Final tree with bootstrap values.

## Step 5: Node Label Extraction and Renaming

To work with the phylogenetic tree structure and label nodes, we used custom Python scripts from the QKphylogeny package.

### 5.1 Cloning QKphylogeny Repository

Download QKphylogeny from GitHub to access the scripts:

```
git clone https://github.com/gurmindersingh12/QKphylogeny.git
```

### 5.2 Extract Node Labels

The QKphylogeny_nodelabels.py script extracts node labels from the RAxML tree file in Newick format.
```
python QKphylogeny/QKphylogeny_nodelabels.py -t RAxML_bestTree.Exo70_tree -o node_labels.txt
```

#### Modifications in QKphylogeny_nodelabels.py for Python 3 Compatibility: The original script used outdated syntax from Python 2. We made the following changes:

1. Changed `string.replace(line, '\n', '')` to `line.replace('\n', '')`.
2. Changed `string.split(line)` to `line.split()`.
3. Changed `string.replace(tree, '(', '')` to `tree.replace('(', '')`.
4. Changed `string.split(node, ':')[0]` to `node.split(':')[0]`.

These modifications were necessary for the script to run in Python 3.


### 5.3 Rename Nodes (Optional)

If you need to rename nodes based on a specific format or abbreviation, create a translation table (translation_table.txt) with two columns:

1. Original name
2. New name

Then use the renaming script:
```
python QKphylogeny/QKphylogeny_rename_nodes.py -t RAxML_bestTree.Exo70_tree -l translation_table.txt -o renamed_tree.newick
```

## Step 6: Alignment Quality Assessment (Optional)
To improve alignment quality, filter out poorly aligned positions using `QKphylogeny_alignment_analysis.py`. Set a threshold for data completeness, such as allowing a maximum of 20% missing data:

```
python QKphylogeny/QKphylogeny_alignment_analysis.py -a Exo70_aligned.aln -d 0.2 -t protein -o Exo70_aligned_filtered.aln
```

#### Explanation:

1. `-a Exo70_aligned.aln`: Input alignment file.
2. `-d 0.2`: Removes columns where more than 20% of data is missing.
3. `-t protein`: Specifies the sequence type as protein.
4. `-o Exo70_aligned_filtered.aln`: Outputs the filtered alignment.


## Step 7: Visualization and Interpretation

To visualize the final phylogenetic tree, you can upload the Newick tree file (e.g., `RAxML_bestTree.Exo70_tree` or `renamed_tree.newick`) to iTOL (https://itol.embl.de/). iTOL provides interactive options to customize, annotate, and download high-quality phylogenetic trees.




