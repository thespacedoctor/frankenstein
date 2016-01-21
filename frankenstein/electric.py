# !/usr/local/bin/python
# encoding: utf-8
"""
electric.py
===========
:Summary:
    The code for the frankenstein package

:Author:
    David Young

:Date Created:
    May 21, 2015

:dryx syntax:
    - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
    - If you have any questions requiring this script/module please email me: d.r.young@qub.ac.uk
"""
################# GLOBAL IMPORTS ####################
import sys
import os
os.environ['TERM'] = 'vt100'
import readline
import glob
import pickle
import shutil
import codecs
import re
from subprocess import Popen, PIPE, STDOUT
from docopt import docopt
from dryxPython import logs as dl
from dryxPython import commonutils as dcu
from dryxPython.projectsetup import setup_main_clutil


class electric():

    """
    The worker class for the electric module

    **Key Arguments:**
        - ``log`` -- logger
        - ``settings`` -- the settings dictionary
        - ``pathToTemplate`` -- path to the template folder/file
        - ``pathToDestination`` -- path to where template should be cloned
        - ``ignoreExisting`` - - ignore existing files in the destination for the template
    """
    # Initialisation

    def __init__(
            self,
            log,
            pathToTemplate,
            pathToDestination,
            settings=False,
            ignoreExisting=False
    ):
        self.log = log
        log.debug("instansiating a new 'electric' object")
        self.settings = settings
        self.pathToTemplate = pathToTemplate
        self.pathToDestination = pathToDestination
        self.ignoreExisting = ignoreExisting
        # xt-self-arg-tmpx

        return None

    # Method Attributes
    def get(self):
        """do the frankenstein magic!
        """
        self.log.info('starting the ``get`` method')

        self._copy_folder_and_get_directory_listings()
        self._join_all_filenames_and_text()
        self._collect_placeholders_required()
        self._populate_dynamic_placeholders()
        self._fill_placeholders_from_settings()
        self._request_remaining_placeholders()
        self._populate_placeholders_in_files()
        self._move_template_to_destination(ignoreExisting=self.ignoreExisting)

        self.log.info('completed the ``get`` method')
        return None

    def _copy_folder_and_get_directory_listings(
            self):
        """ copy template folder to /tmp and get directory listings
        """
        self.log.info(
            'starting the ``_copy_folder_and_get_directory_listings`` method')

        # COPY TEMPLATE STRUCTURE TO /tmp/
        basename = os.path.basename(self.pathToTemplate)
        tmpPath = "/tmp/%(basename)s" % locals()
        try:
            shutil.rmtree(tmpPath)
        except:
            pass
        shutil.copytree(self.pathToTemplate, tmpPath)

        directoryContents = dcu.get_recursive_list_of_directory_contents(
            log=self.log,
            baseFolderPath=tmpPath,
            whatToList='all'  # [ 'files' | 'dirs' | 'all' ]
        )

        self.directoryContents = directoryContents
        self.tmpPath = tmpPath

        self.log.info(
            'completed the ``_copy_folder_and_get_directory_listings`` method')
        return None

    def _collect_placeholders_required(
            self):
        """ collect placeholders required from filename etc
        """
        self.log.info('starting the ``_collect_placeholders_required`` method')

        phs = self.settings["frankenstein"]["placeholder delimiters"]
        phsString = "|".join(phs)

        matchObject = re.finditer(
            r'(%(phsString)s)(.*?)\1' % locals(),
            string=self.contentString,
            flags=re.S  # re.S
        )

        phDict = {}
        for match in matchObject:
            phDict[match.group(2)] = None

        self.phDict = phDict

        self.log.info(
            'completed the ``_collect_placeholders_required`` method')
        return None

    def _join_all_filenames_and_text(
            self):
        """ join all file names, driectory names and text content together
        """
        self.log.info('starting the ``_join_all_filenames_and_text`` method')

        contentString = u""
        for i in self.directoryContents:
            contentString += u"%(i)s\n" % locals()
            if os.path.isfile(os.path.join(i)):
                if i[-4:] in [".png", ".jpg", ".gif"]:
                    continue
                readFile = codecs.open(i, encoding='utf-8', mode='r')
                if ".DS_Store" in i:
                    continue
                data = readFile.read()
                contentString += u"%(data)s\n" % locals()
                readFile.close()

        self.contentString = contentString

        self.log.info('completed the ``_join_all_filenames_and_text`` method')
        return None

    def _populate_dynamic_placeholders(
            self):
        """ populate dynamic placeholders - times etc
        """
        self.log.info('starting the ``_populate_dynamic_placeholders`` method')

        from datetime import datetime, date, time
        now = datetime.now()

        dynamicPhs = {
            "now-ymd": now.strftime("%Y%m%d"),
            "now-ymdhms": now.strftime("%Y%m%dt%H%M%S"),
            "now-date": now.strftime("%B %e, %Y"),
            "now-datetime": now.strftime("%B %e, %Y %I:%M ") + now.strftime("%p").lower(),
            "now-time": now.strftime("%I:%M ") + now.strftime("%p").lower(),
            "now-hms": now.strftime("%H%M%S"),
        }

        for k, v in self.phDict.iteritems():
            if k in dynamicPhs.keys():
                self.phDict[k] = dynamicPhs[k]

        self.log.info(
            'completed the ``_populate_dynamic_placeholders`` method')
        return None

    def _fill_placeholders_from_settings(
            self):
        """ fill placeholders from the placeholders in the settings file
        """
        self.log.info(
            'starting the ``_fill_placeholders_from_settings`` method')

        for k, v in self.phDict.iteritems():
            if k in self.settings["frankenstein"]["fixed placeholders"].keys():
                self.phDict[k] = self.settings[
                    "frankenstein"]["fixed placeholders"][k]

        self.log.info(
            'completed the ``_fill_placeholders_from_settings`` method')
        return None

    def _request_remaining_placeholders(
            self):
        """ request remaining placeholders needing populated from the user
        """
        self.log.info(
            'starting the ``_request_remaining_placeholders`` method')

        phNeeded = False
        for k, v in self.phDict.iteritems():
            if not v:
                phNeeded = True

        if phNeeded == False:
            return

        print "please add your placeholder values ..."

        for k, v in self.phDict.iteritems():
            if not v:
                v = raw_input("%(k)s? \n  >  " % locals())
                self.phDict[k] = v

        self.log.info(
            'completed the ``_request_remaining_placeholders`` method')
        return None

    def _populate_placeholders_in_files(
            self):
        """ populate placeholders in file names, folder names and content
        """
        self.log.info(
            'starting the ``_populate_placeholders_in_files`` method')

        rev = reversed(self.directoryContents)
        phs = self.settings["frankenstein"]["placeholder delimiters"]

        # FILE CONTENT FIRST
        for i in self.directoryContents:
            if os.path.isfile(i):
                pathToReadFile = i
                if ".DS_Store" in i:
                    os.remove(i)
                    continue
                try:
                    self.log.debug(
                        "attempting to open the file %s" % (pathToReadFile,))
                    if i[-4:] in [".png", ".jpg", ".gif"]:
                        continue
                    readFile = codecs.open(
                        pathToReadFile, encoding='utf-8', mode='r')
                    thisData = readFile.read()
                    readFile.close()
                except IOError, e:
                    message = 'could not open the file %s' % (pathToReadFile,)
                    self.log.critical(message)
                    raise IOError(message)

                newContent = thisData
                for k, v in self.phDict.iteritems():
                    for ph in phs:
                        fullPH = ph + k + ph
                        if fullPH in thisData:
                            newContent = newContent.replace(fullPH, v)

                if newContent != thisData:
                    writeFile = codecs.open(
                        pathToReadFile, encoding='utf-8', mode='w')
                    writeFile.write(newContent)
                    writeFile.close()

        # NOW FILE NAMES
        for i in self.directoryContents:
            if os.path.isfile(i):
                newPath = i
                newFile = i.split("/")[-1]
                for k, v in self.phDict.iteritems():
                    for ph in phs:
                        fullPH = ph + k + ph
                        if fullPH in newFile:
                            newFile = newFile.replace(fullPH, v)
                            newPath = "/".join(i.split("/")
                                               [:-1]) + "/" + newFile
                if newPath != i:
                    try:
                        self.log.debug("attempting to rename file %s to %s" %
                                       (i, newPath))
                        shutil.move(i, newPath)
                    except Exception, e:
                        self.log.error(
                            "could not rename file %s to %s - failed with this error: %s " % (i, newPath, str(e),))
                        sys.exit(0)

        # NOW DRIECTORY NAMES
        theseDirs = []
        for i in reversed(self.directoryContents):
            if os.path.isdir(i):
                theseDirs.append(i)
        for i in theseDirs:
            newPath = i
            newFolder = i.split("/")[-1]
            for k, v in self.phDict.iteritems():
                for ph in phs:
                    fullPH = ph + k + ph
                    if fullPH in newFolder:
                        newFolder = newFolder.replace(fullPH, v)
                        newPath = "/".join(i.split("/")[:-1]) + "/" + newFolder
            if newPath != i:
                try:
                    self.log.debug("attempting to rename file %s to %s" %
                                   (i, newPath))
                    shutil.move(i, newPath)
                except Exception, e:
                    self.log.error(
                        "could not rename file %s to %s - failed with this error: %s " % (i, newPath, str(e),))
                    sys.exit(0)

        self.log.info(
            'completed the ``_populate_placeholders_in_files`` method')
        return None

    # use the tab-trigger below for new method
    def _move_template_to_destination(
            self,
            ignoreExisting=False):
        """ move template to destination

        **Key Arguments:**
            # -

        **Return:**
            - None

        **Todo**
            - @review: when complete, clean _move_template_to_destination method
            - @review: when complete add logging
        """
        self.log.info('starting the ``_move_template_to_destination`` method')

        # CREATE DIRECTORY STRUCTURE
        sourceDirectories = dcu.get_recursive_list_of_directory_contents(
            log=self.log,
            baseFolderPath=self.tmpPath,
            whatToList='dirs'  # [ 'files' | 'dirs' | 'all' ]
        )
        destinationDirectories = []
        destinationDirectories = []
        destinationDirectories[:] = [self.pathToDestination +
                                     d.replace(self.tmpPath, "") for d in sourceDirectories]
        for d in destinationDirectories:
            # Recursively create missing directories
            if not os.path.exists(d):
                os.makedirs(d)

        # CREATE NEW FILES
        sourceFiles = dcu.get_recursive_list_of_directory_contents(
            log=self.log,
            baseFolderPath=self.tmpPath,
            whatToList='files'  # [ 'files' | 'dirs' | 'all' ]
        )
        destinationFiles = []
        destinationFiles = []
        destinationFiles[:] = [self.pathToDestination +
                               d.replace(self.tmpPath, "") for d in sourceFiles]

        appendText = ""
        for s, f in zip(sourceFiles, destinationFiles):
            try:
                readFile = codecs.open(f, encoding='utf-8', mode='r')
                content = readFile.read()
                readFile.close()
                fileExists = True
            except IOError:
                fileExists = False
            if fileExists == True and len(content) > 1 and ignoreExisting == False:
                readFile = codecs.open(s, encoding='utf-8', mode='r')
                content = readFile.read()
                readFile.close()
                appendText += """
## `%(f)s`

```
%(content)s 
```

""" % locals()
            else:
                try:
                    if ignoreExisting == False or (ignoreExisting == True and fileExists == False):
                        self.log.debug("attempting to rename file %s to %s" %
                                       (s, f))
                        shutil.move(s, f)
                    else:
                        pass
                except Exception, e:
                    self.log.error("could not rename file %s to %s - failed with this error: %s " %
                                   (s, f, str(e),))
                    sys.exit(0)

        # CREATE NOTE TO USER TO APPEND TEXT
        if len(appendText) > 3:
            appendText = """
# Text to Append to Pre-Existing Files

%(appendText)s
""" % locals()
            writeFile = codecs.open(
                "/tmp/append.md", encoding='utf-8', mode='w')
            writeFile.write(appendText)
            writeFile.close()
            try:
                cmd = """open -a "Marked 2" /tmp/append.md""" % locals()
                p = Popen(cmd, stdout=PIPE, stdin=PIPE, shell=True)
                output = p.communicate()[0]
                self.log.debug('output: %(output)s' % locals())
            except:
                pass

        # REMOVE THE TMP FOLDER
        shutil.rmtree(self.tmpPath)

        self.log.info('completed the ``_move_template_to_destination`` method')
        return None

    # use the tab-trigger below for new method
    # xt-class-method
