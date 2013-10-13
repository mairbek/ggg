from setuptools import setup

# resources go here
resources = ['resources/*']

setup(name = 'gve',
    version = '0.1-SNAPSHOT',
    description = 'Virtual env for golang projects',
    author = 'Mairbek Khadikov',
    author_email = 'mkhadikov@gmail.com',
    url = 'http://github.com/mairbek/gve',
    packages = ['gve'],
    package_data = {'gve' : resources },
    entry_points={
        'console_scripts': [
            'gve = gve.__main__:main',
        ],
    },
    long_description = """ TODO write one """
) 
