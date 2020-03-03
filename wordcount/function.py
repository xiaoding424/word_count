#from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request,'home.html')


def count(request):
    user_text = request.GET['text']
    total_count=len(user_text)

    word_dict = {}
#创建一个字典统计重复出现的字
    for word in user_text:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word]+=1
#给出现字的次数排序，用sorted方法
    sorted_dict = sorted(word_dict.items(),key=lambda w:w[1],reverse=True)
#items:将字典迭代化
    return render(request,'count.html',{'count':total_count, 'text':user_text,
                                        'word':word_dict, 'sorted':sorted_dict})