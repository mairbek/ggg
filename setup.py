from setuptools import setup

# resources go here
resources = ['resources/*']

setup(name='ggg',
      version='0.1',
      description='Virtual env for golang projects',
      author='Mairbek Khadikov',
      author_email='mkhadikov@gmail.com',
      url='http://github.com/mairbek/ggg',
      packages=['ggg'],
      package_data={'ggg': resources},
      entry_points={
          'console_scripts': [
              'ggg = ggg.__main__:main',
          ],
      },
      long_description=""" TODO write one """)
