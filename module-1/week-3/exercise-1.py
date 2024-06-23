import torch.nn as nn
import torch


class softmax(nn.Module):
    def __init__(self):
        super().__init__()

    def softmax(self, x):
        return torch.exp(x) / torch.sum(torch.exp(x), dim=0)

    def forward(self, x):
        out = self.softmax(x)
        return out


class stable_softmax(nn.Module):
    def __init__(self):
        super().__init__()

    def stable_softmax(self, x):
        return torch.exp(x - torch.max(x))/torch.sum(torch.exp(x - torch.max(x)), dim=0)

    def forward(self, x):
        out = self.stable_softmax(x)
        return out


if __name__ == "__main__":
    x = torch.tensor([1, 2, 3])
    model = softmax()
    print(model(x))
