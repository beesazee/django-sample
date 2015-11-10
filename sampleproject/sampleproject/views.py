__author__ = 'sibi'
from django.shortcuts import render,redirect ,get_object_or_404
from django.http import HttpResponse
from time import ctime

def home(request):
    html = """
    <h1>Django CRUD Example</h1>
    <pre>{}</pre>
    <a href='/crud/new'>add employee</a>
    <a href='/crud'>Employee list</a>
    """.format(ctime())
    return HttpResponse(html)