#! /usr/bin/env python3

# In this script
# I process text files with python dictionaries and 
# upload to running web services


import os
import requests

BASEPATH = "./data/feedback/"

directory = os.listdir(BASEPATH)

list = []


for file in directory:
    with open(BASEPATH + file, 'r') as f:
        list.append({
            "title": f.readline().rstrip("\n"),
            "name": f.readline().rstrip("\n"),
            "date": f.readline().rstrip("\n"),
            "feeback": f.read().rstrip("\n")
        })


for item in list:
    response = requests.post("http:127.0.0.1/feedback/", json=item)
    if response.status_code !=201:
        raise Exception(f"POST error statu={response.status_code}")
    print(f"Created feedback ID: {response.json()["id"]}")