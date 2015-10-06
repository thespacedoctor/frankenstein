import os
import nose
import shutil
import yaml
from %%pythonPackageName%% import %%module_name%%
from %%pythonPackageName%%.utKit import utKit

# load settings
cl_utils.main()
stream = file(
    "/Users/Dave/.config/%%pythonPackageName%%/%%pythonPackageName%%.yaml", 'r')
settings = yaml.load(stream)
stream.close()

# SETUP AND TEARDOWN FIXTURE FUNCTIONS FOR THE ENTIRE MODULE
moduleDirectory = os.path.dirname(__file__)
utKit = utKit(moduleDirectory)
log, dbConn, pathToInputDir, pathToOutputDir = utKit.setupModule()
utKit.tearDownModule()

class test_%%module_name%%():

    def test_%%module_name%%_function(self):
        kwargs = {}
        kwargs["log"] = log
        kwargs["settings"] = settings
        # xt-kwarg_key_and_value
        
        testObject = %%module_name%%(**kwargs)
        testObject.get()

        # x-print-testpage-for-pessto-marshall-web-object

    # x-class-to-test-named-worker-function
