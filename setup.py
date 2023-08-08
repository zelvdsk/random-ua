from setuptools import setup

setup(
    author='Errucha', 
    name='random-ua', 
    version='0.1',
    entry_points={"console_scripts": ["scraping=random_ua:ugent"]}, 
    packages=['random_ua'],
    install_requires=[
        'requests', 
        'bs4'
    ],
)
