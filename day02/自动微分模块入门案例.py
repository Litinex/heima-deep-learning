"""
案例：
    演示自动微分模块具体如何求导

回顾：
    权重更新公式：W新 = W旧 - 学习率 * 梯度

    梯度 = 损失对权重的导数

    关于损失函数的导数，无需手动计算，自动微分模块会自动计算

注意：只有标量张量才能求导，且大多数底层操作的都是浮点型，记得转型
"""

#导包
import torch

#1.定义变量，记录：初始的权重w(旧)
#参1：初始值 参2：是否自动微分(求导) 参3：数据类型
w = torch.tensor(10,requires_grad=True, dtype=torch.float)

#2.定义loss变量，表示损失函数
loss = 2 * w ** 2

#3.打印梯度函数类型
print(loss.grad_fn)
print(loss.sum())
#4.计算梯度，计算完毕后，会记录到grad属性中
#loss.backward()
loss.sum().backward()     #保证loss是标量张量
#5.带入权重更新公式
w.data = w.data - 0.01 * w.grad

#6.打印结果
print(f'更新后的权重：{w}')



