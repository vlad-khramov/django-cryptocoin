import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-cryptocoin',
    version='0.1',
    packages=[
        'django_cryptocoin',
        'django_cryptocoin.bitcoinrpc',
        'django_cryptocoin.management',
        'django_cryptocoin.management.commands',
        'django_cryptocoin.migrations',
    ],
    include_package_data=True,
    license='BSD (3-Clause) License',
    description='A Django app to organize accepting bitcoin, litecoin, novacoin and other cryptocoins.',
    long_description=README,
    url='https://github.com/quantum13/django-cryptocoin',
    requires=["South (>0.7.4)"],
    author='Vladimir Khramov',
    author_email='hr.vlad@gmail.com',
)