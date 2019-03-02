import os
import sys

def read_data(path, odir, split):
    label = set()
    with open(path, 'r', errors='ignore') as f:
        for line in f.readlines():
            line_lst = [item.strip() for item in line.split(':')]
            label.add(line_lst[0])
    label = {it:str(i) for i,it in enumerate(list(label))}
    label = {'ABBR': '4', 'HUM': '0', 'LOC': '2', 'NUM': '3', 'ENTY': '5', 'DESC': '1'}

    temp_lst = []
    with open(path, 'r', errors='ignore') as f:
        for line in f.readlines():
            line_lst = [item.strip() for item in line.split(':')]
            line = line_lst[1].strip() + '\t' + label[line_lst[0]]
            temp_lst.append(line)


    test_data = temp_lst[:split[0]]
    dev_data = temp_lst[split[0]:split[1]]
    train_data = temp_lst[split[1]:]
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

    split = [200,380]
    path = '/home/juncsu/Code/Data/CapsData/trec-qa/origin-data'
    odir = '/home/juncsu/Code/Data/CapsData/trec-qa/'
    read_data(path,odir,split)




