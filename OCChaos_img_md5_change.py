# -*- coding: utf-8 -*-

import hashlib
import os
import OCChaos_config
# 获取MD5
def GetFileMd5(filename):
    if not os.path.isfile(filename):
        return
    myhash = hashlib.md5()
    f = open(filename,'rb')
    while True:
        b = f.read(8096)
        if not b :
            break
        myhash.update(b)
    f.close()
    return myhash.hexdigest()
# 给文件添加末尾，改变md5
def fileAppend(filename):
    myfile = open(filename,'a')
    # 添加一个自定义内容，并不影响文件
    myfile.write("jneth")
    myfile.close

# 遍历文件，符合规则的进行重命名
# 项目路径   （找到自己的项目路径）
def start_change_img_md5():
    for (root, dirs, files) in os.walk(OCChaos_config.project_path):
        for file_name in files:
            if file_name.endswith(OCChaos_config.img_suf_set):
                short_name = os.path.splitext(file_name)[0]
                realpath = os.path.join(root, file_name)
                print(short_name + ' ==> ' + realpath)
                oldMd5 = GetFileMd5(realpath)
                fileAppend(realpath)
                newMd5 = GetFileMd5(realpath)
                print(oldMd5 + '-->' + newMd5)
