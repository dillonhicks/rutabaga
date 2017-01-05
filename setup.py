"""Render templates with jinja2"""
from setuptools import setup, find_packages

setup(
    name='rutabaga',
    version='0.0.1',
    url='https://github.com/dillonhicks/rutabaga',
    license='Apache License Version 2.0',
    author='Dillon Hicks',
    author_email='dillon@dillonhicks.io',
    description='Jinja2 Wrapper for CLI Rendering Tools',
    long_description=__doc__,
    package_dir={'': '.'},
    namespace_packages=[],
    packages=find_packages('.'),
    include_package_data=True,
    zip_safe=True,
    platforms='any',
    install_requires=['jinja2', 'pathlib2'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
