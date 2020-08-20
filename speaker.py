import aip
import vlc


def getaudio(text,filename) :
    APP_ID = '14891501'
    API_KEY = 'EIm2iXtvDSplvR5cyHU8dAeM'
    SECRET_KEY = '4KkGGzTq2GVrBEYPLXXWEEIoyLL1F6Zt'

    client = aip.AipSpeech(APP_ID, API_KEY, SECRET_KEY)

    """
       :param spd: 合成语音的讲话速度
       :param pit: 合成语言的讲话音调
       :param vol: 合成语言的音量
       :param per: 发音人选择, 0为普通女声，1为普通男生，3为情感合成-度逍遥，4为情感合成-度丫丫,5为情感合成-小琪琪，默认为情感合成-度逍遥
       :return:
    """

    result = client.synthesis(text, 'zh', 1, {'spd': 4, 'vol': 3, 'per': 4})

    if not isinstance(result, dict):
        with open(filename, 'wb') as f:
            f.write(result)


def playsound(words) :
    getaudio(words, './audio.mp3')
    player = vlc.MediaPlayer('./audio.mp3')
    player.play()


if __name__ == '__main__' :
    text = []
    index = -1
    while True :
        words = input('speake: ')
        if words == 'q' :
            exit()
        elif words == 'l' :
            with open('text.txt', 'r') as f :
                text = f.readlines()
                index = 0
        elif words == 'n' :
            if index != -1 :
                playsound(text[index])
                index += 1
            else :
                print('No text')
        else :
            playsound(words)
