from distutils.core import setup
from setuptools import find_packages

setup(name = 'my_hhh',     # 包名
      version = '1.0',  # 版本号
      description = '',
      long_description = '',
      author = '',
      author_email = '',
      url = '',
      license = '',
      
      classifiers = [
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Natural Language :: Chinese (Simplified)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Utilities'
      ],
      keywords = '',
      packages = find_packages('src'),  # 必填
      package_dir = {'':'src'},         # 必填
      include_package_data = True,
      install_requires=[],
)
