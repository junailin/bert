import sys
import os
import random

def multi_file2one(path,ofile,label = '0'):
    files = os.listdir(path)
    files_name = [path + item for item in files]

    with open(ofile,'w') as out_f:
        for item in files_name:
            with open(item,'r',errors = 'ignore') as in_f:
                lines = in_f.readlines()
                lines = [line.strip().replace('\n',' ') for line in lines]
                lines = ''.join(lines) + '\n'
                out_f.write(lines)

def read_data(names,lst,label):
    for item in names:
        with open(item,'r',errors='ignore') as f:
            lines = f.readlines()
            lines = [line.strip().replace('<br />',' ').replace('\n',' ').replace('  ',' ') for line in lines]
            lines = ''.join(lines)
            lines = lines.strip() + '\t' + str(label)
            lst.append(lines)


def imdb2tsv(indir,path):
    train_pos = os.listdir(indir+'train/pos/')
    train_neg = os.listdir(indir+'train/neg/')

    test_pos = os.listdir(indir+'test/pos/')
    test_neg = os.listdir(indir+'test/neg/')

    train_pos_name = [indir+'train/pos/' + item for item in train_pos]
    train_neg_name = [indir+'train/neg/' + item for item in train_neg]

    test_pos_name = [indir+'test/pos/' + item for item in test_pos]
    test_neg_name = [indir+'test/neg/' + item for item in test_neg]

    train = []
    test = []
    read_data(train_pos_name,train,label=1)
    read_data(train_neg_name,train,label=0)
    read_data(test_pos_name,test,label=1)
    read_data(test_neg_name,test,label=0)
    random.shuffle(train)
    random.shuffle(test)
    
    with open(path+'train.tsv','w') as f:
        for line in train:
            f.write(line + '\n')

    with open(path+'test.tsv','w') as f:
        for line in test:
            f.write(line + '\n')

if __name__ == '__main__':

    '''
    path = '/home/juncsu/Code/Data/CapsData/mr-2004/txt_sentoken/'
    multi_file2one(path+'neg/', path + 'neg.txt', '0')
    multi_file2one(path+'pos/', path + 'pos.txt', '1')
    '''
    indir = '/home/juncsu/Code/Data/aclImdb/'
    path = '/home/juncsu/Code/Data/CapsData/imdb/'
    imdb2tsv(indir,path)



