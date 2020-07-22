"""Main entry point
"""
from pyramid.config import Configurator


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include("cornice")
    config.scan("amhappy.resources")
    config.scan("amhappy.views")
    if 'bower_path' in settings:
        config.add_static_view(
            name='/bower_components',
            path=settings['bower_path'])
    config.add_static_view(
        name='/',
        path=settings['frontend_path'])
    return config.make_wsgi_app()
