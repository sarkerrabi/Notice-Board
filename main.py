import urllib
from Top10Notices import Top10Notices
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    t10n = Top10Notices()
    noticList = t10n.nsu_top10_notice()
    uniname =  t10n.uniList()
    listNo = list(range(1,len(noticList[0])))
    return render_template('index.html',notices =zip(noticList[0],listNo,noticList[1]),uniname =uniname)

@app.route('/nlist')
def nlist():
    top10 = Top10Notices()
    unilist = top10.uniList()

    # lengths = top10.selected_unis_length()
    # # unis = top10.selected_unis()
    # # uni_zip = zip(lengths,unis)
    nsu_zip = zip(list(range(1,len(top10.nsu_top10_notice()[0]))),top10.nsu_top10_notice()[0],top10.nsu_top10_notice()[1])
    aiub_zip = zip(list(range(1,len(top10.aiub_top10_notice()[0]))),top10.aiub_top10_notice()[0],top10.aiub_top10_notice()[1])
    bracu_zip = zip(list(range(1,len(top10.bracu_top10_notice()[0]))),top10.bracu_top10_notice()[0],top10.bracu_top10_notice()[1])
    ewu_zip = zip(list(range(1,len(top10.ewu_top10_notice()[0]))),top10.ewu_top10_notice()[0],top10.ewu_top10_notice()[1])
    iub_zip = zip(list(range(1,len(top10.iub_top10_notice()[0]))),top10.iub_top10_notice()[0],top10.iub_top10_notice()[1])
    iubat_zip = zip(list(range(1,len(top10.iubat_top10_notice()[0]))),top10.iubat_top10_notice()[0],top10.iubat_top10_notice()[1])
    uiu_zip = zip(list(range(1,len(top10.uiu_top10_notice()[0]))),top10.uiu_top10_notice()[0],top10.uiu_top10_notice()[1])
    seu_zip = zip(list(range(1,len(top10.seu_top10_notice()[0]))),top10.seu_top10_notice()[0],top10.seu_top10_notice()[1])




    return render_template('nlist.html',bracu_zip=bracu_zip,unilist=unilist,nsu_zip=nsu_zip,aiub_zip = aiub_zip,ewu_zip=ewu_zip,iub_zip=iub_zip,iubat_zip=iubat_zip,uiu_zip=uiu_zip,seu_zip=seu_zip)




if __name__ == '__main__':
    app.run()


