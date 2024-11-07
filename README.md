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






