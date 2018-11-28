#!/bin/sh
export BERT_BASE_DIR=/home/juncsu/Code/Model/uncased_L-12_H-768_A-12
export GLUE_DIR=/home/juncsu/Code/Data/GlueData
python run_classifier.py --task_name=MRPC \
    --do_train=true \
    --do_eval=true \
    --data_dir=$GLUE_DIR/MRPC \
    --vocab_file=$BERT_BASE_DIR/vocab.txt \
    --bert_config_file=$BERT_BASE_DIR/bert_config.json \
    --init_checkpoint=$BERT_BASE_DIR/bert_model.ckpt \
    --max_seq_length=128 \
    --train_batch_size=32 \
    --learning_rate=2e-5 \
    --num_train_epochs=1.0 \
    --output_dir=~/temp/mrpc_output/

