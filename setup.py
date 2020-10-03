from setuptools import setup, find_packages
import os

moduleDirectory = os.path.dirname(os.path.realpath(__file__))
exec(open(moduleDirectory + "/frankenstein/__version__.py").read())

def readme():
    with open(moduleDirectory + '/README.md') as f:
        return f.read()

install_requires = [
    'pyyaml',
    'frankenstein',
    'fundamentals'
]

# READ THE DOCS SERVERS
exists = os.path.exists("/home/docs/")
if exists:
    c_exclude_list = ['healpy', 'astropy',
                      'numpy', 'sherlock', 'wcsaxes', 'HMpTy', 'ligo-gracedb']
    for e in c_exclude_list:
        try:
            install_requires.remove(e)
        except:
            pass

setup(name="frankenstein",
      version=__version__,
      description="Project Templates Brought to Life",
      long_description=readme(),
      long_description_content_type='text/markdown',
      classifiers=[
          'Development Status :: 4 - Beta',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 2.7',
          'Topic :: Utilities',
      ],
      keywords=['templates'],
      url='https://github.com/thespacedoctor/frankenstein',
      download_url='https://github.com/thespacedoctor/frankenstein/archive/v%(__version__)s.zip' % locals(
      ),
      author='David Young',
      author_email='davidrobertyoung@gmail.com',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      install_requires=install_requires,
      test_suite='nose2.collector.collector',
      tests_require=['nose2', 'cov-core'],
      entry_points={
          'console_scripts': ['frankenstein=frankenstein.cl_utils:main'],
      },
      zip_safe=False)
