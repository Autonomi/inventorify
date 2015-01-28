from setuptools import setup

setup(name='Warehouse', version='1.0',
      description='Autonomi Warehouse',
      author='Your Name', author_email='ramr@example.org',

      #  Uncomment one or more lines below in the install_requires section
      #  for the specific client drivers/modules your application needs.
      install_requires=['bottle','pymongo'],
     )