# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response

from django.http import HttpResponseBadRequest, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json



from right.models import Employee

def build_employee_all(request):
    resource = '/employee/?page=%d&limit=%d&exist=%d'

    try:
        page   = int( request.GET.get('page',  '1') )
        limit  = int( request.GET.get('limit', '20') )
        exist  = int( request.GET.get('exist', '1') )
    except:
        return HttpResponseBadRequest()
    
    es = Employee.objects.select_related().all().order_by('id')
    if exist == 1:
        es = es.filter(login__isnull=False)
    
    es_pages = Paginator(es, limit)
    try:
        p = es_pages.page(page)
    except:
        return HttpResponseBadRequest()
    
    response_object = (
    {
        'meta' : 
        {
             'total_count' : es.count(),
             'total_pages' : es_pages.num_pages,
             'limit'       : limit,
             'page'        : page,
             'exist'       : exist,
             'uri_first'   : resource % ( es_pages.page_range[0] , limit, exist ),
             'uri_last'    : resource % ( es_pages.page_range[-1], limit, exist ),
             'uri_previous': resource % ( p.previous_page_number(), limit, exist ) if p.has_previous() else None,
             'uri_next'    : resource % ( p.next_page_number(), limit, exist ) if p.has_next() else None,
             'uri_allexist': resource % ( page, limit, 0 ),
             'uri_exist'   : resource % ( page, limit, 1 ),
        },
        'objects' : list(obj.get_general() for obj in p.object_list)
    })
    return response_object
    
    
def rest_employee_all(request):
    response_object = build_employee_all(request)

    response = HttpResponse(json.dumps(response_object))
    response['Content-Type'] = 'application/json;'
    return response

def html_employee_all(request):
    response_object = build_employee_all(request)
    return render_to_response('employee_list.html', { 'data': response_object })






def build_employee(request,id):
    try:
        e = Employee.objects.select_related('role').get(pk=id)
    except:
        return HttpResponseBadRequest()
    
    response_object = (
    {
        'meta' : 
        {
            'is_admin'   : e.have_admin_rights(),
            'is_technic' : e.have_technic_rights(),
        },
        'object' : 
        {
            'general'    : e.get_general(),
            'operations' : e.get_operations(),
            'owner_of'   : e.get_equipment(),
            'tasks'      : e.get_tasks()
        }
    })
    return response_object


def rest_employee(request, id):
    response_object = build_employee(request, id)
    
    response = HttpResponse(json.dumps(response_object))
    response['Content-Type'] = 'application/json;'
    return response

def html_employee(request, id):
    response_object = build_employee(request, id)
    return render_to_response('employee_card.html', { 'data': response_object })






from left.models import Equipment

def build_equipment(request,id):
    try:
        e = Equipment.objects.select_related('equipment_model').get(pk=id)
    except:
        return HttpResponseBadRequest()
    
    response_object = (
    {
        'meta' : 
        {
        },
        'object' : 
        {
            'general'    : e.get_general(),
            'owners'     : e.get_owners(),
            'operations' : e.get_operations(),
            'tasks'      : e.get_tasks()
        }
    })
    return response_object


def rest_equipment(request, id):
    response_object = build_equipment(request,id)
    
    response = HttpResponse(json.dumps(response_object))
    response['Content-Type'] = 'application/json;'
    return response

from left.models import Task
def get_equipment_by_task(request, task_id):
    response_object = Task.objects.get(pk=task_id).get_attached_equipment()
    
    response = HttpResponse(json.dumps(response_object))
    response['Content-Type'] = 'application/json;'
    return response

def set_equipment_for_task(request, task_id, equipment_id):
    if request.method == 'POST':
        Task.objects.get(id=task_id).equipment.add(equipment_id)
        return HttpResponse(status=201)
    elif request.method == 'DELETE':
        Task.objects.get(id=task_id).equipment.remove(equipment_id)
        return HttpResponse(status=202)
    return HttpResponseBadRequest()

from datetime import datetime as dt
def post_new_task(request):
    if request.method == 'POST':
        client_id= request.REQUEST.get('client_id', None)
        datetime = request.REQUEST.get('datetime',  '%s' % dt.now())
        name     = request.REQUEST.get('name',  'blablabla')
        priority = request.REQUEST.get('priority', '3')
        priority = int(priority)
        return HttpResponse(status=201)
    return HttpResponseBadRequest()
