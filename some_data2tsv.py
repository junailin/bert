import os
import sys
import random

def read_write_1(infile,ofile):
    with open(ofile, 'w') as out_f:
        with open(infile,'r',errors='ignore') as in_f:
            lines = in_f.readlines()
            random.shuffle(lines)
            for line in lines:
                line_split = line.split(' ', 1)
                line = line_split[1].strip() + '\t' + line_split[0].strip()
                out_f.write(line + '\n')


def read_write_2(infile,ofile,split):
    temp_lst = []
    with open(infile,'r',errors='ignore') as in_f:
        lines = in_f.readlines()
        random.shuffle(lines)
        for line in lines:
            line_split = line.split(' ', 1)
            line = line_split[1].strip() + '\t' + line_split[0].strip()
            temp_lst.append(line)

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
        with open(ofile+n,'w') as f:
            for line in eval(val[i]):
                line = line + '\n'
                f.write(str(line))


if __name__ == "__main__":

    random.seed(1)
#### SST2
    indir = '/home/juncsu/Code/Data/sentiment_dataset/data/'
    odir = '/home/juncsu/Code/Data/CapsData/SST-2/'

    infiles = [indir + 'stsa.fine.train', indir + 'stsa.fine.dev', indir + 'stsa.fine.test']
    ofiles = [odir + 'train.tsv', odir + 'dev.tsv', odir + 'test.tsv']
    for i in range(3):
        read_write_1(infiles[i], ofiles[i])

#### SST1
    indir = '/home/juncsu/Code/Data/sentiment_dataset/data/'
    odir = '/home/juncsu/Code/Data/CapsData/SST-1/'

    infiles = [indir + 'stsa.binary.train', indir + 'stsa.binary.dev', indir + 'stsa.binary.test']
    ofiles = [odir + 'train.tsv', odir + 'dev.tsv', odir + 'test.tsv']
    for i in range(3):
        read_write_1(infiles[i], ofiles[i])

#### mpqa
    split = [8587,9542]
    indir = '/home/juncsu/Code/Data/sentiment_dataset/data/'
    odir = '/home/juncsu/Code/Data/CapsData/MPQA/'
    infile = indir + 'mpqa.all'
    read_write_2(infile, odir, split)

## subj
    split = [9000,9001]
    indir = '/home/juncsu/Code/Data/sentiment_dataset/data/'
    odir = '/home/juncsu/Code/Data/CapsData/SUBJ/'
    infile = indir + 'subj.all'
    read_write_2(infile, odir, split)

    
    











