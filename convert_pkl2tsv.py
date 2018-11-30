import pickle
import argparse
import os
import numpy as np

def convert(input_dir, output_dir,data_name):
    flist = ['devset.pkl', 'testset.pkl', 'trainset.pkl', 'label2id.pkl', 'vocab.pkl']
    wlist = ['dev.tsv', 'test.tsv', 'train.tsv']
    log_dir = '/home/juncsu/Code/Data/CapsData/summary_%s.txt' % (data_name)
    if os.path.exists(log_dir):
        os.remove(log_dir)

    print('Start convert ...!')
    with open(input_dir + flist[-1], 'rb') as f_vocab:
        vocab = pickle.load(f_vocab)
    vocab_rev = {ids:word for word, ids in vocab.items()}

    try:
        print(1,vocab_rev[1])
        print('-'*20 + ' there has 1 ' + '-'*20)
    except:
        print('+'*20 + ' there has not 1 ' + '+'*20)
        vocab_rev[1] = ','

    for i in range(3):
        with open(input_dir + flist[i], 'rb') as f:
            data = pickle.load(f)
        print(data[0])
        write_dir = output_dir + wlist[i]
        sLen = []
        with open(write_dir, 'w') as fw:
            fw.write('sentence' + '\t' + 'label' + '\n')
            for item in data:
                try:
                    word_lst = [vocab_rev[ids] for ids in item[1]]
                except:
                    word_lst = [vocab_rev[ids_in] for ids in item[1] for ids_in in ids]
                sLen.append(len(word_lst))
                word_str = ' '.join(word_lst)
                fw.write(word_str + '\t')
                fw.write(str(item[0]) + '\n')

        if i == 2:
            with open(log_dir,'a') as fa:
                sLen = np.array(sLen)
                p50, p25, p75 = int(np.mean(sLen)), int(np.percentile(sLen,25)), int(np.percentile(sLen,75))
                print(p50, p25, p75)
                fa.write("data_name\navgL: %d\n0.25L: %d\n0.75L: %d\n" % (p50, p25, p75)) 

        print(wlist[i] + ' is finshed!')
    

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--data_name', help='data name',type=str)
    parser.add_argument('--input_dir', help='input dir of which would be converted!', type=str, 
            default='/home/juncsu/Code/MyCapsule4TC/data/')
    parser.add_argument('--output_dir', help='output dir of which would be converted!', type=str,
            default='/home/juncsu/Code/Data/CapsData/')
    args = parser.parse_args()

    input_dir = args.input_dir + args.data_name + '/'
    output_dir = args.output_dir + args.data_name + '/'
    data_name = args.data_name

    try:
        os.makedirs(output_dir)
    except:
        pass

    convert(input_dir,output_dir,data_name)


