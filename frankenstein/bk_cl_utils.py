#!/usr/local/bin/python
# encoding: utf-8
"""
*CL utils for frankenstein*

:Author:
    David Young

:Date Created:
    October 1, 2015

Usage:
    frankenstein <pathToTemplate> <pathToDestination> [-s <pathToSettingsFile>]
    frankenstein -l <pathToTemplate> [-s <pathToSettingsFile>]

Options:
    -l, --list            list the remaining placeholders required by the template after dynamic and settings file placeholders
    -h, --help            show this help message
    -s, --settings        the settings file
"""
################# GLOBAL IMPORTS ####################
import sys
import os
os.environ['TERM'] = 'vt100'
import readline
import glob
import pickle
from docopt import docopt
from fundamentals import tools, times
from frankenstein import electric
# from ..__init__ import *


def main(arguments=None):
    """
    *The main function used when ``cl_utils.py`` is run as a single script from the cl, or when installed as a cl command*
    """
    # setup the command-line util settings
    su = tools(
        arguments=arguments,
        docString=__doc__,
        logLevel="DEBUG",
        options_first=False,
        projectName="frankenstein"
    )
    arguments, settings, log, dbConn = su.setup()

    # unpack remaining cl arguments using `exec` to setup the variable names
    # automatically
    for arg, val in arguments.iteritems():
        if arg[0] == "-":
            varname = arg.replace("-", "") + "Flag"
        else:
            varname = arg.replace("<", "").replace(">", "")
        if isinstance(val, str) or isinstance(val, unicode):
            exec(varname + " = '%s'" % (val,))
        else:
            exec(varname + " = %s" % (val,))
        if arg == "--dbConn":
            dbConn = val
        log.debug('%s = %s' % (varname, val,))

    ## START LOGGING ##
    startTime = times.get_now_sql_datetime()
    log.info(
        '--- STARTING TO RUN THE cl_utils.py AT %s' %
        (startTime,))

    # call the worker function
    # x-if-settings-or-database-credientials
    if not listFlag:
        electric.electric(
            log=log,
            pathToTemplate=pathToTemplate,
            pathToDestination=pathToDestination,
            settings=settings
        ).get()
    if listFlag:
        placeHolders = electric.electric(
            log=log,
            pathToTemplate=pathToTemplate,
            pathToDestination=pathToDestination,
            settings=settings
        ).list_placeholders()
        placeHolders = ("\n").join(placeHolders)
        print placeHolders

    if "dbConn" in locals() and dbConn:
        dbConn.commit()
        dbConn.close()
    ## FINISH LOGGING ##
    endTime = times.get_now_sql_datetime()
    runningTime = times.calculate_time_difference(startTime, endTime)
    log.info('-- FINISHED ATTEMPT TO RUN THE cl_utils.py AT %s (RUNTIME: %s) --' %
             (endTime, runningTime, ))

    return


###################################################################
# CLASSES                                                         #
###################################################################
# xt-class-module-worker-tmpx
# xt-class-tmpx


###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
# xt-worker-def

# use the tab-trigger below for new function
# xt-def-with-logger

###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################

if __name__ == '__main__':
    main()
