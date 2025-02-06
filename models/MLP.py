import torch
from torch import nn

class MLP(nn.Module):
  def __init__(self, input_size, output_size, hidden_sizes=[], actv="ReLU()"):
    super().__init__()

    self.input_size = input_size
    self.output_size = output_size
    self.hidden_sizes = hidden_sizes
    self.mlp = nn.Sequential()
    self.is_rnn = False

    # Create net
    prev_size = self.input_size # Initialize the temporary input feature to each layer
    for i in range(len(hidden_sizes)): # Loop over layers and create each one
        
        # Add linear layer
        current_size = hidden_sizes[i] # Assign the current layer hidden unit from list
        layer = nn.Linear(prev_size, current_size)
        prev_size = current_size # Assign next layer input using current layer output
        self.mlp.add_module('Linear_%d'%i, layer) # Append layer to the model

        # Add activation function
        actv_layer = eval('nn.%s'%actv) # Assign activation function (eval allows us to instantiate object from string)
        self.mlp.add_module('Activation_%d'%i, actv_layer) # Append activation to the model with a name

    out_layer = nn.Linear(prev_size, self.output_size) # Create final layer
    self.mlp.add_module('Output_Linear', out_layer) # Append the final layer

  def forward(self, x):
    x = torch.tensor(x, dtype=torch.float)
    return self.mlp(x)