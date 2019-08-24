
import argparse
import os.path
import difflib
import time
import datetime
import random
import hashlib
import shutil
import sys
from os import path
from serverd import sent
from clientd import receive
 
def log(file_name):
    path=os.getenv("HOME")
    newpath=path+"/dgit/"+file_name
    s1="/record.txt"
    
    n=0
    print(newpath+s1)
    with open(newpath+s1,"r") as f:
        for line in f:
           n=n+1 
           
    print(n)
    with open(newpath+s1,"r+") as f:
        data = f.readlines()
        
    datas=[]
    print("\nCommits Maded for "+file_name+"\n")
    for i in range(n):
        
	    print(data[i].replace(" ","..."))
    	#print(data[i])
    #print(datas)
    f.close()

def push(file_name):
	print ("pushed %s"%(file_name))
	dpath=os.getcwd()
	despath=dpath+'/'+file_name
	print(despath)
	sent(file_name)
	
def pull():
	receive()

def revert(file_name,filename):   
    print ("reverted to commit  %s"%(filename)) 
    
    '''fil1=filename.replace("/"," ")
    print(fil1)'''
    path=os.getenv("HOME")
    curpath=path+"/dgit/"+file_name+'/'+filename+'.txt'
    print(curpath)

    dpath=os.getcwd()
    despath=dpath+'/'+file_name
    print(despath)

    
    with open(curpath,"r") as f:
        with open(despath,"w") as f1:
            for line in f:
                f1.write(line)

    f.close()
    f1.close()

    '''            
    path=os.getenv("HOME")
    cur_path=path+"/dgit/"+file_name+'/'+filename+'.patch'
    orgfile=path+'/dgit/originalfiles/'+file_name
    comd='echo " ">'+orgfile
    os.system(comd)
    cmd1='patch -R '+orgfile+' < '+cur_path	
    #cmd1='patch '+orgfile+'< '+cur_path
    os.system(cmd1)'''
            
         
        



	
def init():
	#path=os.getcwd()
	path=os.getenv("HOME")
	newpath=path+"/dgit"
	paths=path
	anpath=path+"/dgit/originalfiles"
	print("Initialized new dgit repository at" + path)
	if not os.path.exists(newpath):
		os.mkdir(newpath)
	
	if not os.path.exists(anpath):
		os.mkdir(anpath);
	
		
	
def add(file_name):

	print ("added %s"%(file_name))
	path=os.getcwd()
	print(path)
	cur_path=path+'/'+file_name
	print(cur_path)
	
	
	mainpath=os.getenv("HOME")
	#s='main.txt'
	main_path=mainpath+'/dgit/originalfiles'
	#print(main_path)
	shutil.copy(cur_path,main_path)
	'''
    with open(cur_path, "r") as f:
	    with open(main_path, "w+") as f1:
		    for line in f:
			    f1.write(line)
				
				
    f2 = open(os.path.join(mainpath+'/dgit/', 'main.txt'), 'wb')
    with open(file_name) as f1:
    	    f1_text = f1.read()
    with open(main_path) as f2:
    	    f2_text = f2.read()
    	
    	#fbfbg
    		#for line in difflib.unified_diff(f1_text, f2_text,fromfile=f1,tofile=f2):
	        #	print (line)
	#cmd='diff -u '+file_name+' '+main_path+'>'+main_path
	#os.system(cmd)
	#print('ret='+ret)
	
    f1.close()
    f2.close()
'''
	paths=os.getenv("HOME")
	dirname=paths+'/dgit/'+file_name
	print(dirname)
	a=str(os.path.exists(dirname))
	#print('a='+a)
	if(a=='False'):
		os.mkdir(dirname)
		f = open(os.path.join(dirname, 'record.txt'), 'w')
		f.close()
	
	
	
	
	
	
	'''
	l=[]
	path=os.getcwd()
	for subdir, dirs, files in os.walk(path):
		dirs.clear()
		for file in files:
			l.append(file);
	print(l)
	print(len(l))
	print(l[0])
	
	main_path=""
	main_path=path+"/dgit/"
	j=0
	for i in range(0,len(l)):
		with open(path+'/'+str(l[i]),"r") as f:
			print(l[0])
			with open(main_path+'b'+str(j)+".txt", "w+") as f1:	
				j=j+1;
				for line in f:
					f1.write(line)'''
				
	f1.close()
	f.close()
	
 


def commit(filename):
	
	ts=time.time()
	st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_%H:%M:%S')	
	id1=random.randint(1,101)
	print(id1)
	hash1=''
	hash1=hashlib.sha256(str(id).encode()).hexdigest()
	path=os.getcwd()
	s=os.listdir(path)

	s1=st+'.txt'

	path=os.getcwd()
	print(path)
	cur_path=path+'/'+filename
	print(cur_path)
	
	mainpath=os.getenv("HOME")
	new_path=mainpath+'/dgit/'+filename+'/'+s1
	
	shutil.copy(cur_path,new_path)
	
	rcrd_path=mainpath+'/dgit/'+filename+'/record.txt'
	f2=open(rcrd_path,"a")
	f2.write(st)
	f2.write("\n")
	
	'''
	with open(main_path,"r") as f:
		with open(new_path, "w+") as f1:
			for line in f:
				f1.write(line)
			#f1.write(st)
			'''
	

      	
'''def commit(filename):
	
	ts=time.time()
	st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_%H:%M:%S')	
	id1=random.randint(1,101)
	print(id1)
	hash1=''
	hash1=hashlib.sha256(str(id).encode()).hexdigest()
	path=os.getcwd()
	s=os.listdir(path)
	
	mainpath=os.getenv("HOME")
	dirname=mainpath+'/dgit/'+filename
	orgfile=mainpath+'/dgit/originalfiles/'+filename
	
	s1=st+'.patch'
	
	new_path=mainpath+'/dgit/'+filename+'/'+s1
	
	
	cmd='diff -u '+filename+' '+orgfile+'>'+new_path
	os.system(cmd)
	
	rcrd_path=mainpath+'/dgit/'+filename+'/record.txt'
	f2=open(rcrd_path,"a")
	f2.write(st)
	f2.write("\n")
	
	
	with open(main_path,"r") as f:
		with open(new_path, "w+") as f1:
			for line in f:
				f1.write(line)
			#f1.write(st)
			
	
	#comd='echo " ">'+orgfile
	#os.system(comd)
	
	cmd1='patch -R '+orgfile+' < '+new_path
	os.system(cmd1)
	
	#os.rename(new_path,dirname)
	shutil.move(new_path,dirname)'''

	

	
def main():

	ts=time.time()
	st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')	
	l=[]
	path=os.getcwd()
	for subdir, dirs, files in os.walk(path):
		dirs.clear()
		for file in files:
			l.append(file);
			
	print(l)
	
	COMMAND_MAP = {'init' : init,
	               'add' : add,
	               'commit' : commit,
	               'log' : log,
                   'revert' : revert,
                   'push': push,
	         	   'pull': pull
                   }

	parser=argparse.ArgumentParser()
	parser.add_argument('command', choices=COMMAND_MAP.keys())
	parser.add_argument('file_name',nargs='?',default='')
	parser.add_argument('filename',nargs='?',default='')

	args = parser.parse_args()

	func = COMMAND_MAP[args.command]
	if args.command=='add':
		func(args.file_name)
	elif args.command=='revert':
	    func(args.file_name,args.filename)
	elif args.command=='commit':
	    func(args.file_name)
	elif args.command=='log':
            func(args.file_name)
	elif args.command=='push':
	    func(args.file_name) 
	
	else:
		func()
	

main()
