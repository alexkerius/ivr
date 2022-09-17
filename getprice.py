import requests
import re
def price():
    create_file()
    with open("html.txt","r") as file_opened:
        lines=file_opened.readlines()
    pattern="""<div class="fs">[0-9]\s[0-9]+\s[0-9]+"""
    pattern1="[0-9]\s[0-9]+\s[0-9]+"
    list1=[]
    for line in lines:
        if(re.search(pattern,line)):
            list1.append(line)
            break
    for element in list1:
        for i in re.findall(pattern1,element):
            return i
    
def get_html():
    url="https://www.bestchange.com/qiwi-to-bitcoin.html"
    html=requests.get(url).text
    return html
    
def create_file():
    file=open("html.txt","w+",encoding="utf-8")
    file.write(get_html())


