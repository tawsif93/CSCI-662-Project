import time
from datetime import datetime

import torch
import argparse
from torch.utils.data import TensorDataset, DataLoader, RandomSampler, SequentialSampler
import pandas as pd
from sklearn.model_selection import StratifiedKFold, train_test_split
import numpy as np
from roberta_classification_model import RobertaClassificationModel
from tensorflow.keras.preprocessing.sequence import pad_sequences
from transformers import RobertaForSequenceClassification, RobertaTokenizer, RobertaModel
from transformers import BertForSequenceClassification, BertTokenizer, BertModel
from transformers import AutoModel, AutoTokenizer
from sklearn import metrics
import torch.nn as nn 
import torch.nn.functional as F
from transformers import AdamW
from sklearn.utils import class_weight

class Classifier:
    def __init__(self):
        pass
    
    def read_process_data(self, features):
        df = pd.read_csv('bragging_data.csv', header=0, names=['id', 'text', 'sampling', 'round_no', 'label'])

        index_training, label_training, features_training = [], [], []
        index_testing, label_testing, features_testing = [], [], []

        texts = df.text.values
        sampling_ways = df.sampling.values
        round_nos = df.round_no.values
        labels = df.label.values

        labels_number = []
        for i in labels:
            if i == "not":
                labels_number.append(0)
            else:
                labels_number.append(1)

        text_testing_print = []
        for i in range(len(sampling_ways)):
            if sampling_ways[i] == 'keyword':
                index_training.append(i)
                label_training.append(labels_number[i])
                features_training.append(features[i])
            else:
                index_testing.append(i)
                text_testing_print.append(texts[i])
                label_testing.append(labels_number[i])
                features_testing.append(features[i])
                
        return index_training, label_training, features_training, index_testing, label_testing, features_testing, text_testing_print
    
    def get_tokenizer(self, selected_model = 1):
        if(selected_model == 1):
            tokenizer = BertTokenizer.from_pretrained('bert-base-uncased', do_lower_case=True)
        elif selected_model == 2:
            tokenizer = RobertaTokenizer.from_pretrained('roberta-base')
        elif selected_model == 3:
            tokenizer = AutoTokenizer.from_pretrained("vinai/bertweet-base", use_fast=False)
        
        return tokenizer
    
    def tokenize(self, texts, MAX_LEN, selectedModel):
        texts = ['[CLS] ' + str(sentence) + ' [SEP]' for sentence in texts]
        
        tokenizer = self.get_tokenizer(selectedModel)
        tokenized_texts = [tokenizer.tokenize(sent) for sent in texts]

        # Use the BERT tokenizer to convert the tokens to their index numbers in the BERT vocabulary
        input_ids = [tokenizer.convert_tokens_to_ids(x) for x in tokenized_texts]

        # Pad input tokens
        input_ids = pad_sequences(input_ids, maxlen=MAX_LEN, dtype='long', truncating='post', padding='post')
        print(input_ids)
        
        return input_ids
        
    def create_attention_mask(self, input_ids):
        # Create attention masks
        attention_masks = []
        for seq in input_ids:
            seq_mask = [float(i>0) for i in seq]
            attention_masks.append(seq_mask)
        
        return attention_masks
    
    def construct_train_test(self, index_training, index_testing, input_ids, attention_masks):
        text_training, text_testing = [], []
        mask_training, mask_testing = [], []
        for i in index_training:
            text_training.append(input_ids[i])
            mask_training.append(attention_masks[i])
        for i in index_testing:
            text_testing.append(input_ids[i])
            mask_testing.append(attention_masks[i])
            
        return text_training, mask_training, text_testing, mask_testing
    
    def getModel(self, selectedModel):
        if(selectedModel == 1):
            model_roberta = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=2)
        elif selectedModel == 2:
            model_roberta = RobertaForSequenceClassification.from_pretrained('roberta-base', num_labels=2)
        elif selectedModel == 3:
            model_roberta = RobertaClassificationModel()

        return model_roberta
         
    def final_step(self, batch_size, n_epoch, lr, selectedModel):
        # batch_size = 32
        # n_epoch = 12
        is_cuda_available = False 
        if torch.cuda.is_available():
            is_cuda_available = True
            
        text_training = self.text_training
        text_testing = self.text_testing
        mask_training = self.mask_training
        mask_testing = self.mask_testing
        
        label_training = self.label_training
        label_testing = self.label_testing
        
        features_training = self.features_training
        features_testing = self.features_testing

        x_train = text_training
        y_train = label_training
        
        print(len(x_train))
        
        if selectedModel == 3:
            x_dev, x_testing, y_dev, y_testing, features_dev, features_testing, mask_dev, mask_testing = train_test_split(text_testing, label_testing, features_testing, mask_testing, test_size=0.8, random_state=0, stratify=label_testing)
        else:
            x_dev, x_testing, y_dev, y_testing = train_test_split(text_testing, label_testing, test_size=0.8, random_state=0, stratify=label_testing)


        # sklearn
        weight_loss = class_weight.compute_class_weight(class_weight='balanced', classes=np.unique(y_train), y=y_train)
        #weight_loss = torch.tensor(weight_loss, dtype=torch.float32).cpu()
        
        if(is_cuda_available):
            weight_loss = torch.tensor(weight_loss, dtype=torch.float32).cuda()
        else:
            weight_loss = torch.tensor(weight_loss, dtype=torch.float32).cpu()
            
        #model_roberta = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=2).cpu()
        #model_roberta = RobertaForSequenceClassification.from_pretrained('roberta-base', num_labels=2).cuda()
        #model_roberta = RobertaClassificationModel().cpu()
        #model_roberta.cuda()
        
        model_roberta = self.getModel(selectedModel)
        if is_cuda_available:
            model_roberta.cuda()
        else:
            model_roberta.cpu()
        

        param_optimizer = list(model_roberta.named_parameters())
        no_decay = ['bias', 'LayerNorm.weight']        
            
        optimizer_grouped_parameters = [
                {'params': [p for n, p in model_roberta.named_parameters() if not any(nd in n for nd in no_decay)], 'weight_decay': 0.01},
                {'params': [p for n, p in model_roberta.named_parameters() if any(nd in n for nd in no_decay)], 'weight_decay': 0.0}
                ]

        optimizer = AdamW(optimizer_grouped_parameters, lr)
        criterion = nn.CrossEntropyLoss(weight=weight_loss, size_average=None, ignore_index=-100, reduce=None, reduction='mean')

        x_train = torch.LongTensor(x_train)
        x_dev = torch.LongTensor(x_dev)

        y_train = torch.LongTensor(y_train)
        y_dev = torch.LongTensor(y_dev)

        features_train = torch.FloatTensor(features_training)
        features_dev = torch.FloatTensor(features_dev)

        mask_train = torch.LongTensor(mask_training)
        mask_dev = torch.LongTensor(mask_dev)

        # Pack to dataLoader
        train_data = TensorDataset(x_train, features_train, mask_train, y_train) if selectedModel == 3 else TensorDataset(x_train, mask_train, y_train)
        # train_data = TensorDataset(x_train, features_train, mask_train, y_train)
        train_sampler = RandomSampler(train_data)
        train_dataloader = DataLoader(train_data, sampler=train_sampler, batch_size=batch_size)
            
        # dev_data = TensorDataset(x_dev, features_dev, mask_dev, y_dev)
        dev_data = TensorDataset(x_dev, features_dev, mask_dev, y_dev) if selectedModel == 3 else TensorDataset(x_dev, mask_dev, y_dev)
        dev_sampler = RandomSampler(dev_data)
        dev_dataloader = DataLoader(dev_data, sampler=dev_sampler, batch_size=batch_size) 

        # Initialize previous dev loss
        previous_valid_loss = 1000

        for epoch in range(n_epoch):
            print(epoch)
            start_time = time.perf_counter()
            cur_time = datetime.now().strftime('%m-%d-%H:%M:%S')

            # Training
            model_roberta.train()

            train_losses = []
            valid_losses = []

            for step, batch in enumerate(train_dataloader):
                # Add batch to GPU
                batch = tuple(t.to(self.device) for t in batch)

                if(selectedModel == 3):
                    b_input_ids, b_input_features, b_input_mask, b_labels = batch
                    optimizer.zero_grad()
                    outputs = model_roberta(input_ids=b_input_ids, input_feature=b_input_features, attention_mask=b_input_mask, labels=b_labels)
                else:
                    b_input_ids, b_input_mask, b_labels = batch
                    optimizer.zero_grad()
                    outputs = model_roberta(input_ids=b_input_ids, attention_mask=b_input_mask, labels=b_labels)
                # Unpack the inputs from dataloader
                #b_input_ids, b_input_features, b_input_mask, b_labels = batch

                # Clear out the gradients (by default they accumulate)
                #optimizer.zero_grad()
                
                # Generate combined representations      

                
                #outputs = model_roberta(input_ids=b_input_ids, input_feature=b_input_features, attention_mask=b_input_mask, labels=b_labels)
                #outputs = model_roberta(input_ids= b_input_ids, labels=b_labels)
                loss = outputs[0]
                logits = outputs[1]
                #loss = criterion(logits, b_labels)


                # Backward pass
                loss.backward()

                # track train loss
                train_losses.append(loss.item())

                # Update parameters and take a step using the computed gradient
                optimizer.step()
                
            train_loss = np.average(train_losses)
            print('train loss: {}'.format(train_loss))

            # Validation
            model_roberta.eval()

            predictions = []
            targets = []


            # Evaluate data for one epoch
            for batch in dev_dataloader:
                # Add batch to GPU
                batch = tuple(t.to(self.device) for t in batch)

                # Unpack the inputs from dataloader
                # b_input_ids, b_input_features, b_input_mask, b_labels = batch
                
                if(selectedModel == 3):
                    b_input_ids, b_input_features, b_input_mask, b_labels = batch
                else:
                    b_input_ids, b_input_mask, b_labels = batch
                    
                
            
                with torch.no_grad():

                    # Generate combined representations
                    
                    #outputs = model_roberta(input_ids=b_input_ids, input_feature=b_input_features, attention_mask=b_input_mask, labels=b_labels)
                    # outputs = model_roberta(input_ids=b_input_ids, labels=b_labels)
                    
                    if(selectedModel == 3):
                        outputs = model_roberta(input_ids=b_input_ids, input_feature=b_input_features, attention_mask=b_input_mask, labels=b_labels)
                    else:
                        outputs = model_roberta(input_ids=b_input_ids, attention_mask=b_input_mask, labels=b_labels)
                    
                    loss = outputs[0]
                    logits = outputs[1]
                    #loss = criterion(logits, b_labels)
                

                valid_losses.append(loss.item())

                # Move logits and labels to CPU
                logits = logits.detach().cpu().numpy()
                
                labels = b_labels.to('cpu').numpy() 

                predictions = np.append(predictions, np.argmax(logits, axis=1))
                targets = np.append(targets, labels) 

            # Calculate total dev loss 
            valid_loss = np.average(valid_losses)
            print('valid loss: {}'.format(valid_loss))

            # Calculate dev f1 of sverity
            dev_f1 = metrics.f1_score(targets, predictions, average='macro', zero_division=1)
            print("dev_f1:", dev_f1)


            # Save the best model based on dev loss
            if valid_loss < previous_valid_loss:
                previous_valid_loss = valid_loss
                torch.save(model_roberta, './bragging.pkl')
                print("saved")

            after_training = time.perf_counter()
            print(f"Spent {after_training - start_time} seconds.")             
        
        x_testing = torch.LongTensor(x_testing)
        y_testing = torch.LongTensor(y_testing)
        features_testing = torch.FloatTensor(features_testing)
        mask_testing = torch.LongTensor(mask_testing)
            
        # test_data = TensorDataset(x_testing, features_testing, mask_testing, y_testing) 
        test_data = TensorDataset(x_testing, features_testing, mask_testing, y_testing) if selectedModel == 3 else TensorDataset(x_testing, mask_testing, y_testing)
        test_sampler = SequentialSampler(test_data)
        test_dataloader = DataLoader(test_data, sampler=test_sampler, batch_size=batch_size)

        # Testing
        bragging_model = torch.load('./bragging.pkl')

        test_predictions = []
        test_targets = []
        bragging_model.eval()

        for batch in test_dataloader:
            # Add batch to GPU
            batch = tuple(t.to(self.device) for t in batch)
            # Unpack the inputs from dataloader
            # b_input_ids, b_input_features, b_input_mask, b_labels = batch
            
            if(selectedModel == 3):
                b_input_ids, b_input_features, b_input_mask, b_labels = batch
            else:
                b_input_ids, b_input_mask, b_labels = batch
            
            with torch.no_grad():
                # Forward pass, calculate logit predictions
                #outputs = bragging_model(input_ids=b_input_ids, input_feature=b_input_features, attention_mask=b_input_mask)
                # outputs = bragging_model(input_ids=b_input_ids)
                if(selectedModel == 3):
                    outputs = bragging_model(input_ids=b_input_ids, input_feature=b_input_features, attention_mask=b_input_mask)
                else:
                    outputs = bragging_model(input_ids=b_input_ids, attention_mask=b_input_mask)
                logits = outputs[0]
            # Move logits and labels to CPU
            logits = logits.detach().cpu().numpy()
            labels = b_labels.to('cpu').numpy()

            test_predictions = np.append(test_predictions, np.argmax(logits, axis=1))
            test_targets = np.append(test_targets, labels)

        test_acc = metrics.accuracy_score(test_targets, test_predictions)
        test_precision = metrics.precision_score(test_targets, test_predictions, average="macro", zero_division=1)
        test_recall = metrics.recall_score(test_targets, test_predictions, average="macro", zero_division=1)
        test_f1 = metrics.f1_score(test_targets, test_predictions, average="macro", zero_division=1)
        print("test_acc:", test_acc)
        print("test_precision:", test_precision)
        print("test_recall:", test_recall)
        print("test_f1:", test_f1)

        target_names = ['class 0', 'class 1']
        print(metrics.classification_report(test_targets, test_predictions, target_names=target_names))
        
        
    def main(self, batch_size = 32, n_epoch = 12, lr =3e-6, selectedModel = 3, training_data = '../bragging_data/bragging_data.csv'):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        # n_gpu = torch.cuda.device_count()
        # torch.cuda.get_device_name(0)
        
        
        # linguistic features
        df = pd.read_csv('./LIWC2015_Results_1.csv', header=None)
        features = np.array(df.loc[:, 1:])
        print(features.shape) # (6696, 93)
        
        
        # Set the maximum sequence length
        MAX_LEN = 50
        
        
        df = pd.read_csv(training_data, header=0, names=['id', 'text', 'sampling', 'round_no', 'label'])

        index_training, self.label_training, self.features_training = [], [], []
        index_testing, self.label_testing, self.features_testing = [], [], []

        texts = df.text.values
        sampling_ways = df.sampling.values
        round_nos = df.round_no.values
        labels = df.label.values

        labels_number = []
        for i in labels:
            if i == "not":
                labels_number.append(0)
            else:
                labels_number.append(1)

        text_testing_print = []
        for i in range(len(sampling_ways)):
            if sampling_ways[i] == 'keyword':
                index_training.append(i)
                self.label_training.append(labels_number[i])
                self.features_training.append(features[i])
            else:
                index_testing.append(i)
                text_testing_print.append(texts[i])
                self.label_testing.append(labels_number[i])
                self.features_testing.append(features[i])
                
        
        input_ids = self.tokenize(texts, MAX_LEN, selectedModel)
        attention_masks = self.create_attention_mask(input_ids)
        self.text_training, self.mask_training, self.text_testing, self.mask_testing = self.construct_train_test(index_training, index_testing, input_ids, attention_masks)
        
        self.final_step(batch_size, n_epoch, lr, selectedModel)
        

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', type=str, help='training file')
    parser.add_argument('-o', type=str, help='output model file')
    parser.add_argument('-b', type=str, help='Batch size')
    parser.add_argument('-l', type=str, help='learning rate')
    parser.add_argument('-e', type=str, help='number of epoch')
    parser.add_argument('-m', type=str, help='model selection, 1= bert, 2=roberta, 3= bertweet, 4= bertweet-liwc')
    args = parser.parse_args()

    classifier = Classifier()
    # classifier.main(batch_size = args.b, n_epoch = args.e, lr = args.l, selectedModel = args.m, training_data = args.i)
    classifier.main()

    

    