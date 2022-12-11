import torch
import torch.nn as nn 


# Set the maximum sequence length
MAX_LEN = 50


hidden_size = 768
embedding_size = 400
beta = 0.001
dropout_prob = 0.5

class AttnGating(nn.Module):
  def __init__(self):
    super(AttnGating, self).__init__()
   
    self.linear = nn.Linear(93, embedding_size)
    self.relu = nn.ReLU(inplace=True)

    self.weight_emotion_W1 = nn.Parameter(torch.Tensor(hidden_size+embedding_size, hidden_size))
    self.weight_emotion_W2 = nn.Parameter(torch.Tensor(embedding_size, hidden_size))
 
    
    nn.init.uniform_(self.weight_emotion_W1, -0.1, 0.1)
    nn.init.uniform_(self.weight_emotion_W2, -0.1, 0.1)

    self.LayerNorm = nn.LayerNorm(hidden_size)
    self.dropout = nn.Dropout(dropout_prob)

  def forward(self, embeddings_roberta, linguistic_feature):
     
     # Project linguistic representations into vectors with comparable size
     linguistic_feature = self.linear(linguistic_feature)
     emotion_feature = linguistic_feature.repeat(MAX_LEN, 1, 1) # (50, bs, 200) 
     emotion_feature = emotion_feature.permute(1, 0, 2) # (bs, 50, 200)

     # Concatnate word and linguistic representations  
     features_combine = torch.cat((emotion_feature, embeddings_roberta), axis=2) # (bs, 50, 968)
     
     g_feature = self.relu(torch.matmul(features_combine, self.weight_emotion_W1))

     # Attention gating
     H = torch.mul(g_feature, torch.matmul(emotion_feature, self.weight_emotion_W2))
     alfa = min(beta * (torch.norm(embeddings_roberta)/torch.norm(H)), 1)
     E = torch.add(torch.mul(alfa, H), embeddings_roberta)

     # Layer normalization and dropout 
     embedding_output = self.dropout(self.LayerNorm(E)) 

     return E