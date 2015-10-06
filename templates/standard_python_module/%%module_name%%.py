#!/usr/local/bin/python
# encoding: utf-8
"""
%%module_name%%.py
==================
:Summary:
    %%moduleSummary%%

:Author:
    %%authorName%%

:Date Created:
    %%now-date%%

:dryx syntax:
    - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
    - If you have any questions requiring this script/module please email me: %%authorEmail%%

:Tasks:
    @review: when complete pull all general functions and classes into dryxPython
"""
################# GLOBAL IMPORTS ####################
import sys
import os
os.environ['TERM'] = 'vt100'
from dryxPython import logs as dl
from dryxPython import commonutils as dcu
from dryxPython.projectsetup import setup_main_clutil

class %%module_name%%():
    """
    The worker class for the %%module_name%% module

    **Key Arguments:**
        - ``log`` -- logger
        - ``settings`` -- the settings dictionary
        
    **Todo**
        - @review: when complete, clean %%module_name%% class
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract class to another module
    """
    ## Initialisation
    # 1. @flagged: what are the unique attrributes for each object? Add them to __init__
    def __init__(
            self,
            log, 
            settings=False, 
            
        ):
        self.log = log
        log.debug("instansiating a new '%%module_name%%' object")
        self.settings = settings
        # xt-self-arg-tmpx

        # 2. @flagged: what are the default attrributes each object could have? Add them to variable attribute set here
        ## Variable Data Atrributes

        # 3. @flagged: what variable attrributes need overriden in any baseclass(es) used
        ## Override Variable Data Atrributes

        ## Initial Actions

        return None
    
    # 4. @flagged: what actions does each object have to be able to perform? Add them here
    ## Method Attributes
    def get(self):
        """get the %%module_name%% object
    
        **Return:**
            - ``%%module_name%%``
    
        **Todo**
            - @review: when complete, clean get method
            - @review: when complete add logging
        """
        self.log.info('starting the ``get`` method')
        
        %%module_name%% = None
    
        self.log.info('completed the ``get`` method')
        return %%module_name%%
    
    # xt-class-method


    # 5. @flagged: what actions of the base class(es) need ammending? ammend them here
    ## Override Method Attributes
    # method-override-tmpx

