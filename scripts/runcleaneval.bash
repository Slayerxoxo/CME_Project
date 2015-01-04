#! /bin/bash

######################################################################
### Script de lancement du programme cleaneval sur tous les corpus ###
######################################################################

### Corpus el
python cleaneval.py -t ../corpus/html_killer/el/ ../corpus/source/el/gold/ > ../results/html_killer/corpus_el_all_files.txt
python cleaneval.py ../corpus/html_killer/el/ ../corpus/source/el/gold/ > ../results/html_killer/corpus_el_each_files.txt
echo "corpus el : done"

### Corpus en
python cleaneval.py -t ../corpus/html_killer/en/ ../corpus/source/en/gold/ > ../results/html_killer/corpus_en_all_files.txt
python cleaneval.py ../corpus/html_killer/en/ ../corpus/source/en/gold/ > ../results/html_killer/corpus_en_each_files.txt
echo "corpus en : done"

### Corpus pl
python cleaneval.py -t ../corpus/html_killer/pl/ ../corpus/source/pl/gold/ > ../results/html_killer/corpus_pl_all_files.txt
python cleaneval.py ../corpus/html_killer/pl/ ../corpus/source/pl/gold/ > ../results/html_killer/corpus_pl_each_files.txt
echo "corpus pl : done"

### Corpus ru
python cleaneval.py -t ../corpus/html_killer/ru/ ../corpus/source/ru/gold/ > ../results/html_killer/corpus_ru_all_files.txt
python cleaneval.py ../corpus/html_killer/ru/ ../corpus/source/ru/gold/ > ../results/html_killer/corpus_ru_each_files.txt
echo "corpus ru : done"

### Corpus zh
python cleaneval.py -t ../corpus/html_killer/zh/ ../corpus/source/zh/gold/ > ../results/html_killer/corpus_zh_all_files.txt
python cleaneval.py ../corpus/html_killer/zh/ ../corpus/source/zh/gold/ > ../results/html_killer/corpus_zh_each_files.txt
echo "corpus zh : done"
