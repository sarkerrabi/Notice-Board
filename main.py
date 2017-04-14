import urllib
from Top10Notices import Top10Notices
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    t10n = Top10Notices()
    noticList = t10n.seu_top10_notices()
    uniname = "Southeast University (SEU)"
    listNo = list(range(1,len(noticList)))
    return render_template('index.html',notices =zip(noticList,listNo),uniname =uniname)



if __name__ == '__main__':
    app.run()


