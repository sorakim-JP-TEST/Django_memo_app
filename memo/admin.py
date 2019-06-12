# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Memo

# Memo モデルを登録
admin.site.register(Memo)
