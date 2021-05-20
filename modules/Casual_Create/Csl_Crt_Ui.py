'''
Function:
    定义人机对战
'''
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtMultimedia import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import shutil
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.animation import FuncAnimation

from scipy.signal import detrend
from pydub import AudioSegment

import matplotlib.pyplot as plt
import numpy as np
import struct
import wave
import os
import sys
import pygame
import socket
import json
import time
import random
import threading
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from modules.misc.Buttons import *
from modules.misc.utils import *
from modules.misc.MIDIexe import *



'''随机生成'''


class go_Casual_Create(QWidget):
    back_signal = pyqtSignal()
    exit_signal = pyqtSignal()
    receive_signal = pyqtSignal(dict, name='data')
    send_back_signal = False

    def __init__(self, cfg, parent=None, **kwargs):
        super(go_Casual_Create, self).__init__(parent)
        # 常量初始化
        self.cfg = cfg
        self.motion = 0
        self.instrument = 0
        self.motion_str_lis = ['随意', '喜悦', '愤怒', '平静', '忧伤']
        self.instrument_str_lis = ['随意', '二胡', '唢呐']
        # 窗口初始化
        self.fonth = QFont('Microsoft YaHei', 13, 75)
        self.setFixedSize(760, 650)
        self.setWindowTitle('Casual_Create')
        self.setWindowIcon(QIcon(cfg.ICON_FILEPATH))
        # 背景图片
        palette = QPalette()
        palette.setBrush(self.backgroundRole(), QBrush(QPixmap(cfg.BACKGROUND_IMAGEPATHS.get('bg_game'))))
        #self.setPalette(palette)
        # 按钮
        # 主页按钮
        self.home_button = PushButton(cfg.BUTTON_IMAGEPATHS.get('home'), self)
        self.home_button.click_signal.connect(self.goHome)
        self.home_button.move(680, 10)
        # 情绪单选按钮
        self.btn1 = QRadioButton("喜悦", self)
        self.btn1.setChecked(False)
        self.btn1.move(50, 10)
        self.btn2 = QRadioButton("愤怒", self)
        self.btn2.setChecked(False)
        self.btn2.move(50, 40)
        self.btn3 = QRadioButton("平静", self)
        self.btn3.setChecked(False)
        self.btn3.move(50, 70)
        self.btn4 = QRadioButton("忧伤", self)
        self.btn4.setChecked(False)
        self.btn4.move(50, 100)
        # 情绪按钮组
        self.btgrp_motion = QButtonGroup(self)
        self.btgrp_motion.addButton(self.btn1, 1)
        self.btgrp_motion.addButton(self.btn2, 2)
        self.btgrp_motion.addButton(self.btn3, 3)
        self.btgrp_motion.addButton(self.btn4, 4)
        self.btgrp_motion.buttonClicked.connect(self.rbclicked)
        # 乐器单选按钮
        self.btn10 = QRadioButton("二胡", self)
        self.btn10.setChecked(False)
        self.btn10.move(200, 10)
        self.btn20 = QRadioButton("唢呐", self)
        self.btn20.setChecked(False)
        self.btn20.move(200, 40)
        # 乐器按钮组
        self.btgrp_instruction = QButtonGroup(self)
        self.btgrp_instruction.addButton(self.btn10, 10)
        self.btgrp_instruction.addButton(self.btn20, 20)
        self.btgrp_instruction.buttonClicked.connect(self.rbclicked)
        # 提交
        self.btn_submit = QPushButton('提交', self)
        self.btn_submit.move(300, 10)
        self.btn_submit.clicked.connect(self.submit_conditions)
        #网络
        # 接收数据信号绑定到responseForReceiveData函数
        self.receive_signal.connect(self.responseForReceiveData)
        # TCP/IP客户端
        self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#socket.AF_INET, socket.SOCK_STREAM
        try:
            self.tcp_socket.connect(('47.118.60.38', 8899))
            #data = {'type': 'action', 'detail': 'regret'}
            #self.tcp_socket.sendall(self.packSocketData(data))

        except Exception as err:
            # 正式运行前注释掉打印异常
            print(err)

        threading.Thread(target=self.receiveServerData).start()
        #音乐按钮
        #播放
        self.btn_start = QPushButton('播放', self)
        self.btn_start.move(10, 500)
        self.btn_start.clicked.connect(self.play_and_off)
        #上一首
        self.btn_for = QPushButton('上一首', self)
        self.btn_for.move(110, 500)
        self.btn_for.clicked.connect(self.music_for)
        #下一首
        self.btn_back = QPushButton('下一首', self)
        self.btn_back.move(210, 500)
        self.btn_back.clicked.connect(self.music_back)
        #打谱
        # 下一首
        self.btn_print = QPushButton('打谱', self)
        self.btn_print.move(310, 500)
        self.btn_print.clicked.connect(self.music_print)
        #显示总数
        self.music_sum_label = QLabel(self)
        self.music_sum_label.move(50,200)
        self.music_sum_label.setText('0')
        self.music_sum_label.repaint()
        self.playdex = 0
        # 显示当前
        self.music_ndex_label = QLabel(self)
        self.music_ndex_label.move(200, 200)
        self.music_ndex_label.setText('1')
        self.music_ndex_label.repaint()

        #音乐播放器
        self.playlist = QMediaPlaylist(self)  # 1
        self.player = QMediaPlayer(self)
        self.player.setPlaylist(self.playlist)
        self.playlist.setCurrentIndex(0)
        self.playlist.setPlaybackMode(self.playlist.Sequential)
        self.player.setVolume(100)  # 5
        self.player.status = 0

    # 选择
    def rbclicked(self):
        sender = self.sender()
        if sender == self.btgrp_motion:
            if self.btgrp_motion.checkedId() == 1:
                self.motion = 1
            elif self.btgrp_motion.checkedId() == 2:
                self.motion = 2
            elif self.btgrp_motion.checkedId() == 3:
                self.motion = 3
            else:
                self.motion = 4
        else:
            if self.btgrp_instruction.checkedId() == 10:
                self.instrument = 1
            else:
                self.instrument = 2

    def submit_conditions(self, btn_submit):
        print('motion' + self.motion_str_lis[self.motion] + 'instrument' + self.instrument_str_lis[self.instrument])
        self.tcp_socket.sendall(self.packSocketData({'motion':self.motion,'instrument':self.instrument}))
        self.playlist.clear()
        self.playdex = 0
        self.music_sum_label.setText('0')
        self.music_sum_label.repaint()
        self.music_ndex_label.setText('1')
        self.music_ndex_label.repaint()
    '''关闭窗口事件'''

    def closeEvent(self, event):
        if not self.send_back_signal:
            self.exit_signal.emit()

    '''返回游戏主页面'''

    def goHome(self):
        self.send_back_signal = True
        self.close()
        self.back_signal.emit()

    def packSocketData(self, data):
        return (json.dumps(data) + ' END').encode()
    
    def play_and_off(self):
        if self.player.status:
            self.player.pause()
            self.btn_start.setText('播放')
            self.player.status = 0
        else:
            self.player.play()
            self.btn_start.setText('暂停')
            self.player.status = 1
    def music_for(self):
        if self.player.status:
            self.player.stop()
            self.player.status = 0
            self.btn_start.setText('播放')
        self.player.playlist().previous()
        print('总数'+str(self.player.playlist().mediaCount()))
        print('现在' + str(self.player.playlist().currentIndex()))
        self.music_ndex_label.setText(str(self.player.playlist().currentIndex()))
        self.music_ndex_label.repaint()

    def music_back(self):
        if self.player.status:
            self.player.stop()
            self.player.status = 0
            self.btn_start.setText('播放')
        self.player.playlist().next()
        print('总数' + str(self.player.playlist().mediaCount()))
        print('现在' + str(self.player.playlist().currentIndex()))
        self.music_ndex_label.setText(str(self.player.playlist().currentIndex()))
        self.music_ndex_label.repaint()
    def music_print(self):
        printSheet(r'mm/'+str(self.player.playlist().currentIndex()+'.mid'))
        return 0
    def receiveServerData(self):
        while 1:
            buffsize = 1024
            head_struct = self.tcp_socket.recv(4)  # 接收报头的长度,
            if head_struct:
                print('已连接服务端,等待接收数据')
            head_len = struct.unpack('i', head_struct)[0]  # 解析出报头的字符串大小
            data = self.tcp_socket.recv(head_len)  # 接收长度为head_len的报头内容的信息 (包含文件大小,文件名的内容)

            head_dir = json.loads(data.decode('utf-8'))
            filesize_b = head_dir['filesize_bytes']
            filename = head_dir['filename']

            #   接受真的文件内容
            recv_len = 0
            recv_mesg = b''
            old = time.time()
            f = open('mm/'+filename, 'wb')
            while recv_len < filesize_b:
                percent = recv_len / filesize_b

                process_bar(percent)
                if filesize_b - recv_len > buffsize:

                    recv_mesg = self.tcp_socket.recv(buffsize)
                    f.write(recv_mesg)
                    recv_len += len(recv_mesg)
                else:
                    recv_mesg = self.tcp_socket.recv(filesize_b - recv_len)
                    recv_len += len(recv_mesg)
                    f.write(recv_mesg)

            print(recv_len, filesize_b)
            now = time.time()
            stamp = int(now - old)
            print('总共用时%ds' % stamp)
            f.close()
            self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile('mm/'+filename)))
            self.playdex += 1
            self.music_sum_label.setText(str(self.playdex))
            self.music_sum_label.repaint()
        return 0
    def responseForReceiveData(self):
        return 0
