# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Memo
from .forms import MemoForm

def index(request):
    memos = Memo.objects.order_by('-updated_at')
    return render(request, 'index.html',  {'memos': memos})

def show(request, memokey):
    memo = Memo.objects.get(pk = memokey)
    return HttpResponse("%s:%s" % (memo.title,memo.content))

def create(request):
    if request.method == 'GET':
        form = MemoForm()
        return render(request, 'create.html', {'form': form})
    elif request.method == 'POST':
        form = MemoForm(request.POST)
        if form.is_valid():
            memo = form.save(commit=False)
            memo.save()
            return redirect('memo', memokey=memo.pk)

def modify(request, memokey):
    if request.method == "POST":
        memo = Memo.objects.get(pk = memokey)
        form = MemoForm(request.POST, instance=memo)
        if form.is_valid():
             form.save()
             return redirect('/memos')
    else:
        memo = Memo.objects.get(pk = memokey)
        # TODO: ユーザー認証のチェックを行う
        if memo:
            memo = Memo.objects.get(pk = memokey)
            form = MemoForm(instance = memo)
            return render(request, 'create.html', {'form': form, 'memo': memo})
        else:
            # エラーハンドリングの処理必要
            return render(request, 'warning.html')

def delete(request, memokey):
    memo = Memo.objects.get(pk = memokey)
    if memo:
        memo.delete()
        return redirect('/memos')
    else:
        # エラーハンドリングの処理必要
        return render(request, 'warning.html')