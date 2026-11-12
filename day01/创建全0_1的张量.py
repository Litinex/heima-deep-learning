"""
案例:
    演示如何创建全0，全1，指定值的张量

涉及到的函数如下：
torch.ones 和 torch.ones_like 创建全1张量
torch.zeros 和 torch.zeros_like 创建全0张量
torch.full 和 torch.full_like 创建指定值的张量

需要掌握的函数：
    zeros(),full()
"""
#导包
import torch


#场景1：torch.ones 和 torch.ones_like 创建全1张量
t1 = torch.ones(3, 4)  # 创建一个3行4列的全1张量
print(f't1 :{t1},type:{type(t1)}')
print('-'*30)

#t2:3行2列
t2 = torch.tensor([[1, 2], [3,4], [5, 6]])
print(f't2 :{t2},type:{type(t2)}')

#创建一个和t2形状相同的全1张量
t3 = torch.ones_like(t2)
print(f't3 :{t3},type:{type(t3)}')

#场景2：torch.zeros 和 torch.zeros_like 创建全0张量
t4 = torch.zeros(3, 4)  # 创建一个3行4列的全0张量
print(f't4 :{t4},type:{type(t4)}')
print('-'*30)

#场景3：torch.full 和 torch.full_like 创建指定值的张量
t5 = torch.full((3, 4), 5)  # 创建一个3行4列的张量，所有元素都是5
print(f't5 :{t5},type:{type(t5)}')
