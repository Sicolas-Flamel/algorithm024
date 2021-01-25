学习笔记



一开始的学习交作业：

# 1 初始化

在想要 交互 的文件夹下，右键 git-bash here（设置注册表在...\shell目录下 git-bash.exe 和 icon 的图标。）
然后输入
$ git init （后续如果删掉了还需要重新 init）

$ git config --global user.name "xxx"
$ git config --global user.email "xxx"
(查看一下：git config --global --list, 第二次重搞时发现，不用设置第二次。)

## 2 SSH连接--2步

### （1）生成 SSH，以便于后续的 SSH 链接，每次不用输密码了。

ssh-keygen -t rsa -C "email（XXX@xx.com）"
然后一路回车。

进入那个文件下：

cd /C/Users/.../.ssh（上一步的输出有）
$ ls   (查看当前目录下的文件）你会看到两个

$ cat id_ras.pub   # 看一眼公钥，复制所有，连带空格前面的 ssh-rsa 直到好几行的行尾：

![image-20210125175427827](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\image-20210125175427827.png)

### （2）复制粘贴到个人设置【点个人头像下的 Setting】里的 SSH，然后回到命令这边输入以下验证：
$ ssh -T git@github.com

# 3 git clone 

克隆，就是网页那边去点一个东西，就出现了形如 ： git clone git@github.com:Sicolo.../..xx.git
就ok啦。

越交流越有收获：
分享自己没有切好目录的错误启示，这时有大佬 phylony-lu 出现，解锁新的git管理工具：sourcetree。



# 安装 sourcetree 不好意思我又踩坑了：

![image-20210125180457784](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\image-20210125180457784.png)

我没有装 它自带的 git。。因为电脑里已经有 Git 了。

第二次装时发现，它是可以自动检测到已装了什么什么。所以第一次没检测到 Git，不然也会提醒的。

![image-20210125181450619](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\image-20210125181450619.png)