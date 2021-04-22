import paramiko
import psycopg2
import re

username,password = "antlou-6","Mobles112"
host,port = "sftp.student.ltu.se",22
filepath = "/nfs/students/antlou-6/botnia/bilder/"

def create_table():
    conn=psycopg2.connect("dbname='botnia' user='postgres' password='Mobles112' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS image (id SERIAL PRIMARY KEY)")
    conn.commit()
    conn.close()

def insert():
    conn=psycopg2.connect("dbname='botnia' user='postgres' password='Mobles112' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("INSERT INTO image VALUES (DEFAULT)")
    conn.commit()
    conn.close()

def view():
    conn=psycopg2.connect("dbname='botnia' user='postgres' password='Mobles112' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("SELECT id FROM image ORDER BY id DESC LIMIT 1")
    rows = cur.fetchall()
    conn.close()
    return rows

def upload_file(localpath):
    paramiko.util.log_to_file("paramiko.log")
    transport = paramiko.Transport((host,port))
    transport.connect(None,username,password)    
    sftp = paramiko.SFTPClient.from_transport(transport)
    #concatenates list-value to file output path string
    viewOutput = str(view()) + ".jpg"
    fixedOutput = re.sub(r"\((,*?)\)","", viewOutput)
    outputpath = filepath + fixedOutput
    sftp.put(localpath,outputpath)

create_table()
insert()

#add file path of picture to upload
upload_file("newyork.jpg")