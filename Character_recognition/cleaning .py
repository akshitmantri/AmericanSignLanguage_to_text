import os
import csv
import pandas as pd
header=[]
listans=[]
def val(fname):
	s=''
	# leng = len(fname)
	return str(fname[0])

def list_files(dir):                                                                                                  
    r = []                                                                                                            
    subdirs = [x[0] for x in os.walk(dir)]                                                                            
    for subdir in subdirs:                                                                                            
        files = os.walk(subdir).next()[2]                                                                             
        if (len(files) > 0):                                                                                          
            for file in files:                                                                                        
                r.append(subdir + "/" + file)
                fpath = subdir + "/" + file
                fname = val(file)
                # print fpath
                with open(fpath,'rb') as f:
					reader = csv.reader(f)
					mylist = list(reader)
					# print mylist[0]
					i=-1
					for line in mylist:
						i=i+1
						if(len(line)!=0):
							if(line[0]!='' and line[0][0]!='G' and line[0][0]!='d'):
								tmp = []
								tmp = line
								tmp.append(str(fname))
								listans.append(tmp)     
    return r  

list_files('alphabets')
# print listans
out = open('traindata.csv','wb')
wr = csv.writer(out, quoting=csv.QUOTE_ALL)
# wr.writerow(listans)
df = pd.DataFrame(listans)
df.to_csv('traindata.csv', index=False)
# for lis in listans:
# 	i=0
# 	for elem in lis:
# 		i=i+1
# 		if(elem!=''):
# 			if(i==31):
# 				out.write(float(elem))
# 				out.write("\n")
# 			else:
# 				out.write(float(elem))
# 				out.write(",")