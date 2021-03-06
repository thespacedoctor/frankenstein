# Installation

The easiest way to install frankenstein is to use `pip` (here we show the install inside of a conda environment):

``` bash
conda create -n frankenstein python=3.7 pip
conda activate frankenstein
pip install frankenstein
```

Or you can clone the [github repo](https://github.com/thespacedoctor/frankenstein) and install from a local version of the code:

``` bash
git clone git@github.com:thespacedoctor/frankenstein.git
cd frankenstein
python setup.py install
```

To upgrade to the latest version of frankenstein use the command:

``` bash
pip install frankenstein --upgrade
```

To check installation was successful run `frankenstein -v`. This should return the version number of the install.

## Development

If you want to tinker with the code, then install in development mode. This means you can modify the code from your cloned repo:

``` bash
git clone git@github.com:thespacedoctor/frankenstein.git
cd frankenstein
python setup.py develop
```

[Pull requests](https://github.com/thespacedoctor/frankenstein/pulls) are welcomed! 

<!-- ### Sublime Snippets

If you use [Sublime Text](https://www.sublimetext.com/) as your code editor, and you're planning to develop your own python code with soxspipe, you might find [my Sublime Snippets](https://github.com/thespacedoctor/frankenstein-Sublime-Snippets) useful. -->


