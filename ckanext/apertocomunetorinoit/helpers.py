import ckan.model as model
import ckan.lib.helpers as h

from ckan.common import ungettext

def traking_views_count(package_id):
    tracking_summary = model.TrackingSummary.get_for_package(package_id)
    return tracking_summary['total']

def traking_views(package_id):
    number = traking_views_count(package_id)
    title = ungettext('{number} view', '{number} views', number)
    return h.snippet('snippets/package_tracking_item.html',
                   title=title, number=number, min=1)

def traking_resource_views_count(url):
    tracking_res_summary = model.TrackingSummary.get_for_resource(url)
    return tracking_res_summary['total']

def traking_resource_views(number, min=1):
    title = ungettext('{number} view', '{number} views', number)
    return h.snippet('snippets/package_tracking_item.html',
                   title=title, number=number, min=min)
