import sys
import os

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


if __name__ == '__main__':

    path = '/home/juncsu/Code/Data/CapsData/mr-2004/txt_sentoken/'
    multi_file2one(path+'neg/', path + 'neg.txt', '0')
    multi_file2one(path+'pos/', path + 'pos.txt', '1')
    




