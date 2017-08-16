import os
import filetype
import shutil
import time

counter=1
folder = 'F:\\img'  # 文件夹路径
newder= 'F:\\20170814001\\'#新路劲
beiyong= os.path.join(newder,"beiyong\\")#重复备用路径
os.mkdir(beiyong)
#判断文件是否重复
def ppppp(newder,file):
    return os.path.os.path.exists(os.path.join(newder+file))
#获取到文件下的所有文件了
for root, dis, files in os.walk(folder):  # os.walk() 返回的是当前的路径，当前文件夹下的文件：
    for file in files:
        if file.endswith('.gif') or file.endswith('.jpg') or file.endswith('.JPG') or file.endswith('.png') or file.endswith('.tif') or file.endswith('.tiff') or file.endswith('.psd') or file.endswith('.swf'):
            #判断新路径下时候存在这个文件
            bn= ppppp(newder,file)
            if bn:
                #存在加随机数
                # sjs=timeYS()
                #改一下文件的名字
                spiltfile=file[:-4]
                newfile= spiltfile +'_'+str(counter-1)+ '.jpg'
                #保存到文件下面
                shutil.copy(os.path.join(root, file), beiyong)
                #修改文件名字
                os.rename(os.path.join(beiyong, file), os.path.join(beiyong, newfile))
                #移动文件
                shutil.move(os.path.join(beiyong,newfile),newder)
                print("已经成功混入图片区")
                counter += 1
                print("----删除备用路径----")
            else:
                print("不存在，继续执行")
                shutil.copy(os.path.join(root,file),newder)
                counter += 1
            print("这是一张图片，正在处理第"+str(counter-1)+"张" )
        else:
            print('这不是一张图片 ,不进行处理-----------------正在检查下一个');

print("----删除备用路径----")
os.rmdir(beiyong)
print("总共执行了"+str(counter-1)+"张的迁移")
print("----运行完毕----")