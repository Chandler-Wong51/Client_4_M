# -*- coding:utf-8 -*-
import time
import os
from pykeyboard import PyKeyboard

def printSheet(name_list):
    # 打开页面
    cmd = r"MidiSheetMusic-2.1.exe"  #exe文件的绝对路径
    a = os.startfile(cmd)
    time.sleep(0.2)
    # 打开MIDI文件
    k=PyKeyboard()
    k.press_key(k.control_key)
    k.tap_key('o')
    k.release_key(k.control_key)
    time.sleep(0.5)
    str=name_list
    k.press_keys(str)
    time.sleep(0.2)
    k.tap_key(k.enter_key)
    # 保存图片
    k.press_key(k.control_key)
    k.tap_key('s')
    k.release_key(k.control_key)
    time.sleep(0.6)
    k.tap_key(k.enter_key)
    # 关闭窗口
    k.press_key(k.alt_key)
    k.tap_key(k.function_keys[4])
    k.release_key(k.alt_key)

# if __name__=="__main__":
#     printSheet("new1.mid")