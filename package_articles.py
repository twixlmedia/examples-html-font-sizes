#!/usr/bin/env python

import os
import sys
import zipfile

def main():

    if len(sys.argv) < 2:
        print 'Usage:', os.path.basename(sys.argv[0]), '<root folder>'
        sys.exit(1)

    root = sys.argv[1]
    if not os.path.exists(root):
        print 'Path not found:', root
        sys.exit(1)
    root = os.path.realpath(root)

    for folderName in os.listdir(root):

        if folderName == '__SharedResources':
            continue

        folderBasePath = os.path.join(root, folderName)
        if os.path.isfile(folderBasePath):
            continue

        articlePath = folderBasePath + '.article'
        print '    Creating:', articlePath

        if os.path.exists(articlePath):
            os.remove(articlePath)

        articleFile = zipfile.ZipFile(articlePath, 'w')

        # Add the shared resources

        addSharedResources(root, articleFile)

        for articleRoot, dirs, files in os.walk(folderBasePath):
            for file in files:
                if file[0] == '.':
                    continue
                fullPath = os.path.join(articleRoot, file)
                relPath  = os.path.relpath(fullPath, folderBasePath)
                articleFile.write(fullPath, relPath, zipfile.ZIP_DEFLATED)

        articleFile.close()

def addSharedResources(root, articleFile):

    resourcesPath = os.path.join(root, '__SharedResources')
    if not os.path.exists(resourcesPath):
        return

    for resourceRoot, dirs, files in os.walk(resourcesPath):
        for file in files:
            if file[0] == '.':
                continue
            fullPath = os.path.join(resourceRoot, file)
            relPath  = os.path.relpath(fullPath, resourcesPath)
            articleFile.write(fullPath, relPath, zipfile.ZIP_DEFLATED)

if __name__ == '__main__':
    main()
