from setuptools import setup, find_packages

setup(name='obsio',
      version='0.3',
      packages=find_packages(),
      description='Climate and weather observation IO',
      long_description=('obsio is Python package that provides a consistent generic '
                        'interface for accessing weather and climate observations '
                        'from multiple different data providers.'),    
      author='Jared W. Oyler',
      author_email='jaredwo@gmail.com',
      license='GPL',
      classifiers=['Development Status :: 2 - Pre-Alpha',
                   'Intended Audience :: Science/Research',
                   'Intended Audience :: Developers',
                   'Topic :: Scientific/Engineering',
                   'Topic :: Scientific/Engineering :: Atmospheric Science',
                   'Topic :: Scientific/Engineering :: GIS',
                   'License :: OSI Approved :: GNU General Public License',
                   'Programming Language :: Python :: 3'],    
      install_requires=['lxml', 'netCDF4', 'numpy', 'pandas', 'pycurl', 'pytz',
                        'scipy', 'shapely', 'suds-py3', 'tzwhere', 'xarray'],
      python_requires='>=3',
      package_data={'obsio.providers': ['data/*']} 
)