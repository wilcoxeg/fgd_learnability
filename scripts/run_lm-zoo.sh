#!/bin/bash

echo "getting ngram surprisals"
lm-zoo get-surprisals ngram ../data/sample_suites/test_sents.txt > ../data/model_output/ngram_output.txt

echo "getting gpt2 surprisals"
lm-zoo get-surprisals gpt2 ../data/sample_suites/test_sents.txt > ../data/model_output/gpt2_output.txt

echo "getting grnn surprisals"
lm-zoo get-surprisals GRNN ../data/sample_suites/test_sents.txt > ../data/model_output/grnn_output.txt

echo "getting jrnn surprisals"
lm-zoo get-surprisals JRNN ../data/sample_suites/test_sents.txt > ../data/model_output/jrnn_output.txt