import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()

requires = [
    'cornice<2',
    'waitress',
    'pyramid',
    'pyramid_debugtoolbar',
    'docker-compose<1.4.0',
    'CouchDB',
    'setuptools==28.8.0'
]

setup(name='amhappy',
      version='0.2',
      description='amhappy',
      long_description=README,
      classifiers=[
          "Programming Language :: Python",
          "Framework :: Pylons",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application"
      ],
      keywords="web services",
      author='',
      author_email='',
      url='',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      entry_points = """\
      [paste.app_factory]
      main = amhappy:main
      """,
      paster_plugins=['pyramid'])
