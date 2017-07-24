from setuptools import setup, find_packages

setup(name='czo-tools',
      version='0.0.1',
      description='Process data from HOBO pressure loggers',
      url='https://github.com/tohodson/czo-tools',
      download_url =
      'https://github.com/tohodson/hobo/archive/0.0.1.tar.gz',
      author='Tim Hodson',
      author_email='tohodson.gmail.com',
      license='GPL',
      packages=['hobo','discharge'],
      install_requires=[
                    'pandas',
                ],
      python_requires='>=3',
      scripts=['bin/process-hobo', 'bin/calc-discharge'],
      zip_safe=False)
