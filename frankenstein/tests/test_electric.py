from __future__ import print_function
from builtins import str
import os
import unittest
import shutil
import yaml
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

pathToTemplate = pathToInputDir + "/test_template"
pathToDestination = pathToOutputDir


class test_electric(unittest.TestCase):

    def test_electric_function(self):
        from frankenstein import electric
        kwargs = {}
        kwargs["log"] = log
        kwargs["settings"] = settings
        kwargs["pathToTemplate"] = pathToTemplate
        kwargs["pathToDestination"] = pathToDestination
        # xt-kwarg_key_and_value
        testObject = electric(**kwargs)
        testObject.get()

    def test_electric_list_function(self):
        from frankenstein import electric
        kwargs = {}
        kwargs["log"] = log
        kwargs["settings"] = settings
        kwargs["pathToTemplate"] = pathToTemplate
        kwargs["pathToDestination"] = pathToDestination
        # xt-kwarg_key_and_value
        testObject = electric(**kwargs)
        testObject.list_placeholders()

        # x-print-testpage-for-pessto-marshall-web-object

    # x-class-to-test-named-worker-function
