```
conda init
```
```
source ~/.bashrc
```
```
conda activate RAxML
```
```
muscle -in exo-new.txt -out Exo70_aligned.aln
```
```
raxmlHPC -f a -x 12345 -p 12345 -# 1000 -m PROTGAMMAJTT -s Exo70_aligned.aln -n Exo70_tree -T 32
```
