#-*- coding:utf-8 -*-

import argparse
import os
import random
import sys

def read_data(f_lbl0,f_lbl1):
    temp_lst = []

    with open(f_lbl0,'r',errors = 'ignore') as inf:
        for line in inf.readlines():
            line = str(line.strip())
            line = line + '\t' + '0'
            temp_lst.append(line)

    with open(f_lbl1,'r',errors = 'ignore') as inf:
        for line in inf.readlines():
            line = line.strip() + '\t' + '1'
            temp_lst.append(line)

    random.shuffle(temp_lst)
    return temp_lst

def write_data(f_lbl0,f_lbl1,odir,split):

    temp_lst = read_data(f_lbl0,f_lbl1)

    train_data = temp_lst[:split[0]]
    dev_data = temp_lst[split[0]:split[1]]
    test_data = temp_lst[split[1]:]
    head = 'sentence\tlabel'
    train_data.insert(0,head)
    dev_data.insert(0,head)
    test_data.insert(0,head)

    name = ['train.tsv','dev.tsv','test.tsv']
    val = ['train_data','dev_data','test_data']

    for i,n in enumerate(name):
        with open(odir+n,'w') as f:
            for line in eval(val[i]):
                line = line + '\n'
                f.write(str(line))


if __name__ == "__main__":

    random.seed(1)
    split = [8635,9595]
    file0 = '/home/juncsu/Code/Data/CapsData/mr-2005/originalData/rt-polarity.neg'
    file1 = '/home/juncsu/Code/Data/CapsData/mr-2005/originalData/rt-polarity.pos'
    odir = '/home/juncsu/Code/Data/CapsData/mr-2005/'

    write_data(file0,file1,odir,split)

    








