from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^listing(/(?P<repo>[A-Za-z0-9@._+\-]+))??(/(?P<pkgname>[A-Za-z0-9@._+\-]+))?/?$', views.listing, name='listing'),
    url(r'^man/'
        r'((?P<repo>[A-Za-z0-9@._+\-]+)/)??'
        r'((?P<pkgname>[A-Za-z0-9@._+\-]+)/)?'
        r'(?P<name_section_lang>[A-Za-z0-9@._+\-:\[\]]+?)'
        r'(\.(?P<url_output_type>html|txt|raw))?$',
        views.man_page, name='man_page'),
    url(r'^search', views.search, name="search"),
    url(r'^(?P<template_name>[a-z]+)', views.simple_view, name='simple_view'),
]
