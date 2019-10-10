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

def tracking_resource_downloads_count(url):
    '''Restituisce il numero di downloads totali di una data risorsa

       :param url: url della risorsa
       :rtype: number
    '''
    tracking_res_summary = TrackingSummary.get_for_resource(url)
    return tracking_res_summary['total']

def tracking_resource_downloads(number, min=1):
    title = ungettext('{number} download', '{number} downloads', number)
    return h.snippet('snippets/resource_tracking_item.html',
                   title=title, number=number, min=min)

def dataset_tracking_views_sum():
    '''Restituisce il numero di visualizzazioni totali ottenute sommando quelle di ciascun package (dataset).
       Attenzione: la tabella 'tracking_summary' traccia il numero di visualizzazioni totali tenendo traccia anche del giorno,
       per ogni package (dataset) non c'e' solo una riga nella tabella ma ce ne tante quanti i giorni per i quali
       e' stata registrata la statistica, si prende il valore MAX per ogni dataset, e su questo si fa la SUM.

       :rtype: number
    '''
    result = Session.execute("select SUM(q.running_total) total_count FROM ( "
                                          "select MAX(t.running_total) AS running_total "
                                            "FROM tracking_summary t "
                                            "JOIN package p ON p.id=t.package_id "
                                            "GROUP BY t.package_id) AS q")
    total_count = 0
    for row in result:
      total_count = row['total_count']
    return total_count
