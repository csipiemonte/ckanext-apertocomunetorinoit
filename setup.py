from setuptools import setup, find_packages  # Always prefer setuptools over distutils
from codecs import open  # To use a consistent encoding
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ckanext-apertocomunetorinoit',
    version = '1.0.0',
    description="CKAN customizations for aperto.comune.torino.it",
    long_description="CKAN customizations for aperto.comune.torino.it",
    author="Carlo Peraudo",
    author_email="carlo.peraudo@consulenti.csi.it",
    url='http://aperto.comune.torino.it',
    license='AGPL',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        # 3 - Alpha
        # 4 - Beta
        # 5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    namespace_packages=['ckanext', 'ckanext.apertocomunetorinoit'],
    include_package_data=True,
    package_data={
    },
    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages.
    # see http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    data_files=[],
    install_requires=[],
    entry_points='''
        [ckan.plugins]
        apertocomunetorinoit = ckanext.apertocomunetorinoit.plugin:ApertoComuneTorinoPlugin
    '''
)
