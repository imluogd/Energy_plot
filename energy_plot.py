#import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
input_list=[]
x_list = []
# 存储用于plt绘图的x坐标，实际上列表里元素为1,3,5....
y_list = []  # 能量数值,单位kcal/mol or hatree
level_count = 0  # 需要绘制的能量数目
color_list = []
try:
    while (True):  # 获取能级并计数，还需要获取颜色
        level_count += 1
        input_str = input(
            "please:\n\tEnter an energy;\n\tYou can also specify the color of the point\nblue( b ), cyan( c ), green( g ), black( k ), magenta( m ), red( r ), white( w ), yellow( y )\ne.g : 36.9 k or 36.9\n To exit, Press Ctrl+C :\n")
        if ' ' in input_str :
            input_list.append(level_count)
            #x_list = [2*i-1 for i in input_list]
            y_list.append(int(float(input_str.split(sep=' ')[0])))
            color_list.append(input_str.split(sep=' ')[1])
        else:
            input_list.append(level_count)
            y_list.append(int(float(input_str)))
            color_list.append('k')
        #while获取input_list,y_list,color_list 
        
except KeyboardInterrupt:
    x_list = [2*i-1 for i in input_list] 
    print("level-adding has finished")
    print(x_list, y_list, color_list)  #
    
fig = plt.figure()
ax = plt.axes()
step = 1 #横线长度
#print(input_list, x_list, y_list, color_list)#输出一下最终的各个列表
def get_ylim(min,max):#假定最小值是小于零的，应该不会有最大值还小于零的吧？
    return (min//10)*10, ((max//10)+1)*10
def draw_hline(xlist,ylist,colorlist):#颜色默认值
    if  xlist != [] and ylist !=[]:  
        #先画能级，再做连线
        
        ax.set_xlim(0,xlist[-1]+1)#需要根据输入，自动判断范围
        ax.set_ylim(get_ylim(min(ylist),max(ylist)))
        for i in range(len(xlist)):
            '''refer to markers : https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html'''
            line = Line2D([xlist[i]-0.5,xlist[i]+step-0.5],[ylist[i],ylist[i]],color=colorlist[i])
            ax.add_line(line)
    else : print("lists are empty! Please check your input.")        
def draw_link(xlist,ylist):#这一步是在两个点之间连线
     for i in range(len(xlist)):#第几条线？
        if i < len(xlist)-1:
            '''refer to https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html for linestyle'''
            link = Line2D([xlist[i]+0.5,xlist[i+1]-0.5],[ylist[i],ylist[i+1]],color='k',linestyle='--')
            ax.add_line(link)
        else : pass

draw_hline(x_list,y_list,color_list)
draw_link(x_list,y_list)#连线就不用变颜色了，一条线用一条颜色就可以    
plt.show()
    
    #plt.savefig()