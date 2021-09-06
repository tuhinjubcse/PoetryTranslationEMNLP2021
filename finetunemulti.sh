python ./transformers/examples/seq2seq/run_translation.py \
    --model_name_or_path facebook/mbart-large-50-many-to-one-mmt \
    --do_train \
    --do_eval \
    --source_lang nl_XX \
    --target_lang en_XX \
    --output_dir ./output/ \
    --per_device_train_batch_size=32 \
    --per_device_eval_batch_size=4 \
    --overwrite_output_dir \
    --predict_with_generate \
    --max_val_samples 2000 \
    --gradient_accumulation_steps 1\
    --num_train_epochs 3 \
    --save_strategy epoch \
    --evaluation_strategy epoch

#change parameters for non-poetic data based on paper
# gradient_accumulation_steps to 10 and batch size to 8