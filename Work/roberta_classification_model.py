import torch
from transformers import AutoModel
import torch.nn as nn
from attn_gating import AttnGating
from transformers import BertForSequenceClassification, BertTokenizer, BertModel


class RobertaClassificationModel(nn.Module):
    def __init__(self):
        super(RobertaClassificationModel, self).__init__()

        self.embedding_roberta = AutoModel.from_pretrained("vinai/bertweet-base", output_hidden_states=True)
        self.attn_gate = AttnGating()

        self.roberta = AutoModel.from_pretrained("vinai/bertweet-base", return_dict=True)

        self.dropout = nn.Dropout(0.2)
        #self.relu = nn.ReLU(inplace=True)

        self.num_labels_bragging = 2
      
        self.classifier_bragging = nn.Linear(768, 2)
        

    def forward(self, input_ids, input_feature, attention_mask, labels=None):

        embedding_roberta = self.embedding_roberta(input_ids)
        #last_hidden_state, pooler_output, all_hidden_states = self.embedding_roberta(input_ids)
        last_hidden_state = embedding_roberta['last_hidden_state']
        pooler_output = embedding_roberta['pooler_output']
        all_hidden_states = embedding_roberta['hidden_states']
        roberta_embed = all_hidden_states[0]
        combine_embed = self.attn_gate(roberta_embed, input_feature)

        outputs = self.roberta(input_ids=None, inputs_embeds=combine_embed, attention_mask=attention_mask)
        sequence_output  = outputs.last_hidden_state

        x = sequence_output[:, 0, :]
        x = self.dropout(x)
        x = torch.tanh(x)
        x = self.dropout(x)

        logits_bragging = self.classifier_bragging(x)


        # Initialize loss of bragging 
        loss_bragging = None 

        # Training on bragging
        if labels is not None:
          if self.num_labels_bragging == 1:
            loss_fct_bragging = nn.MSELoss()
            loss_bragging = loss_fct_bragging(logits_bragging.view(-1), labels.view(-1))
          else:
            loss_fct_bragging = nn.CrossEntropyLoss()
            loss_bragging = loss_fct_bragging(logits_bragging.view(-1, self.num_labels_bragging), labels.view(-1))


        output = (logits_bragging,) +outputs[2:]

      
        return ((loss_bragging,) + output) if loss_bragging is not None else output