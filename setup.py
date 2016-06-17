from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='frankenstein',
      version='0.1',
      description='',
      long_description=readme(),
      classifiers=[
          'Development Status :: 4 - Beta',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
          'Topic :: Utilities',
      ],
      keywords='utilities dryx',
      # url='https://github.com/thespacedoctor/frankenstein',
      author='thespacedoctor',
      author_email='davidrobertyoung@gmail.com',
      license='MIT',
      packages=['frankenstein'],
      include_package_data=True,
      install_requires=[
          'pyyaml'
      ],
      test_suite='nose.collector',
      tests_require=['nose', 'nose-cover3'],
      entry_points={
          'console_scripts': ['frankenstein=frankenstein.cl_utils:main'],
      },
      zip_safe=False)


# +++++++++++++++++++ NEW CONTENT ++++++++++++++++++


from setuptools import setup, find_packages
import os

moduleDirectory = os.path.dirname(os.path.realpath(__file__))
exec(open(moduleDirectory + "/frankenstein/__version__.py").read())


def readme():
    with open(moduleDirectory + '/README.rst') as f:
        return f.read()


setup(name="frankenstein",
      version=__version__,
      description="Project Templates Brought to Life",
      long_description=readme(),
      classifiers=[
          'Development Status :: 4 - Beta',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
          'Topic :: Utilities',
      ],
      keywords=['templates, tools'],
      url='https://github.com/thespacedoctor/frankenstein',
      download_url='https://github.com/thespacedoctor/frankenstein/archive/v%(__version__)s.zip' % locals(
      ),
      author='David Young',
      author_email='davidrobertyoung@gmail.com',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      install_requires=[
          'pyyaml',
          'frankenstein',
          'fundamentals'
      ],
      test_suite='nose.collector',
      tests_require=['nose', 'nose-cover3'],
      # entry_points={
      #     'console_scripts': ['frankenstein=frankenstein.cl_utils:main'],
      # },
      zip_safe=False)
