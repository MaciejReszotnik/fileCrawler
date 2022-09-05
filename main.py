import glob
import os

defaultFilesPath = "./*.*"
my_string="hello python world , i'm a beginner"
print(my_string.split("hello python world , ",1)[1])
searchedString1 = input("Please, provide string to search in the files! ")

targetFolder = input("Please provide target folder. If none is provided THIS folder will be analyzed.     ")
filesPath = ""
filePattern = input("Please, provide file pattern. If none is provided the following pattern will be used: *.*     ")

if (targetFolder == ""):
    filesPath = defaultFilesPath
else:
    filesPath = targetFolder + "/" + filePattern

completeFileList = glob.glob(filesPath)
print(completeFileList)

while(len(completeFileList) > 0):
    completeFileList = glob.glob(filesPath)
    filePath = completeFileList[0]
    allFilesExceptFirstFile = completeFileList.copy()
    allFilesExceptFirstFile.remove(filePath)
    id = ""
    with open(filePath, "r") as fi:
        for ln in fi:
            if ln.startswith(searchedString1):
                print("Whole searched line: " + ln)
                id = my_string.split(searchedString1 ,1)[1]
                break
    for fileFi in allFilesExceptFirstFile:
        with open(fileFi, "r") as fi:
            for ln in fi:
                if ln.find(id):
                    print("Whole searched line: " + ln)
                    id = my_string.split(searchedString1 ,1)[1]
                    break

    os.mkdir(targetFolder + "/" + id)

def getStringLineBySubString(filePath, searchedString):
    with open(filePath, "r") as fi:
        for ln in fi:
            if ln.startswith(searchedString):
                print("Whole searched line: " + ln)
                return ln
        return ""

def getKeyValueBySubString(filePath, searchedString, delimiter):
    with open(filePath, "r") as fi:
        for ln in fi:
            if ln.startswith(searchedString):
                thisDict = getKeyValueFromLine(ln, delimiter)
                print("Whole searched line: " + ln)
                return thisDict
        return ""

def getKeyValueFromLine(line, delimiter):
    return {
        line.split(delimiter, 1)[0]: line.split(delimiter, 1)[1]
    }

def isLineInFile(filePath, lineString):
    with open(filePath, "r") as fi:
        for ln in fi:
            if ln.find(lineString):
                print("Whole searched line: " + ln)
                return True
        return False

def moveFileToTargetDirectory(srcFolderPath, srcFileName, targetFolderPath):
    if (not os.path.isdir(targetFolderPath)):
        os.mkdir(targetFolderPath)
    
    os.rename(srcFolderPath + "/" + srcFileName, targetFolderPath + "/" + srcFileName)

    


"""

1. Get searched string1
2. Start loop 1
    2a. Get all files in the folder (subfolders)?
    2b. Read first file and find a line that contains string1
    2c. Memorize the whole line as line1
    2d. Declare isMatchFound = false
    2d. Start loop 2
        2da. Read first file after the previous file and find a line that contains line1
        2db. If match found mark isMatchFound as true
        2db. Create a separate folder called after the latter part of line1.
        2dc. Crop the file into designated folder
    2e. If other matches were found move file to designated folder / If not move to folder called "singles"



"""