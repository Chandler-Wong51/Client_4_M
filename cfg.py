'''config file'''
import os


# 图标路径
ICON_FILEPATH = os.path.join(os.getcwd(), 'resources/images/icon/icon.ico')
# 背景图片路径
BACKGROUND_IMAGEPATHS = {
                            'bg_game': os.path.join(os.getcwd(), 'resources/images/bg/bg_game.png'),
                            'bg_start': os.path.join(os.getcwd(), 'resources/images/bg/bg_start.png')
                        }
# 按钮图片路径
BUTTON_IMAGEPATHS = {
                        'Imitate': [os.path.join(os.getcwd(), 'resources/images/buttons/Imitate_0.png'),
                                   os.path.join(os.getcwd(), 'resources/images/buttons/Imitate_1.png'),
                                   os.path.join(os.getcwd(), 'resources/images/buttons/Imitate_2.png')],
                        'Casual': [os.path.join(os.getcwd(), 'resources/images/buttons/Casual_0.png'),
                               os.path.join(os.getcwd(), 'resources/images/buttons/Casual_1.png'),
                               os.path.join(os.getcwd(), 'resources/images/buttons/Casual_2.png')],
                        'tip': [os.path.join(os.getcwd(), 'resources/images/buttons/tip_0.png'),
                               os.path.join(os.getcwd(), 'resources/images/buttons/tip_1.png'),
                               os.path.join(os.getcwd(), 'resources/images/buttons/tip_2.png')],
                        'turn1': [os.path.join(os.getcwd(), 'resources/images/buttons/turn1_0.png'),
                               os.path.join(os.getcwd(), 'resources/images/buttons/turn1_1.png'),
                               os.path.join(os.getcwd(), 'resources/images/buttons/turn1_2.png')],
                        'turn2': [os.path.join(os.getcwd(), 'resources/images/buttons/turn2_0.png'),
                                  os.path.join(os.getcwd(), 'resources/images/buttons/turn2_1.png'),
                                  os.path.join(os.getcwd(), 'resources/images/buttons/turn2_2.png')],
                        'others': [os.path.join(os.getcwd(), 'resources/images/buttons/others_0.png'),
                               os.path.join(os.getcwd(), 'resources/images/buttons/others_1.png'),
                               os.path.join(os.getcwd(), 'resources/images/buttons/others_2.png')],
                        'exit': [os.path.join(os.getcwd(), 'resources/images/buttons/exit_0.png'),
                               os.path.join(os.getcwd(), 'resources/images/buttons/exit_1.png'),
                               os.path.join(os.getcwd(), 'resources/images/buttons/exit_2.png')],
                        'home': [os.path.join(os.getcwd(), 'resources/images/buttons/home_0.png'),
                                 os.path.join(os.getcwd(), 'resources/images/buttons/home_1.png'),
                                 os.path.join(os.getcwd(), 'resources/images/buttons/home_2.png')],
                        'givein': [os.path.join(os.getcwd(), 'resources/images/buttons/givein_0.png'),
                                   os.path.join(os.getcwd(), 'resources/images/buttons/givein_1.png'),
                                   os.path.join(os.getcwd(), 'resources/images/buttons/givein_2.png')],
                        'regret': [os.path.join(os.getcwd(), 'resources/images/buttons/regret_0.png'),
                                   os.path.join(os.getcwd(), 'resources/images/buttons/regret_1.png'),
                                   os.path.join(os.getcwd(), 'resources/images/buttons/regret_2.png')],
                        'startgame': [os.path.join(os.getcwd(), 'resources/images/buttons/startgame_0.png'),
                                      os.path.join(os.getcwd(), 'resources/images/buttons/startgame_1.png'),
                                      os.path.join(os.getcwd(), 'resources/images/buttons/startgame_2.png')],
                        'urge': [os.path.join(os.getcwd(), 'resources/images/buttons/urge_0.png'),
                                 os.path.join(os.getcwd(), 'resources/images/buttons/urge_1.png'),
                                 os.path.join(os.getcwd(), 'resources/images/buttons/urge_2.png')]
                    }
# 显示胜利图片路径
WIN_IMAGEPATHS = {
                    'black': os.path.join(os.getcwd(), 'resources/images/win/black_win.png'),
                    'white': os.path.join(os.getcwd(), 'resources/images/win/white_win.png'),
                    'draw': os.path.join(os.getcwd(), 'resources/images/win/draw.png')
                }
# 棋子图片路径
CHESSMAN_IMAGEPATHS = {
                        'black': os.path.join(os.getcwd(), 'resources/images/chessman/black.png'),
                        'white': os.path.join(os.getcwd(), 'resources/images/chessman/white.png'),
                        'sign': os.path.join(os.getcwd(), 'resources/images/chessman/sign.png'),
                        'blank':os.path.join(os.getcwd(), 'resources/images/chessman/blank.png')
                    }
# 音效
SOUNDS_PATHS = {
                    'drop': os.path.join(os.getcwd(), 'resources/audios/drop.wav'),
                    'urge': os.path.join(os.getcwd(), 'resources/audios/urge.wav')
                }
# 端口号(联机对战时使用)
PORT = 3333
