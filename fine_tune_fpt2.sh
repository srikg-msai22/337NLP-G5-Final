export TRAIN_FILE=woz.train_b.txt
export TEST_FILE=woz.test_b.txt
python3 run_clm.py --output_dir=./b --model_type=gpt2 --model_name_or_path=gpt2 --train_file=$TRAIN_FILE --do_train --validation_file=$TEST_FILE --do_eval --save_total_limit 10 --num_train_epochs 10 --block_size 200
