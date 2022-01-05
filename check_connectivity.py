import datetime#why not
import requests #url
import time #time is important
import argparse #the arguments
import psycopg2 #postgresql

from pymongo import MongoClient #mongodb

#arguments stuff
parser = argparse.ArgumentParser()

parser.add_argument("-url", action='store', dest = 'url', help = 'Check this url')
parser.add_argument("-mongodb", action = 'store', dest = 'uridb', help = 'Check this URI to the DB')
parser.add_argument("-postgresql", action = 'store', dest = 'urisql', help = 'Check this uri ro SQL')
parser.add_argument("-t",action = 'store', dest = 'time', help = 'Check every x seconds')

result = parser.parse_args()

#output to file stuff
output = open("output.txt","a+")

#counter
counter = 1

#url checking
if result.url is not None:
    #print counter,time and link
    output.write(str(counter)+'\n')
    e = datetime.datetime.now()
    output.write("%s:%s:%s %s/%s/%s" % (e.hour, e.minute, e.second, e.day, e.month, e.year))
    output.write('\n')
    output.write(result.url)
    output.write('\n')
    counter=counter+1
    #trying to find the url and if nout found print the error
    try:
        r = requests.get(result.url)
        r.raise_for_status()
        output.write(str(r.status_code)+'\n')
        output.write(str(r.elapsed)+'\n')
        output.write('\n\n')
        r.close()
    except requests.exceptions.HTTPError as err:
        output.write(str(err))
        output.write('\n\n')

    if result.time is not None:
        #just going in circles every x seconds and retrying connecting
        while True:
            time.sleep(int(result.time))
            #print counter,time and link
            output.write(str(counter)+'\n')
            e = datetime.datetime.now()
            output.write("%s:%s:%s %s/%s/%s" % (e.hour, e.minute, e.second, e.day, e.month, e.year))
            output.write('\n')
            output.write(result.url)
            output.write('\n')
            counter=counter+1
            #trying to find the url and if not found print the error
            try:
                r = requests.get(result.url)
                r.raise_for_status()
                output.write(str(r.status_code)+'\n')
                output.write(str(r.elapsed)+'\n')
                output.write('\n\n')
                r.close()  
            except requests.exceptions.HTTPError as err:
                output.write(str(err))
                output.write('\n\n')

#mongodb checking
if result.uridb is not None:
    #print counter,time and uri
    output.write(str(counter)+'\n')
    e = datetime.datetime.now()
    output.write("%s:%s:%s %s/%s/%s" % (e.hour, e.minute, e.second, e.day, e.month, e.year))
    output.write('\n')
    output.write(result.uridb)
    output.write('\n')
    counter=counter+1
    #trying connection to mongodb
    start = time.time()#elapsed time
    client = MongoClient(result.uridb)
    end = time.time()
    version = tuple(client.server_info()['version'].split('.'))
    if version is not None:
        output.write('Connected to MongoDB \n')
        output.write(str(end-start))
        output.write('\n')
        output.write('Version:' + str(version))
        output.write('\n\n')
        client.close()
    else:
        output.write("Not found")
        output.write('\n\n')        
    

    if result.time is not None:
        #just going in circles every x seconds and retrying connecting
        while True:
            time.sleep(int(result.time))
            #print counter,time and uri
            output.write(str(counter)+'\n')
            e = datetime.datetime.now()
            output.write("%s:%s:%s %s/%s/%s" % (e.hour, e.minute, e.second, e.day, e.month, e.year))
            output.write('\n')
            output.write(result.uridb)
            output.write('\n')
            counter=counter+1
            #trying connection to mongodb
            start = time.time()#elapsed time
            client = MongoClient(result.uridb)
            end = time.time()
            version = tuple(client.server_info()['version'].split('.'))
            if version is not None:
                output.write('Connected to MongoDB \n')
                output.write(str(end-start))
                output.write('\n')
                output.write('Version:' + str(version))
                output.write('\n\n')
                client.close()
            else:
                output.write("Not found")
                output.write('\n\n')   

#postgresql checking
if result.urisql is not None:
    #print counter,time and uri
    output.write(str(counter)+'\n')
    e = datetime.datetime.now()
    output.write("%s:%s:%s %s/%s/%s" % (e.hour, e.minute, e.second, e.day, e.month, e.year))
    output.write('\n')
    output.write(result.urisql)
    output.write('\n')
    counter=counter+1
    #i guess postgresql
    try:
        conn = psycopg2.connect(host=result.urisql)
    except psycopg2.OperationalError as err:
        output.write(str(err))
        output.write('\n\n')
    if result.time is not None:
        #just going in circles every x seconds and retrying connecting
        while True:
            time.sleep(int(result.time))
            #print counter,time and uri
            output.write(str(counter)+'\n')
            e = datetime.datetime.now()
            output.write("%s:%s:%s %s/%s/%s" % (e.hour, e.minute, e.second, e.day, e.month, e.year))
            output.write('\n')
            output.write(result.urisql)
            output.write('\n')
            counter=counter+1
            #i guess postgresql
            try:
                conn = psycopg2.connect(host=result.urisql)
            except psycopg2.OperationalError as err:
                output.write(str(err))
                output.write('\n\n')

output.close()#closing the file after we're done