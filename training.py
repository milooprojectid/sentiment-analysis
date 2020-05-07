import os
import numpy as np 
import pandas as pd 


# prepare data
def prepareData(dirpath):
    readData = pd.read_csv(dirpath,error_bad_lines=False)
    return(readData)


class Sentimet(object):
    def __init__(self,data,epoch,lr,opt):
        self.data = None
        self.epoch = 50
        self.lr = 0.001
        self.opt = None
          
