from right.models import Employee

from django.shortcuts import render_to_response


def employee_card(request, snils):
    e = Employee.objects.get(snils=snils)
    return render_to_response('employee_card.html', { 'employee': e })


def employee_list_all(request):
    offset = int( request.GET.get('offset', '0') )
    limit  = int( request.GET.get('limit', '20') )
    es = Employee.objects.all()
    resource = '/rest/right/employee/?offset=%d&limit=%d&format=json' % (offset, limit) 

    meta = dict()
    meta['offset']       = offset
    meta['limit']        = limit
    meta['total_count']  = es.count()
    
    link = '/rest/right/employee/?offset=%d&limit=%d&format=json'
    if offset + limit < meta['total_count']:
        meta['next']     = link % (offset+limit, limit)
    else:
        meta['next']     = None
        
    if offset - limit > 0:
        meta['previous'] = link % (offset-limit, limit)
    elif offset == 0:
        meta['previous'] = None
    else:
        meta['previous'] = link % (0, limit)
        
    return render_to_response('employee_list.html', { 'employees': list(es[offset:offset+limit]), 
                                                      'meta' : meta })


def employee_list_existing(request):
    offset = int( request.GET.get('offset', '0') )
    limit  = int( request.GET.get('limit', '20') )
    es       = Employee.objects.exclude(login=None)[offset:offset+limit]
    resource = '/rest/right/employee/?login__isnull=False&offset=%d&limit=%d&format=json' % (offset, limit) 
    return render_to_response('employee_list.html', { 'employees': list(es), 'resource' : resource })

