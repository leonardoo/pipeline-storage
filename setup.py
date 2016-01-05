import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-pipeline-storage',
    version='0.0.1',
    packages=['pipeline_storage'],
    include_package_data=True,
    license='MIT License',
    description='A simple Storage finder for files when django-pipeline is develop mode.',
    long_description=README,
    author='Leonardo orozco',
    author_email='leonardoorozcop@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Storage',
    ],
)
