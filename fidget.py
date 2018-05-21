import torch
x = torch.tensor([5.5, 3])
x = x.new_ones(5, 3, dtype=torch.double)
x = torch.randn_like(x, dtype=torch.float)
y = torch.rand(5, 3)
# print(x + y)
# changing a torch tensor to numpy,
a = torch.ones(5)
print(a)
b = a.numpy()
print(b)
a.add_(1)
print(a)
print(b)
