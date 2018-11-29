#!/bin/sh
export BERT_BASE_DIR=/home/juncsu/Code/Model/uncased_L-12_H-768_A-12
export GLUE_DIR=/home/juncsu/Code/Data/GlueData/SST-2
export TRAINED_CLASSIFIER=/home/juncsu/temp/mrpc_output/model.ckpt-229
python run_classifier.py --task_name=MRPC \
    --do_predict=true \
    --data_dir=$GLUE_DIR \
    --vocab_file=$BERT_BASE_DIR/vocab.txt \
    --bert_config_file=$BERT_BASE_DIR/bert_config.json \
    --init_checkpoint=$TRAINED_CLASSIFIER \
    --max_seq_length=128 \
    --output_dir=/home/juncsu/temp/mrpc_output_p/

