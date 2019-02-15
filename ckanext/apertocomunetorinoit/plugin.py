
import ckan.plugins as plugins
import logging
import ckan.plugins.toolkit as plugins_toolkit

from ckan.common import _, ungettext

try:
   from ckan.lib.plugins import DefaultTranslation
except ImportError:
   class DefaultTranslation():
       pass

log = logging.getLogger(__name__)

class ApertoComuneTorinoPlugin(plugins.SingletonPlugin, DefaultTranslation):

    # IConfigurer
    plugins.implements(plugins.IConfigurer)

    # Implementation of IConfigurer
    # ------------------------------------------------------------

    def update_config(self, config):
        plugins_toolkit.add_public_directory(config, 'public')
        plugins_toolkit.add_template_directory(config, 'templates')

