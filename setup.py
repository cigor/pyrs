import os
import sys


from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()



requires = [
    'paramiko',
    'protobuf'
]

test_requires = [
]


setup(name='pyrs',
      version='0.1',
      description='Using this library you can control your retroshare instance programatically in python.',
      long_description=README,
      classifiers=[
      "Programming Language :: Python",
          "Topic :: Communications :: Chat",
          "Topic :: Communications :: File Sharing",
      ],
      author='drbob',
      author_email='',
      url='https://github.com/drbob/pyrs',
      keywords='retroshare protobuf rpc',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      #extras_require=extras_require,
      tests_require=test_requires,
      )
