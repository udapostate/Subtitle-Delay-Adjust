# encoding: UTF-8
#!/usr/bin/python
# Filename: using_file.py
import sys
import time
import re
input_file = sys.argv[1]
time = sys.argv[2]


pattern1 = re.compile('\w*.srt')
pattern2 = re.compile('\w*.ass')

match1 = pattern1.match(input_file)
match2 = pattern2.match(input_file)




def time2itv(sTime):
        slist = sTime.split(':')
        sslist = slist[2].split(',')
        return int(slist[0])*3600+ int(slist[1])*60 + int(sslist[0])
                




def time2itv_ass(sTime):
        slist = sTime.split(':')
        sslist = slist[2].split('.')
        return int(slist[0])*3600+ int(slist[1])*60 + int(sslist[0])
                


def itv2time(iItv):
	if type(iItv)==type(1):
		h=iItv/3600
		sUp_h=iItv-3600*h
		m=sUp_h/60
		sUp_m=sUp_h-60*m
		s=sUp_m
                if h>9:
                        strh = str(h)
                else:
                        strh = '0'+str(h)
                if m>9:
                        strm = str(m)
                else:
                        strm = '0'+str(m)
                if s>9:
                        strs = str(s)
                else: 
                        strs = '0'+str(s)
                        
                return ":".join([strh,strm,strs])
	else:
		return "[InModuleError]:itv2time(iItv) invalid argument type"



#     if match:
        
pattern = re.compile('\d\d:\d\d:\d\d,\d*')

pattern3 = re.compile('\d:\d\d:\d\d.\d\d')



if match1:
        fp=open(sys.argv[1],'r')  
        alllines=fp.readlines()  
        fp.close() 
        filename = "my" + sys.argv[1]
        fp=open(filename,'w')  
        for eachline in alllines:
                alist = eachline.split()
                newlist = []
                for s1 in alist:
                        match = pattern.match(s1)
                        if match:
                                s = itv2time(time2itv(s1)+int(time))
                                s +=','+s1.split(',')[1]
                                s1 = s
                        newlist.append(s1)
                newline = " ".join(newlist)
                fp.writelines(newline)
                        
    


if match2:
        fp=open(sys.argv[1],'r')  
        alllines=fp.readlines()  
        fp.close() 
        filename = "my" + sys.argv[1]
        fp=open(filename,'w')  
        for eachline in alllines:
                alist = eachline.split(',')
                newlist = []
                for s1 in alist:
                       # print (s1)
                        match = pattern3.match(s1)
                        if match:
                                s = itv2time(time2itv_ass(s1)+int(time))
                                s +='.'+s1.split('.')[1]
                                s1 = s
                                #print (s1)
                        newlist.append(s1)
                newline = ",".join(newlist)
                fp.writelines(newline)
                        
    


# if match2:

