from setuptools import setup, find_packages

setup(name='czo-tools',
      version='0.0.1',
      description='Process data from HOBO pressure loggers',
      url='https://github.com/tohodson/hobo',
      download_url =
      'https://github.com/tohodson/hobo/archive/0.0.1.tar.gz',
      author='Tim Hodson',
      author_email='tohodson.gmail.com',
      license='GPL',
      packages=['hobo'],
      install_requires=[
                    'pandas',
                ],
      python_requires='>=3',
      scripts=['bin/process-hobo'],
      zip_safe=False)
