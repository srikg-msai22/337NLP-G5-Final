# Service Chatbot

In this project, we built a chatbot for service finding and booking by implementing state-of-the-art text generation models including: GPT-2, GPT-3, XLNet. The best model setup (Fine tuned XLNet for 50 epochs with Beam search decoding) reached a BLEU score of 0.64 and a ROUGE-recall score of 0.53. We also created an ablation study to compare the performance of each model, number of fine-tune epochs, and decoding methods.

## Data

MultiWOZ 2.2 dataset from GitHub (see
https://github.com/budzianowski/multiwoz/tree/master/data/MultiWOZ_2.2).

Data processed in the `make_woz_datasets` function in `woz.py`.

## Exploratory Data Analysis

Run `nlp_eda.py`

## Models

We implemented:
* Pre-trained GPT-2
* Fine tuned GPT-2 for 50 epochs
* Fine tuned GPT-2 for 500 epochs
* Fine tuned Mini GPT-3 for 50 epochs
* Fine tuned XLNet for 50 epochs (best)

Models are fine-tuned in scripts like `fine_tune_fpt2.sh` utilizing Huggingface fine-tuning python file `run_clm.py`.

## Decoding Methods

We implemented:
* Greedy decoding
* Top-p Sampling
* Beam Search (best)

## Reports

See `G5_preliminary.pdf` for a text report and `G5_Chatbot.pdf` for final presentation slides.
