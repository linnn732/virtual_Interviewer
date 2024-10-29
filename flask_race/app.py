from flask import Flask, render_template, url_for,request,redirect
import requests
import time
from xml.etree import ElementTree
import os
import sys

app = Flask(__name__)  # __name__ 代表目前執行的模組
app = Flask(__name__, static_folder='') 

try:
    input = raw_input
except NameError:
    pass


class TextToSpeech(object):
    def __init__(self, subscription_key):
        self.subscription_key = subscription_key
        # self.tts =
        # self.timestr = sys.argv[2]
        self.access_token = None

    def get_token(self):
        fetch_token_url = "https://southcentralus.api.cognitive.microsoft.com/sts/v1.0/issuetoken"
        headers = {
        'Ocp-Apim-Subscription-Key': self.subscription_key
        }
        response = requests.post(fetch_token_url, headers=headers)
        self.access_token = str(response.text)

    def save_audio_boy(self,tts,timestr):
        base_url = 'https://southcentralus.tts.speech.microsoft.com/'
        path = 'cognitiveservices/v1'
        constructed_url = base_url + path
        headers = {
            'Authorization': 'Bearer ' + self.access_token,
            'Content-Type': 'application/ssml+xml',
            'X-Microsoft-OutputFormat': 'riff-24khz-16bit-mono-pcm',
            'User-Agent': 'AI-Voice'
            }

        xml_body = ElementTree.Element('speak', version='1.0')
        xml_body.set('{http://www.w3.org/XML/1998/namespace}lang', 'zh-TW')
        voice = ElementTree.SubElement(xml_body, 'voice')
        voice.set('{http://www.w3.org/XML/1998/namespace}lang', 'zh-TW')
        voice.set(
            'name', 'Microsoft Server Speech Text to Speech Voice (zh-TW, Zhiwei)')
        voice.text = tts
        body = ElementTree.tostring(xml_body)

        response = requests.post(constructed_url, headers=headers, data=body)

        save_path = './'
        if response.status_code == 200:
            with open(save_path+timestr + '.wav', 'wb') as audio:
                audio.write(response.content)
                print("\nStatus code: " + str(response.status_code) +
                    "\nYour TTS is ready for playback.\n")
        else:
            print("\nStatus code: " + str(response.status_code) +
              "\nSomething went wrong. Check your subscription key and headers.\n")


    def save_audio_girl(self,tts,timestr):
        base_url = 'https://southcentralus.tts.speech.microsoft.com/'
        path = 'cognitiveservices/v1'
        constructed_url = base_url + path
        headers = {
            'Authorization': 'Bearer ' + self.access_token,
            'Content-Type': 'application/ssml+xml',
            'X-Microsoft-OutputFormat': 'riff-24khz-16bit-mono-pcm',
            'User-Agent': 'AI-Voice'
            }
        xml_body = ElementTree.Element('speak', version='1.0')
        xml_body.set('{http://www.w3.org/XML/1998/namespace}lang', 'zh-TW')
        voice = ElementTree.SubElement(xml_body, 'voice')
        voice.set('{http://www.w3.org/XML/1998/namespace}lang', 'zh-TW')
        voice.set(
            'name', 'Microsoft Server Speech Text to Speech Voice (zh-TW, HsiaoYuNeural)')
        voice.text = tts
        body = ElementTree.tostring(xml_body)

        response = requests.post(constructed_url, headers=headers, data=body)

        save_path = './'
        if response.status_code == 200:
            with open(save_path+timestr + '.wav', 'wb') as audio:
                audio.write(response.content)
                print("\nStatus code: " + str(response.status_code) +
                    "\nYour TTS is ready for playback.\n")
        else:
            print("\nStatus code: " + str(response.status_code) +
              "\nSomething went wrong. Check your subscription key and headers.\n")


@app.route("/")  # 函數的裝飾(Decorator): 以函式為基礎，提供附加的功能
def hello():  # 函式
    username = "Welcome To Virtual Interviewer"
    titleimg = url_for('static', filename="header_back.jpg")
    img_f1 = url_for('static', filename="ting.jpg")
    img_f2 = url_for('static', filename="1lin.jpg")
    img_f3 = url_for('static', filename="kim.jpg")
    img_f4 = url_for('static', filename="peng.jpg")
    img_start = url_for('static', filename="start_button.png")
    img_user = url_for('static', filename="Interview.png")


    return render_template('idx.html',img_user=img_user, username=username, titleimg=titleimg, img_f1=img_f1, img_f2=img_f2, img_f3=img_f3, img_f4=img_f4, img_start=img_start)

@app.route('/record')
def record():
    return render_template('record.html')

@app.route("/voice", methods=["POST"])
def voice():
    if request.method == 'POST':
        
        if request.form["action"] == "gen_voice":
            tts = request.values['content']
            face = request.values['face']
            timestr = "voice"
            print(face)
            if face == 'kim.jpg' or face == 'peng.jpg':
                subscription_key = "f5c54db5c5f241e4bba6ef6e7d8bce23"
                app = TextToSpeech(subscription_key)
                app.get_token()
                app.save_audio_boy(tts,timestr)
                print('音檔已生成')

                return redirect(url_for('hello'))
            else:
                subscription_key = "f5c54db5c5f241e4bba6ef6e7d8bce23"
                app = TextToSpeech(subscription_key)
                app.get_token()
                app.save_audio_girl(tts,timestr)
                print('音檔已生成')

                return redirect(url_for('hello'))

        elif request.form["action"] == "gen_video":
            face = request.values['face']
            voice = request.values['voice']

            print(face)
            print(voice)
            os.system("python3 demo.py "+face+" "+voice+" video.mp4")

        return redirect(url_for('hello'))


if __name__=="__main__": #如果主程式執行
    app.debug = True
    app.run() #立刻啟動伺服器
