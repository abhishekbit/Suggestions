import csv
from os import close
import re
import difflib
import itertools

from re import  findall
from typing import final
from difflib import get_close_matches

reader = csv.reader(open('templates/python_assesment.csv'))

from django.shortcuts import render
from django.http import HttpResponse


def home(req): 
    return render(req, 'home.html')


def suggestions(req):
    productname = req.GET.get('ProductName')
    print("productname = ",productname)
    c=0
    cnt = 0
    suggestedlist = []    
    closelist=[]
    
    totallist=[]
  
    for product in reader:

        x=(product[1].split(" "))
        closelist.append((x))
        k = str(product[1])
        totallist.append(k)
       # searched_string = ''.join(re.findall(productname,k,re.IGNORECASE))
        searched_string = re.search(productname,k,re.IGNORECASE)

        if searched_string:
            final_string = searched_string.group(0) 
            cnt+=1
            suggestedlist.append(k)
        
        if cnt==20:
            break
        c+=1
     
 #  print("b=",b)
    m = list(itertools.chain(*closelist))
#   print("m=",m)
    final_closest_list=get_close_matches(productname.upper(),m)
    print("p=",final_closest_list)
    closest_match=[]
    flag=0
    for i in final_closest_list:
        for j in totallist:
            if i in j:
                closest_match.append(j)
            if len(closest_match)>=20:
                flag=1
                break
        if flag==1:
            break

    print("closest = ",closest_match)
 
    print("suggestedlist = ",suggestedlist)
    print("cnt=",cnt)
    return render(req, 'suggestions.html', {'ProductName': productname, 'suggestions':sorted(suggestedlist) } )

