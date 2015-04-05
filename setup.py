from setuptools import setup

setup(name='Warehouse', version='1.0',
      description='Autonomi Warehouse',
      author='Pragya Jaiswal', author_email='pragya.jswl@gmail.com',

      #  Uncomment one or more lines below in the install_requires section
      #  for the specific client drivers/modules your application needs.
      install_requires=['flask','pymongo'],
     )