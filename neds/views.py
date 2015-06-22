# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth import logout


def home(request):
    return render(request, "index.html", {})


def home_files(request, filename):
    return render(request, filename, {}, content_type="text/plain")


def logout_view(request):
    logout(request)
    return home(request)
