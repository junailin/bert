#!/bin/sh
export BERT_BASE_DIR=/home/juncsu/Code/Model/uncased_L-12_H-768_A-12
export GLUE_DIR=/home/juncsu/Code/Data/CapsData/mr-2005
rm -rf /home/juncsu/Code/Data/Temp/mrpc_output/*

python run_classifier_v2.py \
    --task_name=MRPC \
    --do_train=true \
    --do_eval=true \
    --do_predict=true \
    --caps_iter=10 \
    --data_dir=$GLUE_DIR \
    --vocab_file=$BERT_BASE_DIR/vocab.txt \
    --bert_config_file=$BERT_BASE_DIR/bert_config.json \
    --init_checkpoint=$BERT_BASE_DIR/bert_model.ckpt \
    --max_seq_length=40 \
    --train_batch_size=20 \
    --learning_rate=2e-5 \
    --num_train_epochs=3.0 \
    --output_dir=/home/juncsu/Code/Data/Temp/mrpc_output/

