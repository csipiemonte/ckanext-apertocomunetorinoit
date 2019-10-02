import ckan.model as model
import ckan.lib.helpers as h

from ckan.common import ungettext

def traking_views(package_id):
    tracking_summary = model.TrackingSummary.get_for_package(package_id)
    number = tracking_summary['total']
    title = ungettext('{number} view', '{number} views', number)
    return h.snippet('snippets/package_tracking_item.html',
                   title=title, number=number, min=1)
