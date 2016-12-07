#-*- coding: utf8 -*-

from setuptools import setup

setup(
    name='python-lora',
    version='0.1',
    description='Python interface for certain Semtech SX127x and HopeRF RFM9x chips',
    url='http://github.com/netom/pylora',
    author='Fábián Tamás László',
    author_email='giganetom@gmail.com',
    license='MIT',
    packages=['lora'],
    install_requires=[
        'spidev'
    ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: System :: Hardware :: Hardware Drivers'
    ],
    include_package_data=True,
    zip_safe=False)

