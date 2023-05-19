from sklearn.model_selection import train_test_split
import csv
import torch
from transformers import BertTokenizerFast, BertForSequenceClassification, Trainer, TrainingArguments

 

# Suppose 'texts' is a list of strings, and 'labels' is a list of integers representing classes (0: non-fraudulent, 1: fraudulent)
def read_csv(file_path):
    texts = []
    labels = []
    with open(file_path, "r", encoding="latin-1") as file:
        file.readline()
        reader = csv.reader(file)
        for row in reader:
            texts.append(row[0])  # Assuming text is in the first column (index 0)
            labels.append(int(row[1]))  # Assuming labels are in the second column (index 1)
    return texts, labels

# Path to your CSV file
csv_file = "./data/fraud_email_.csv"

# Read texts and labels from the CSV file
texts, labels = read_csv(csv_file)
 

# Load BERT tokenizer

tokenizer = BertTokenizerFast.from_pretrained('bert-base-uncased')

 

# Tokenize the texts

encodings = tokenizer(texts, truncation=True, padding=True)

 

# Split data into training and validation sets

train_texts, val_texts, train_labels, val_labels = train_test_split(encodings['input_ids'], labels, test_size=0.2)

 

# Load BERT model

model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=2)  # Binary classification

 

# Define training arguments

training_args = TrainingArguments(

    output_dir='./results',

    num_train_epochs=3,

    per_device_train_batch_size=16,

    per_device_eval_batch_size=64,

    warmup_steps=500,

    weight_decay=0.01,

    logging_dir='./logs',

)

 

# Define Trainer and train the model

trainer = Trainer(

    model=model,

    args=training_args,

    train_dataset=(train_texts, train_labels),

    eval_dataset=(val_texts, val_labels),

)

trainer.train()

 

# After training, you can use the model for prediction as follows:

test_text = "Some test text..."

test_encodings = tokenizer([test_text], truncation=True, padding=True, return_tensors="pt")

pred = model(**test_encodings)