from setuptools import setup, find_packages

setup(
    name='MyPackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    licence='MIT',
    description='EDSA example python package',
    long_description=open('readme.md').read(),
    install_requires=['numpy'],
    url='https://github.com/<username>/<package-name>',
    author='Landré Venter',
    author_email='lanven@vodamail.co.za'
)