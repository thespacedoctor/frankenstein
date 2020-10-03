import os
import nose
import shutil
import yaml
from frankenstein import electric
from frankenstein.utKit import utKit

# load settings
stream = file("/Users/Dave/git_repos/frankenstein/default_settings.yaml", 'r')
settings = yaml.load(stream)
stream.close()


# SETUP AND TEARDOWN FIXTURE FUNCTIONS FOR THE ENTIRE MODULE
moduleDirectory = os.path.dirname(__file__)
utKit = utKit(moduleDirectory)
log, dbConn, pathToInputDir, pathToOutputDir = utKit.setupModule()
utKit.tearDownModule()

pathToTemplate = pathToInputDir + "/test_template"
# xnose-class-to-test-main-command-line-function-of-module


class test_electric(unittest.TestCase):

    def test_electric_function(self):
        kwargs = {}
        kwargs["log"] = log
        kwargs["settings"] = settings
        kwargs["pathToTemplate"] = pathToTemplate
        # xt-kwarg_key_and_value
        testObject = electric(**kwargs)
        testObject.get()

    def test_electric_list_function(self):
        kwargs = {}
        kwargs["log"] = log
        kwargs["settings"] = settings
        kwargs["pathToTemplate"] = pathToTemplate
        # xt-kwarg_key_and_value
        testObject = electric(**kwargs)
        testObject.list()

        # x-print-testpage-for-pessto-marshall-web-object

    # x-class-to-test-named-worker-function
