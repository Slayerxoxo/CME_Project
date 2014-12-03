#! /bin/bash

######################################################################
### Script de lancement du programme cleaneval sur tous les corpus ###
######################################################################

### Corpus el
python cleaneval.py -t ../corpus/readability/el/html/ ../corpus/readability/el/gold/ > ../results/readability/corpus_el_all_files.txt
python cleaneval.py ../corpus/readability/el/html/ ../corpus/readability/el/gold/ > ../results/readability/corpus_el_each_files.txt
echo "corpus el : done"

### Corpus en
python cleaneval.py -t ../corpus/readability/en/html/ ../corpus/readability/en/gold/ > ../results/readability/corpus_en_all_files.txt
python cleaneval.py ../corpus/readability/en/html/ ../corpus/readability/en/gold/ > ../results/readability/corpus_en_each_files.txt
echo "corpus en : done"

### Corpus pl
python cleaneval.py -t ../corpus/readability/pl/html/ ../corpus/readability/pl/gold/ > ../results/readability/corpus_pl_all_files.txt
python cleaneval.py ../corpus/readability/pl/html/ ../corpus/readability/pl/gold/ > ../results/readability/corpus_pl_each_files.txt
echo "corpus pl : done"

### Corpus ru
python cleaneval.py -t ../corpus/readability/ru/html/ ../corpus/readability/ru/gold/ > ../results/readability/corpus_ru_all_files.txt
python cleaneval.py ../corpus/readability/ru/html/ ../corpus/readability/ru/gold/ > ../results/readability/corpus_ru_each_files.txt
echo "corpus ru : done"

### Corpus zh
python cleaneval.py -t ../corpus/readability/zh/html/ ../corpus/readability/zh/gold/ > ../results/readability/corpus_zh_all_files.txt
python cleaneval.py ../corpus/readability/zh/html/ ../corpus/readability/zh/gold/ > ../results/readability/corpus_zh_each_files.txt
echo "corpus zh : done"
