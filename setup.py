#!/usr/bin/python3
# -*- coding: utf-8 -*-


import setuptools


with open('./README.rst', 'r') as file:
    long_desc = file.read()


# set-up script for pip distribution
setuptools.setup(
    name = 'jspcapy',
    version = '0.1.3',
    author = 'Jarry Shaw',
    author_email = 'jarryshaw@icloud.com',
    url = 'https://github.com/JarryShaw/jspcap/jspcapy/',
    license = 'GNU General Public License v3 (GPLv3)',
    keywords = 'computer-networking pcap-analyzer pcap-parser',
    description = 'A command line pcap file analyser tool.',
    long_description = long_desc,
    python_requires = '>=3.6',
    py_modules = ['jspcapy'],
    entry_points = {
        'console_scripts': [
            'jspcapy = src.jspcapy:main',
        ]
    },
    packages = [],
    package_data = {
        '': [
            'LICENSE.txt',
            'README.md',
            'README.rst',
        ],
        'jsformat': ['*.py'],
        'jspcap': ['*.py'],
    },
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: MacOS X',
        'Environment :: Win32 (MS Windows)',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: System :: Networking',
        'Topic :: Utilities',
    ]
)