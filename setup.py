from setuptools import setup, find_packages

setup(name='hobo',
      version='0.1',
      description='Process data from HOBO pressure loggers',
      url='NA',
      author='Tim Hodson',
      author_email='tohodson.gmail.com',
      license='GPL',
      packages=['hobo'],
      install_requires=[
                    'pandas',
                ],
      scripts=['bin/process-hobo'],
      zip_safe=False)
