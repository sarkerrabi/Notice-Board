import urllib

from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)
def seu_top10_notices():
    url = 'http://www.seu.ac.bd/notice_board.php'
    source_code = urllib.request.urlopen(url)
    soup = BeautifulSoup(source_code.read(), 'html.parser')
    count = 1
    listNotices = []

    for link in soup.find_all('a', {'rel': 'facebox'}):
        listNotices.append(link.text+' ')

        # print(str(count) + ' ' + link.text)
        # print(url + link.get('href'))
        count += 1
        if count > 10:
            break
    return listNotices

@app.route('/')
def index():
    noticList = seu_top10_notices()
    uniname = "Southeast University (SEU)"
    listNo = list(range(1,len(noticList)))
    return render_template('index.html',notices =zip(noticList,listNo),uniname =uniname)



if __name__ == '__main__':
    app.run()


