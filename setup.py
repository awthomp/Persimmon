from setuptools import setup, find_packages


setup(name='whitewater',
      description='A visual dataflow language for sklearn',
      author='Álvaro Bermejo',
      author_email='alvaro.garcia95@hotmail.com',
      version='0.9.1',
      url='http://github.com/AlvarBer/Whitewater',
      download_url='https://github.com/AlvarBer/Whitewater/archive/v0.9.1.tar.gz',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      python_requires='>=3.5',
      setup_requires=['Cython'],
      install_requires=['Cython', 'Kivy', 'scikit-learn', 'pandas', 'fuzzywuzzy', 'pymitter'],
      zip_safe=False,
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6'])
