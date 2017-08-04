import time
import pandas as pd
from time import gmtime, strftime

from git import Repo

def report():
    cities = ['taipei', 'taichung', 'tainan', 'taitung', 'hualien', 'pingtung', 'yilan']
    urls = [
        'http://www.cwb.gov.tw/V7/observe/24real/Data/46692.htm',
        'http://www.cwb.gov.tw/V7/observe/24real/Data/46749.htm',
        'http://www.cwb.gov.tw/V7/observe/24real/Data/46741.htm',
        'http://www.cwb.gov.tw/V7/observe/24real/Data/46766.htm',
        'http://www.cwb.gov.tw/V7/observe/24real/Data/46699.htm',
        'http://www.cwb.gov.tw/V7/observe/24real/Data/C0R17.htm',
        'http://www.cwb.gov.tw/V7/observe/24real/Data/46708.htm',
    ]
    for city, url in zip(cities, urls): 

        df = pd.read_html(url, header=0)
        df = df[0]
        del df['溫度(°F>>°C)']

        fname = city + strftime("/%d-%b-%Y.csv", gmtime())
        df.to_csv(fname)

        repo = Repo('.')
        origin = repo.remote('origin')
        file_list = [fname]
        commit_message = 'Add file: %s' % fname
        repo.index.add(file_list)
        repo.index.commit(commit_message)
        origin.push()
  
report()



