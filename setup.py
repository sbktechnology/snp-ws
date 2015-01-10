from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='snp_ws',
    version=version,
    description='App for managing Spectrum Fruits Website',
    author='Systematrix',
    author_email='info@systematrix.co.in',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
