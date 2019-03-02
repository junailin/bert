#!/bin/sh
export BERT_BASE_DIR=/home/juncsu/Code/Model/uncased_L-12_H-768_A-12
export GLUE_DIR=/home/juncsu/Code/Data/GlueData/SST-2
export TRAINED_CLASSIFIER=/home/juncsu/Code/Data/Temp/mrpc_output/model.ckpt-749
rm -rf /home/juncsu/Code/Data/Temp/mrpc_eval/*

python run_classifier_v2.py \
    --task_name=MRPC \
    --do_train=false \
    --do_eval=true \
    --do_predict=true \
    --caps_iter=10 \
    --data_dir=$GLUE_DIR \
    --vocab_file=$BERT_BASE_DIR/vocab.txt \
    --bert_config_file=$BERT_BASE_DIR/bert_config.json \
    --init_checkpoint=$TRAINED_CLASSIFIER \
    --max_seq_length=150 \
    --train_batch_size=32 \
    --learning_rate=2e-5 \
    --num_train_epochs=1.0 \
    --output_dir=/home/juncsu/Code/Data/Temp/mrpc_eval/

