"""
standard file
create installable package
run a setup function
"""
from setuptools import find_packages, setup
with open('README.md','r') as f:
    long_description = f.read()

setup(
    name = 'pgbackup',
    version = '0.1.0',
    author = 'Allen Zhang',
    author_email = 'zzhan785@uwo.ca',
    description = 'A utility for backing up PostgreSQl databases',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/capitalallen/pgbackup',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=['boto3'],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'pgbackup=pgbackup.cli:main',
        ],
    }
)