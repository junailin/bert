import os

def change(inFile,outFile):
    with open(inFile,'r') as fin:
        with open(outFile,'w') as fout:
            for line in fin.readlines():
                label,sent = line.strip().split('\t')
                fout.write(sent + '\t' + label + '\n')
    print('Finshed!')

if __name__ == '__main__':
    base_dir = '/home/juncsu/Code/Data/GlueData/SST-2/'
    inFile = base_dir + 'test.tsv'
    outFile = base_dir + 'test.tsv.1'
    change(inFile,outFile)




