from distutils.core import setup
from importlib_metadata import entry_points
from setuptools import find_packages

setup(
    name='ShootingSpaceJetGame',
    version='1.0',
    packages=['shootingspacejetgame'],
    include_package_data=True,
    license='MIT',
    author='Harkirat Singh (honey.harkirat@outlook.com)',
    install_requires=["pygame"],
    long_description=open('README.md').read(),
)
