from django.shortcuts import render,redirect
from .models import * 
from .forms import * 
 
def show_ad(request):
    topic = Advert.objects.all()
    texts = []
    for i in topic:
        texts.append(i.text_set.all())
    count = texts.count(i)

    context={'topic':topic,
              'count':count,
              'texts':texts,
              }
    return render(request,'bulletin_board/bulletin-board.html',context)
 
def addMessage(request):
    form = CreateInText()
    if request.method == 'POST':
        form = CreateInText(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request,'bulletin_board/add-message.html',context)