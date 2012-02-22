from setuptools import setup, find_packages

# Check for Plone versions
try:
    from plone.app.upgrade import v40
    HAS_PLONE40 = True
except ImportError:
    HAS_PLONE40 = False

base_requires=[
          'setuptools',
          'Solgema.ContextualContentMenu',
          'plone.app.z3cform',
          'plone.z3cform',
          'z3c.form',
          'collective.js.colorpicker',
          'collective.js.fullcalendar>=1.5.2.1',
          'collective.js.jqueryui>=1.8.16.4',
          # -*- Extra requirements: -*-
      ]

plone4_requires = ['collective.js.jqueryui>=1.8.16.4',]

plone3_requires = [
            'zope.i18n=3.6',
            'zope.schema=3.8.1',
            'collective.js.jqueryui=1.7.2.7',
      ]

if HAS_PLONE40:
      install_requires = base_requires + plone4_requires

if not HAS_PLONE40:
      install_requires = base_requires + plone3_requires
      
version = '2.0.1'

setup(name='Solgema.fullcalendar',
      version=version,
      description="Solgema",
      long_description=open("README.rst").read() + "\n" +
                       open("CHANGES.txt").read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='Solgema, fullcalendar, diary',
      author='Martronic SA',
      author_email='martronic@martronic.ch',
      url='http://www.martronic.ch/Solgema/plone_products/solgema_fullcalendar',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Solgema'],
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
