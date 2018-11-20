import os
from setuptools import setup, find_packages

def read(file_name):
    with open(os.path.join(os.path.dirname(__file__), file_name)) as f:
        return f.read()

setup(
    name='fatec-debug-ettore',
    version='0.0.0',
    description='Fatec CI/CD Example',
    long_description=read('../README.md'),
    url='https://github.com/ettoreleandrotognoli/fatec-debug',
    download_url='https://github.com/ettoreleandrotognoli/fatec-debug',
    license='BSD',
    author='Éttore Leandro Tognoli',
    author_email='ettore.leandro.tognoli@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    keywords=['fatec', 'debug'],
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
    ]
)