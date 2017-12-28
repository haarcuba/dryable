from setuptools import setup, find_packages

README = 'provide --dry-run functionality for your application'

requires = []
tests_require = [ 'pytest', ]

setup(name='dryable',
      version='0.2.1',
      description=README,
      long_description=README,
      url='https://github.com/haarcuba/dryable',
      classifiers=[
          "Programming Language :: Python",
      ],
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
      )
