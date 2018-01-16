""" Setup for calitateaer.ro data science project"""
from setuptools import setup, find_packages

test_requirements = ['pytest']

setup(
    name="calitateaer.ro data science project",
    version="0.0.1",
    packages=['app'],
    include_package_data=True,
    author="Andrei Pruteanu (andrei.pruteanu@gmail.com), "
           "",
    license="Open-Source",
    install_requires=[
        'requests',
        'pandas',
        'logging'
    ],
)
