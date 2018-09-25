from setuptools import setup, find_packages
import os

current_dir = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(current_dir, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
     name = 'find_my_favorite_cat',
     version = '0.1',
     description = 'Find cat information that matches the input from user.'
     long_description = long_description,
     long_description_content_type = 'text/x-rst',
     classifiers = [
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        ],
     keywords = 'find cat',
     url = 'https://github.com/hong-chen/find-my-favorite-cat',
     author = 'Hong Chen, Yixing Shao',
     author_email = 'me@hongchen.cz, yixingshao@foxmail.com',
     license = 'MIT',
     packages = ['find_my_favorite_cat'],
     # install_requires = ['nose', 'numpy', 'scipy', 'h5py', 'netcdf4', 'python-hdf4'],
     python_requires = '~=3.6',
     # scripts = ['bin/lss'],
     include_package_data = True,
     zip_safe = False
     )
