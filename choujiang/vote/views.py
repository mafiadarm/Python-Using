import json
import pandas as pd

from django.shortcuts import render
from django.http import HttpResponse
from .models import Votes, People, Start
from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode


# Create your views here.


def get_ip(request):
    if "HTTP_X_FORWARDED_FOR" in request.META:
        ip = request.META("HTTP_X_FORWARDED_FOR")
    else:
        ip = request.META.get("REMOTE_ADDR", "unknown")
    return ip


def vote_index(request):
    start = Start.objects.all().first()
    if not start.flag:
        return HttpResponse('请等待开始')
    votes = Votes.objects.all()
    content = {'votes': votes, 'level': '年会节目投票'}
    return render(request, 'vote.html', content)


def make_score(request):
    post = request.POST
    add_score_list = post.getlist('items')
    check_ip = get_ip(request)
    if People.objects.filter(user_ip=check_ip):
        return render(request, 'error.html', {'error': '您已经投过了', 'check': 0})
    if len(add_score_list) != 3:
        return render(request, 'error.html', {'error': '请选择3个', 'check': 1})
    else:
        for name in add_score_list:
            p = People()
            p.user_ip = check_ip
            p.from_host = request.get_host()
            p.visits_url = request.get_full_path()
            p.target = name
            p.save()

            add_score = Votes.objects.get(name=name)
            add_score.score += 1
            print(add_score.score)
            add_score.save()
        return render(request, 'error.html', {'error': '谢谢投票', 'check': 2})


def get_score(request):
    data = Votes.objects.all().values_list()

    vs = pd.DataFrame(data, columns=['id', 'name', 'art', 'score'])
    vs['color'] = vs.score / vs.score.sum() * 100
    vs.sort_values('score', inplace=True)
    vs_data = vs[['color', 'score', 'name']].values.tolist()
    vs_data.insert(0, ['score', 'amount', 'product'])

    return HttpResponse(json.dumps(vs_data))


def bar(request):
    return render(request, 'bar.html')


def view(request):
    return render(request, 'view.html')
