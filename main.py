'''
Function:
	客户端开始界面
'''
import sys
import cfg
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from modules.misc.Buttons import *
from modules.Casual_Create.Csl_Crt_Ui import *


'''游戏开始界面'''
class appStartUI(QWidget):#继承最简单窗体
	'''初始化'''
	def __init__(self, parent=None, **kwargs):
		super(appStartUI, self).__init__(parent)#多继承防止重复定义，调用父类构造方法

		#窗口大小
		self.setFixedSize(760, 650)#由于图片大小不可拉伸窗口
		self.setWindowTitle('MusicCreateApp')#左上角窗口文字
		self.setWindowIcon(QIcon(cfg.ICON_FILEPATH))#左上角标志图片

		# 背景图片
		palette = QPalette()#创建调色板实例
		palette.setBrush(self.backgroundRole(), QBrush(QPixmap(cfg.BACKGROUND_IMAGEPATHS.get('bg_start'))))
		self.setPalette(palette)

		# 按钮
		# 生成按钮
		self.Casual_C_button = PushButton(cfg.BUTTON_IMAGEPATHS.get('Casual'), self)
		self.Casual_C_button.move(250, 50)#按钮位置
		self.Casual_C_button.show()#Qlabel需要让我们看到
		self.Casual_C_button.click_signal.connect(self.Casual_Create)
		#退出按钮
		self.exit_button=PushButton(cfg.BUTTON_IMAGEPATHS.get('exit'),self)
		self.exit_button.move(250,500)
		self.exit_button.show()
		self.exit_button.click_signal.connect(self.exit_exit)

	'''随机生成'''
	def Casual_Create(self):
		self.close()
		self.running_ui = go_Casual_Create(cfg)
		self.running_ui.exit_signal.connect(lambda: sys.exit())
		self.running_ui.back_signal.connect(self.show)
		self.running_ui.show()

	'''退出'''
	def exit_exit(self):
		sys.exit()

'''run'''
if __name__ == '__main__':
	app = QApplication(sys.argv)
	handle = appStartUI()
	font = QFont()
	font.setPointSize(12)
	handle.setFont(font)
	handle.show()
	sys.exit(app.exec_())
