'''
案例：
    演示张量的形状操作

涉及到的API:
    reshape(): #在不改变张量的内容前提下，对其形状做改变，即无论形状怎么改变，拼出来的内容顺序不会变
    unsqueeze(): #在张量的指定位置插入1个1维度
    squeeze(): #删除张量中所有维度为1的维度
    transpose(): #转置张量,一次只能转置2个维度
    permute(): #重新排列张量的维度，一次可以排列多个维度
    view(): #改变张量的形状，但要求张量是连续的
    contiguous(): #返回一个连续的张量，如果张量已经连续则返回原张量
    is_contiguous():#判断张量是否连续
'''

#导包
import torch

#指定随机种子，确保随机结果可重复
torch.manual_seed(24)

#1.定义函数，演示reshape()函数.

def dm01():
    #1.定义2行3列的张量
    t1 = torch.randint(1,10,size=(2,3))
    print(f't1 :{t1},shape:{t1.shape},row:{t1.shape[0]},columns:{t1.shape[1]},{t1.shape[-1]}')

    #2.通过reshape()函数，把t1转换成3行2列，1行6列，6行1列
    #t2 = t1.reshape(3,2)
    t2 = t1.reshape(1,6)
    t2 = t1.reshape(6,1)

    #3.尝试通过reshape()函数，把t1转换成2行5列
    #t3 = t1.reshape(2,5) #报错，元素不一致
    #print(f't3:{t3}')
#2.定义函数，演示unsqueeze(), squeeze()函数.
def dm02():
    #1.定义2行3列的张量
    t1 = torch.randint(1,10,size=(2,3))
    print(f't1:{t1}')

    #2.在0维，插入1个1维度
    t2 = t1.unsqueeze(0)
    print(f't2:{t2},shape:{t2.shape}')

    #3.在1维，插入1个1维度
    t3 = t1.unsqueeze(1)
    print(f't3:{t3},shape:{t3.shape}')

    #4.在2维，插入1个1维度
    t4 = t1.unsqueeze(2)
    print(f't4:{t4},shape:{t4.shape}')

    #5.在3维(不存在)，插入1个1维度，报错，越界
    #t5 = t1.unsqueeze(3)
    #print(f't5:{t5},shape:{t5.shape}')

    #6.删除张量中所有维度为1的维度
    t6 = t2.squeeze()
    print(f't6:{t6},shape:{t6.shape}')
#3.定义函数，演示transpose(), permute()函数.
def dm03():
    #1.定义张量
    t1 = torch.randint(1,10,size = (2,3,4))

    #2.改变维度从(2,3,4) -> (3,2,4)
    t2 = t1.transpose(0,1)
    print(f't2:{t2},shape:{t2.shape}')

    #3.改变维度从(2,3,4) -> (4,2,3)
    t3 = t1.permute(2,0,1)
    print(f't3:{t3},shape:{t3.shape}')
#4.定义函数，演示view()函数, contiguous(), is_contiguous()函数.
def dm04():
    #1.定义张量
    t1 = torch.randint(1,10,size=(2,3))

    #2.判断张量是否连续
    print(f't1:{t1},is_contiguous:{t1.is_contiguous()}') #True

    #3.通过view()函数，改变张量的形状
    t2 = t1.view(3,2)
    print(f't2:{t2},shape:{t2.shape}')
    print(f't2:{t2},shape:{t2.shape},is_contiguous:{t2.is_contiguous()}') #True

    #4. 通过transpose函数交换维度 -> 交换之后就会不连续
    t3 = t1.transpose(0,1)
    print(f't3:{t3},shape:{t3.shape},is_contiguous:{t3.is_contiguous()}') #False

    #5. 尝试把t3张量转换成(3,2)的形状,通过view()函数
    #t4 = t3.view(2,3) #报错，因为t3是不连续的
    #print(f't4:{t4},shape:{t4.shape},is_contiguous:{t4.is_contiguous()}') #False

    #6. 可以通过contiguous()函数，把t3张量转换成连续的
    t5 = t3.contiguous()
    print(f't5:{t5},shape:{t5.shape},is_contiguous:{t5.is_contiguous()}') #True
    t6 = t5.view(3,2)
    print(f't6:{t6},shape:{t6.shape},is_contiguous:{t6.is_contiguous()}') #True

#5.测试
if __name__ == '__main__':
   # dm01()
   # dm02()
   # dm03()
   dm04()
