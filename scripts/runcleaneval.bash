#! /bin/bash

######################################################################
### Script de lancement du programme cleaneval sur tous les corpus ###
######################################################################

### Corpus el
python cleaneval.py -t ../corpus/boilerpipe/getHtml/el/ ../corpus/source/el/gold/ > ../results/boilerpipehtml/corpus_el_all_files.txt
python cleaneval.py ../corpus/boilerpipe/getHtml/el/ ../corpus/source/el/gold/ > ../results/boilerpipehtml/corpus_el_each_files.txt
echo "corpus el : done"

### Corpus en
python cleaneval.py -t ../corpus/boilerpipe/getHtml/en/ ../corpus/source/en/gold/ > ../results/boilerpipehtml/corpus_en_all_files.txt
python cleaneval.py ../corpus/boilerpipe/getHtml/en/ ../corpus/source/en/gold/ > ../results/boilerpipehtml/corpus_en_each_files.txt
echo "corpus en : done"

### Corpus pl
python cleaneval.py -t ../corpus/boilerpipe/getHtml/pl/ ../corpus/source/pl/gold/ > ../results/boilerpipehtml/corpus_pl_all_files.txt
python cleaneval.py ../corpus/boilerpipe/getHtml/pl/ ../corpus/source/pl/gold/ > ../results/boilerpipehtml/corpus_pl_each_files.txt
echo "corpus pl : done"

### Corpus ru
python cleaneval.py -t ../corpus/boilerpipe/getHtml/ru/ ../corpus/source/ru/gold/ > ../results/boilerpipehtml/corpus_ru_all_files.txt
python cleaneval.py ../corpus/boilerpipe/getHtml/ru/ ../corpus/source/ru/gold/ > ../results/boilerpipehtml/corpus_ru_each_files.txt
echo "corpus ru : done"

### Corpus zh
python cleaneval.py -t ../corpus/boilerpipe/getHtml/zh/ ../corpus/source/zh/gold/ > ../results/boilerpipehtml/corpus_zh_all_files.txt
python cleaneval.py ../corpus/boilerpipe/getHtml/zh/ ../corpus/source/zh/gold/ > ../results/boilerpipehtml/corpus_zh_each_files.txt
echo "corpus zh : done"
