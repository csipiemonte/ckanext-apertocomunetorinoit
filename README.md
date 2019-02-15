# Ckan plugin for aperto.comune.torino.it

[CKAN] Extension for the Comune di Torino (http://aperto.comune.torino.it)

[Ckan]: http://ckan.org

## Plugins

Available plugins in this extension:

- ``apertocomunetorinoit``: Theme customization

## Installation

1. Activate your CKAN virtual environment, for example:

     `. /usr/lib/ckan/default/bin/activate`
     
2. Go into your CKAN path for extension (like /usr/lib/ckan/default/src):

    `git clone https://github.com/csipiemonte/ckanext-apertocomunetorinoit.git`
    
    `cd ckanext-apertocomunetorinoit`
    
    `pip install -e .`

3. Add ``apertocomunetorinoit`` to the ``ckan.plugins`` setting in your CKAN config file (by default the config file is located at ``/etc/ckan/default/production.ini``).

5. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu::

     sudo service apache2 reload
