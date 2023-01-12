import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'LazyDeveloper'

os.system("git clone https://Noturritik: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@github.com/Noturritik/LazyPrincessV2  okk && cd okk && pip3 install -U -r requirements.txt && nohup python3 bot.py &")
