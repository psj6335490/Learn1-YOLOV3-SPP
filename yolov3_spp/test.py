import torch

a=torch.tensor([1,2,8,6,4])

b= a[[2,2,3]]

print(a)
print(b)