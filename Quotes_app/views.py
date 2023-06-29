import json
import requests
from django.shortcuts import render
def home(request):
    ins_res = requests.get('https://api.api-ninjas.com/v1/quotes?category=inspirational',headers={'X-Api-Key':'nAvbZjOt/rx8UQz//3l0fg==tQIfqSgYzoGJGsBx '}).text
    # print(ins_res)
    ins_json = ins_res.strip('[]')
    ins_dict = json.loads(ins_json)
    quot = ins_dict['quote']
    author = ins_dict['author']
    
    return render(request,'home.html',{'quote':quot,'author':author})
# Create your views here.
