from setuptools import setup

setup(
    author='Errucha', 
    name='random-ua',
    descriptions='Alat untuk mengambil useragent secara random dari website', 
    version='0.1',
    entry_points={"console_scripts": ["random-ua:random-ua.main:scraping"]}, 
    py_modules=['random-ua'],
    install_requires=[
        'requests', 
        'bs4'
    ],
)

