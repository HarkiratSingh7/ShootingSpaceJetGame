from setuptools import setup, find_packages

setup(
    name='ShootingSpaceJetGame',
    version='1.0',
    packages=find_packages(include=['shootingspacejetgame', 'shootingspacejetgame.*']),
    license='MIT',
    author='Harkirat Singh (honey.harkirat@outlook.com)',
    install_requires=["pygame"],
    long_description=open('Readme.md').read(),
)
