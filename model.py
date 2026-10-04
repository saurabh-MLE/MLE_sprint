
import torch
import torch.nn as nn

class SimpleMLEModel(nn.Module):
    def __init__(self):
        super(SimpleMLEModel, self).__init__()
        self.linear = nn.Linear(in_features=2, out_features=1)

    def forward(self, x):
        return self.linear(x)

if __name__ == "__main__":
    model = SimpleMLEModel()
    torch.save(model.state_dict(), "model_weights.pth")
    print("PyTorch model successfully serialized and saved as model_weights.pth")
