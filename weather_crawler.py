import schedule
import time
import pandas as pd
from time import gmtime, strftime

from git import Repo

def report():
    df = pd.read_html('http://weathernews.jp/onebox/35.71/139.73/temp=c&q=%E6%9D%B1%E4%BA%AC%E9%83%BD%E6%96%87%E4%BA%AC%E5%8C%BA&v=b2b28d9493819bf1c217652bab096ba7080ad18b7e5f01c90b57371ae4b06857')
    weather = df[4]
    weather.columns = [u'時刻', u'氣溫（℃）', u'風速（m/s）', u'風向',
                   u'降水量（mm/h）', u'日照（分）']
    fname = strftime("daily/%d-%b-%Y.csv", gmtime())
    weather.to_csv(fname)

    repo = Repo('.')
    origin = repo.remote('origin')
    file_list = [fname]
    commit_message = 'Add file: %s' % fname
    repo.index.add(file_list)
    repo.index.commit(commit_message)
    origin.push()


schedule.every().day.at("16:59").do(report)

while True:
    schedule.run_pending()
    time.sleep(1)
