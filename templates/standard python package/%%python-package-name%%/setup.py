from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='%%python-package-name%%',
      version='0.1',
      description='',
      long_description=readme(),
      classifiers=[
          'Development Status :: 4 - Beta',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
          'Topic :: Utilities',
      ],
      keywords='%%package_keywords%%',
      # url='https://github.com/thespacedoctor/%%python-package-name%%',
      author='%%authorName%%',
      author_email='%%authorEmail%%',
      license='MIT',
      packages=['%%python-package-name%%'],
      install_requires=[
          'pyyaml',
      ],
      test_suite='nose.collector',
      tests_require=['nose', 'nose-cover3'],
      # entry_points={
      #     'console_scripts': ['%%python-package-name%%=%%python-package-name%%.cl_utils:main'],
      # },
      zip_safe=False)
