from setuptools import setup, find_packages

README = 'provide --dry-run functionality for your application'

requires = []
tests_require = [ 'pytest', ]

setup(name='dryable',
      version='1.2.0',
      description=README,
      long_description=README,
      url='https://github.com/haarcuba/dryable',
      author='Yoav Kleinberger',
      author_email='haarcuba@gmail.com',
      keywords='subprocess',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      extras_require={
          'testing': tests_require,
      },
      install_requires=requires,
      entry_points={},
      classifiers = [
            "Programming Language :: Python :: 3",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
         ]
      )
