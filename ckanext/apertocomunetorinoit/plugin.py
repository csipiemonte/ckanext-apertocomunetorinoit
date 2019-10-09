# encoding: utf-8

import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import ckanext.apertocomunetorinoit.helpers as helpers

try:
   from ckan.lib.plugins import DefaultTranslation
except ImportError:
   class DefaultTranslation():
       pass

class ApertoComuneTorinoPlugin(plugins.SingletonPlugin, DefaultTranslation):

    # IConfigurer
    plugins.implements(plugins.IConfigurer)

    # ITemplateHelpers
    plugins.implements(plugins.ITemplateHelpers)

    # ITranslation
    if toolkit.check_ckan_version(min_version='2.5.0'):
      plugins.implements(plugins.ITranslation, inherit=True)

    # -------- IConfigurer implementations -------- #

    def update_config(self, config):
      toolkit.add_public_directory(config, 'public')
      toolkit.add_template_directory(config, 'templates')

    # -------- ITemplateHelpers implementations -------- #

    def get_helpers(self):
      aperTO_helpers = {
        'tracking_views_count': helpers.tracking_views_count,
        'tracking_views': helpers.tracking_views,
        'tracking_resource_downloads_count': helpers.tracking_resource_downloads_count,
        'tracking_resource_views': helpers.tracking_resource_views,
        'tracking_resource_downloads': helpers.tracking_resource_downloads,
        'dataset_tracking_views_sum': helpers.dataset_tracking_views_sum,
      }
      return aperTO_helpers

    # ------------- ITranslation ---------------#

    def i18n_domain(self):
        '''Change the gettext domain handled by this plugin
        This implementation assumes the gettext domain is
        ckanext-{extension name}, hence your pot, po and mo files should be
        named ckanext-{extension name}.mo'''
        return 'ckanext-{name}'.format(name='apertocomunetorinoit')
