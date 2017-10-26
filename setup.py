from setuptools import setup, find_packages
from os import path

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='bijou',
    version='0.0.1',
    packages=find_packages(exclude=['docs', 'tests']),
    url='https://github.com/bijou/bijou-server',
    download_url='https://github.com/bijou/bijou-server/archive/0.0.1.tar.gz',
    install_requires=requirements,
    namespace_packages=['bijou'],
    entry_points={
        'console_scripts': [
            'bijou-server=bijou.__main__:main'
        ]
    }
)
