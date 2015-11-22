# Copyright 2015 Yanis Guenane  <yanis@guenane.org>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from setuptools import setup, find_packages


setup(
    name='ics2task',
    version='0.0.1',
    description='An utility that converts ICS events into tasks in '
                'Taskwarrior',
    long_description='An utility that converts ICS events into tasks in '
                     'Taskwarrior',

    url='https://github.com/Spredzy/ics2task',

    author='Yanis Guenane',
    author_email='yanis@guenane.org',

    license='Apache V2.0',

    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
    ],

    install_requires=['icalendar', 'taskw'],
    packages=find_packages(exclude=['tests']),

    entry_points={
        'console_scripts': [
            'ics2task=ics2task:main',
        ],
    },
)
