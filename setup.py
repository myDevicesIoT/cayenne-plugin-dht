import os
import subprocess

from setuptools import setup
  
classifiers = ['Development Status :: 4 - Beta',
               'Operating System :: POSIX :: Linux',
               'License :: OSI Approved :: MIT License',
               'Intended Audience :: Developers',
               'Programming Language :: Python :: 3',
               'Topic :: Software Development',
               'Topic :: Home Automation',
               'Topic :: System :: Hardware',
               'Topic :: System :: Monitoring']

setup(name             = 'cayenne-dht',
      version          = '0.1.0',
      author           = 'myDevices',
      author_email     = 'N/A',
      description      = 'myDevices Cayenne DHT sensor plugin',
      keywords         = 'myDevices IoT Cayenne DHT11 DHT22 AM2302 plugin',
      url              = 'https://www.mydevices.com/',
      classifiers      = classifiers,
      packages         = ['cayenne-dht'],
      install_requires = ['Adafruit_DHT'])