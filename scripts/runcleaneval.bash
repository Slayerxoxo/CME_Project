#! /bin/bash

######################################################################
### Script de lancement du programme cleaneval sur tous les corpus ###
######################################################################

### Corpus el
python cleaneval.py -t ../corpus/el/html/ ../corpus/el/gold/ > ../results/cleaneval/corpus_el_all_files.txt
python cleaneval.py ../corpus/el/html/ ../corpus/el/gold/ > ../results/cleaneval/corpus_el_each_files.txt
echo "corpus el : done"

### Corpus en
python cleaneval.py -t ../corpus/en/html/ ../corpus/en/gold/ > ../results/cleaneval/corpus_en_all_files.txt
python cleaneval.py ../corpus/en/html/ ../corpus/en/gold/ > ../results/cleaneval/corpus_en_each_files.txt
echo "corpus en : done"

### Corpus pl
python cleaneval.py -t ../corpus/pl/html/ ../corpus/pl/gold/ > ../results/cleaneval/corpus_pl_all_files.txt
python cleaneval.py ../corpus/pl/html/ ../corpus/pl/gold/ > ../results/cleaneval/corpus_pl_each_files.txt
echo "corpus pl : done"

### Corpus ru
python cleaneval.py -t ../corpus/ru/html/ ../corpus/ru/gold/ > ../results/cleaneval/corpus_ru_all_files.txt
python cleaneval.py ../corpus/ru/html/ ../corpus/ru/gold/ > ../results/cleaneval/corpus_ru_each_files.txt
echo "corpus ru : done"

### Corpus zh
python cleaneval.py -t ../corpus/zh/html/ ../corpus/zh/gold/ > ../results/cleaneval/corpus_zh_all_files.txt
python cleaneval.py ../corpus/zh/html/ ../corpus/zh/gold/ > ../results/cleaneval/corpus_zh_each_files.txt
echo "corpus zh : done"
