# CSCI-662-Project
This is a reproduction study conducted on the paper : Automatic Identification and Classification of Bragging in Social Media (https://aclanthology.org/2022.acl-long.273.pdf)
The results on this study aligns with the claims made on the original paper.
The dataset used in this study: https://archive.org/details/bragging_data

1. Work folder consists of all the codes used for this study
2. Work/Existing Work folder consists of the codes received from the original study
3. bragging_data folder contains the original dataset, plus the additional dataset injected on the original data

**Description of the codes (inside work folder)**
1. binary_bertweet_liwc.ipynb is the slightly modified file that we recieved from the authors and used to reproduce the result
2. binary_bert.ipynb, binary_bertweet.ipynb, binary_roberta.ipynb are the codes that we modified to reproduce the base models
3. data.py consists of the newly collected data
4. write_excel.py is used to pre-process the text on the newly collected tweets according to the description on the original paper
5. classifier.py is the main file that will run the experiments. The file requires following parameteres:
    parser.add_argument('-i', type=str, help='training file')
    parser.add_argument('-o', type=str, help='output model file')
    parser.add_argument('-b', type=str, help='Batch size')
    parser.add_argument('-l', type=str, help='learning rate')
    parser.add_argument('-e', type=str, help='number of epoch')
    parser.add_argument('-m', type=str, help='model selection, 1= bert, 2=roberta, 3= bertweet, 4= bertweet-liwc')
  
Sample command to run the file: **python3 classifier.py -i bragging_data.csv -o bragging.pkl -b 32 -l 3e-6 -e 12 -m 1**

Models link:
https://uscedu-my.sharepoint.com/:f:/g/personal/fabiha_usc_edu/EvOxxCg_WdBAgP6G7xZZvfgBV0uHm16Ak7UXlxOSELxn-w?e=uNJfrX


