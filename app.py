from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import os
import requests, json


app = Flask(__name__)

line_bot_api = LineBotApi(os.environ['CHANNEL_ACCESS_TOKEN'])
handler = WebhookHandler(os.environ['CHANNEL_SECRET'])


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


# @app.route("/api/test" , methods=['POST'])
# def testapi():
#   try:
#     msg = request.data   # 取得網址的 msg 參數
    
#     if msg != None:
#       msg_data = msg.decode("utf-8")
#       print(msg_data)
#       # 如果有 msg 參數，觸發 LINE Message API 的 push_message 方法
#       line_bot_api.push_message("Ua4c9e00a3662dddc35ee1d36665a8e27", TextSendMessage(text=msg_data))
#       return msg
#     else:
#       return 'OK'
#   except:
#     print('error')




# @handler.add(MessageEvent, message=TextMessage)
# def handle_message(event):
#     line_bot_api.push_message("Ua4c9e00a3662dddc35ee1d36665a8e27", TextSendMessage(text='Hello World!!!'))
#     message = TextSendMessage(text=event.message.text)
#     line_bot_api.reply_message(event.reply_token, message)
    
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)