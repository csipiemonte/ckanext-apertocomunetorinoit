import ckan.plugins as plugins
import ckan.plugins.toolkit as plugins_toolkit
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

    # -------- IConfigurer implementations -------- #

    def update_config(self, config):
      plugins_toolkit.add_public_directory(config, 'public')
      plugins_toolkit.add_template_directory(config, 'templates')

    # -------- ITemplateHelpers implementations -------- #

    def get_helpers(self):
      aperTO_helpers = {
          'traking_views': helpers.traking_views,
      }
      return aperTO_helpers
