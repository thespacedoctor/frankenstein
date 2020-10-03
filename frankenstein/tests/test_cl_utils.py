from __future__ import print_function
from builtins import str
import os
import unittest
import shutil
import yaml
from docopt import docopt
from frankenstein import cl_utils
doc = cl_utils.__doc__
from frankenstein.utKit import utKit
from fundamentals import tools
from os.path import expanduser
home = expanduser("~")

packageDirectory = utKit("").get_project_root()
settingsFile = packageDirectory + "/test_settings.yaml"
# settingsFile = home + "/git_repos/_misc_/settings/frankensteinyy/test_settings.yaml"

su = tools(
    arguments={"settingsFile": settingsFile},
    docString=__doc__,
    logLevel="DEBUG",
    options_first=False,
    projectName=None,
    defaultSettingsFile=False
)
arguments, settings, log, dbConn = su.setup()

# SETUP PATHS TO COMMON DIRECTORIES FOR TEST DATA
moduleDirectory = os.path.dirname(__file__)
pathToInputDir = moduleDirectory + "/input/"
pathToOutputDir = moduleDirectory + "/output/"

try:
    shutil.rmtree(pathToOutputDir)
except:
    pass
# COPY INPUT TO OUTPUT DIR
shutil.copytree(pathToInputDir, pathToOutputDir)

# Recursively create missing directories
if not os.path.exists(pathToOutputDir):
    os.makedirs(pathToOutputDir)

class test_cl_utils(unittest.TestCase):

    def test_init(self):
        # TEST CL-OPTIONS
        command = "frankenstein init"
        args = docopt(doc, command.split(" ")[1:])
        cl_utils.main(args)
        return

    # x-class-to-test-named-worker-function
