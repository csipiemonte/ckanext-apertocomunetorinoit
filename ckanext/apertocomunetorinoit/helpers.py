# encoding: utf-8

'''AperTO Helper functions

Functions utilizzate nei template di AperTO che estendono quelli di CKAN.
'''

import ckan.lib.helpers as h

from ckan.common import ungettext
from ckan.model import Session, meta, Package, TrackingSummary

from sqlalchemy.sql import func

def tracking_views_count(package_id):
    '''Restituisce il numero di visualizzazioni totali di un dato package (dataset)

       :param package_id: id del package (dataset)
       :rtype: number
    '''
    tracking_summary = TrackingSummary.get_for_package(package_id)
    return tracking_summary['total']

def tracking_views(package_id):
    number = tracking_views_count(package_id)
    title = ungettext('{number} view', '{number} views', number)
    return h.snippet('snippets/package_tracking_item.html',
                   title=title, number=number, min=1)

def tracking_resource_views_count(url):
    '''Restituisce il numero di visualizzazioni totali di una data risorsa

       :param url: url della risorsa
       :rtype: number
    '''
    tracking_res_summary = TrackingSummary.get_for_resource(url)
    return tracking_res_summary['total']

def tracking_resource_views(number, min=1):
    title = ungettext('{number} view', '{number} views', number)
    return h.snippet('snippets/package_tracking_item.html',
                   title=title, number=number, min=min)

def dataset_tracking_views_sum():
    '''Restituisce il numero di visualizzazioni totali ottenute sommando quelle di ciascun package (dataset).
       Il codice sottostante e' scritto secondo la sintassi di SQLAlchemy (the Python SQL toolkit and Object Relational Mapper).

       :rtype: number
    '''

    obj = meta.Session.query(func.sum(TrackingSummary.running_total).label('total_views')).\
                autoflush(False).\
                join(Package, Package.id == TrackingSummary.package_id)
    data = obj.first()
    return data.total_views
