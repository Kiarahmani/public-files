import urllib.request
import sys
import os

# configure
input_file = "./cs-samples.csv"
output_dir = "./files/"
min_index = 1
max_index = 50


fp = open(input_file, 'r').readlines()
try:
    os.makedirs(output_dir)
except FileExistsError:
    print ()
except: 
    raise



for i in range(min_index,max_index):
    try:
        print ("\nDownloading from "+fp[i])
        file = urllib.request.urlretrieve(fp[i], output_dir+"file_"+str(i)+".cs")
    except urllib.error.HTTPError:
        print ("error 404\n")
        continue
    except UnicodeDecodeError:
        print ("decoding error\n")
        continue
    except:
        print ("unknown error\n")
        continue
    print ("success!\n")

