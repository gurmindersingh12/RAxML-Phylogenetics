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
    -p 12345: Random seed for parsimony starting tree.
    -# 100: Number of bootstrap replicates to assess tree stability.
    -m PROTGAMMAJTT: Specifies the evolutionary model (PROTGAMMAJTT for protein data).
    -s Exo70_aligned.aln: Specifies the input alignment file.
    -n Exo70_tree: Names the output files.
    -T 32: Uses 32 threads for faster computation.




