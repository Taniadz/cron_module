from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))


with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='cron_module',
      version='0.1',
      description='cron module for python',
      long_description=long_description,
      url='https://github.com/Taniadz/cron_module',
      author='Tania',
      author_email='taniarabota@gmail.com',
      license='MIT',
      classifiers=[
              # How mature is this project? Common values are
              #   3 - Alpha
              #   4 - Beta
              #   5 - Production/Stable
              'Development Status :: 3 - Alpha',

              # Indicate who your project is intended for
              'Intended Audience :: Developers',
              'Topic :: Software Development :: Build Tools',

              # Pick your license as you wish (should match "license" above)
              'License :: OSI Approved :: MIT License',

              # Specify the Python versions you support here. In particular, ensure
              # that you indicate whether you support Python 2, Python 3 or both.
              'Programming Language :: Python :: 3',
              'Programming Language :: Python :: 3.3',
              'Programming Language :: Python :: 3.4',
              'Programming Language :: Python :: 3.5',
          ],
      keywords='cron module development',
      packages=find_packages(exclude=['cron_module']),
      )