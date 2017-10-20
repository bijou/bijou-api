from setuptools import setup, find_packages
from os import path

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='bijou',
    version='0.0.1',
    install_requires=requirements,
    packages=find_packages(exclude=['docs', 'tests']),
    entry_points={
        'console_scripts': [
            'bijou-server=bijou.__main__:main'
        ]
    }
)
