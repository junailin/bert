#!/bin/sh
export BERT_BASE_DIR=/home/juncsu/Code/Model/uncased_L-12_H-768_A-12                                                                     
export GLUE_DIR=/home/juncsu/Code/Data/GlueData/SST-2

echo 'Who was Jim Henson ? ||| Jim Henson was a puppeteer' > /home/juncsu/temp/input.txt
python extract_features.py \
    --input_file=/home/juncsu/temp/input.txt \
    --output_file=/home/juncsu/temp/output.txt \
    --vocab_file=$BERT_BASE_DIR/vocab.txt \
    --bert_config_file=$BERT_BASE_DIR/bert_config.json \
    --init_checkpoint=$BERT_BASE_DIR/bert_model.ckpt \
    --layers=-1,-2,-3,-4 \
    --max_seq_length=128 \
    --batch_size=8
