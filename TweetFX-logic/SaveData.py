# -*- coding: utf-8 -*-
"""
@author: dvo
@class: Save Data
"""


class SaveData(object):
    '''
        Save Data class
        Saves labelled tweets to a csv file called dataset.csv
    '''
    def __init__(self):
        '''
            Class constructor or initialization method.
        '''

    def writeCsv(self, tweetsLabelled):
        try:
            with open("twitterData.txt","w") as f:
                for tweetLabelled in tweetsLabelled:
                    f.write(str(tweetLabelled['sentiment'])+","+str(tweetLabelled['text']))
        except IOError:
            print("writeCsv has an IOError")
            print(str(IOError))