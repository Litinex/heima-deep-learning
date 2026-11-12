"""
案例：
    演示张量和numpy之间如何相互转换，以及如何从标量张量中提取内容

涉及到的API:
    场景1：张量->numpy nd数组对象
        张量对象.numpy()        浅拷贝
        张量对象.numpy().copy() 深拷贝,链式编程
    场景2：numpy nd数组对象->张量
        from_numpy(ndarray) 浅拷贝
        torch.tensor(ndarray) 深拷贝
    场景3：从标量张量中提取其内容
        张量对象.item()

掌握：
    张量 -> numpy  张量对象.detach().numpy()
    numpy -> 张量  torch.tensor(ndarray)
    从标量张量中提取其内容  张量对象.item()
"""
import torch
import numpy as np
#1.定义函数,演示：张量 -> numpy
def dm01():
    #1.创建张量
    t1 = torch.tensor([1, 2, 3, 4, 5])
    print(f't1 :{t1},type:{type(t1)}')
    #2.张量 -> numpy
    #n1 = t1.numpy()                  #浅拷贝
    n1 = t1.detach().numpy().copy()   #深拷贝,链式编程
    print(f'n1 :{n1},type:{type(n1)}')

    #3.演示上述方式是否共享内存
    n1[0] = 100
    print(f'n1 :{n1},type:{type(n1)}')
    print(f't1 :{t1},type:{type(t1)}')
    pass

#2.定义函数,演示：numpy -> 张量
def dm02():
    #1.创建numpy
    n1 = np.array([11, 22, 33])
    print(f'n1 :{n1},type:{type(n1)}')
    #2.numpy -> 张量
    #t1 = torch.from_numpy(n1)        #浅拷贝
    t1 = torch.tensor(n1)            #深拷贝
    #t2 = t1.type(torch.float32)     #转换类型
    print(f't1 :{t1},type:{type(t1)}')
    #print(f't2 :{t2},type:{type(t2)}')
    #也可以链式编程转换类型
    #t3 = torch.tensor(n1).type(torch.float32)
    #3.演示上述方式是否共享内存
    t1[0] = 100
    print(f't1 :{t1},type:{type(t1)}')
    print(f'n1 :{n1},type:{type(n1)}')
    pass
#3.定义函数,演示：从标量张量中提取其内容
def dm03():
    #1.创建标量张量
    t1 = torch.tensor(100)
    print(f't1 :{t1},type:{type(t1)}')
    #2.从标量张量中提取其内容
    n1 = t1.item()
    print(f'n1 :{n1},type:{type(n1)}')
    pass

#4.测试
if __name__ == '__main__':
    dm01()
    dm02()
    dm03()