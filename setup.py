from setuptools import setup
from setuptools import find_packages


setup(name='KaggleUtils',
      version='0.0.1',
      description='Utils for my kaggle projects',
      author='Abhijeet Mulgund',
      author_email='abhmul@gmail.com',
      url='https://github.com/abhmul/KaggleUtils',
      license='MIT',
      install_requires=['numpy>=1.12.0'],
      classifiers=[
          'Development Status :: 1 - Pre-Alpha',
          'Intended Audience :: Developers',
          'Intended Audience :: Education',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules'
      ],
      packages=find_packages())
