import os,glob,time,math,re
from operations import euclideanNorm,dotProduct
global currentDirABSPath
currentDirABSPath=os.path.split(os.path.abspath(__file__))[0]
def getFilesList(*fileExt,sourceFolder=currentDirABSPath,currentDirABSPath=(os.path.split(os.path.abspath(__file__))[0])):
    """
    if no arguments are passed, the function considers currentDirABSPath as the source folder
    """
    sourceFolderABSPath=os.path.join(currentDirABSPath,sourceFolder);
    stringtoGetTxts_List=[]
    #print(fileExt)
    fileExt=(os.path.join(sourceFolder,"*") if len(fileExt)==0 else fileExt)
    #print("hello",fileExt)
    for i in fileExt:
        #stringtoGetTxts_List.append(os.path.join(sourceFolder,"*"+i))
        temp=getAbsFilepath(os.path.join(sourceFolder,"*"+i))
        #print("temp",glob.glob(temp))
        stringtoGetTxts_List.extend(glob.glob(temp))
    #print("stringtoGetTxts_List",stringtoGetTxts_List)
    filesList=[]
    for i in stringtoGetTxts_List:
        #print("glo",glob.glob(currentDirABSPath,i))
        filesList.append(i)
        #filesList.extend(glob.glob(i))
    return filesList
def getFilesList2(*fileExt,sourceFolderABSPath):
    """
    if no arguments are passed, the function considers currentDirABSPath as the source folder
    """
    sourceFolder=os.path.split(sourceFolderABSPath)[1]
    stringtoGetTxts_List=[]
    fileExt=(os.path.join(sourceFolder,"*") if len(fileExt)==0 else fileExt)
    for i in fileExt:
        temp=sourceFolderABSPath+os.sep+"*"+i
        stringtoGetTxts_List.extend(glob.glob(temp))
    print("stringtoGetTxts_List",stringtoGetTxts_List)
    filesList=[]
    for i in stringtoGetTxts_List:
        filesList.append(i)
    return filesList
def printDict(d):
    print("\n",d)
    for i in d:
        print(i," : ",d[i])
def getAbsFilepath(a):
    temp=str(os.path.join(currentDirABSPath,a))
    return temp
def getFilename(filepath):
    return os.path.split(filepath)[1]
def getFreqDict(filePath,caseSensitive=False,ignoreSpecialChars=True):
    #ABSFilePath=getAbsFilepath(filePath)
    ABSFilePath=filePath
    try:
        file=open(ABSFilePath,"r")
        fileContents=file.read()
        #print(fileContents)
        if not caseSensitive:
            fileContents=fileContents.lower()
        if ignoreSpecialChars:
            fileContents=re.sub(r"\W"," ",fileContents)
        words=fileContents.split()
        freqDict={}
        for i in words:
            if i not in freqDict:
                freqDict[i]=1
            else:
                freqDict[i]+=1
        return freqDict
    except UnicodeDecodeError as e:
        print("\nThe program can't handle proprietary files.Skipping",getFilename(filePath),"\n")
        return -999
    except:
        print("Input Error")
        
def getPlagiarismPercent(file1,file2):
    print("File1 : ",getFilename(file1))
    print("File2 : ",getFilename(file2))
    dict1=getFreqDict(file1)
    dict2=getFreqDict(file2)
    eN1=euclideanNorm(dict1)
    eN2=euclideanNorm(dict2)
    dProduct=dotProduct(dict1,dict2)
    theta=math.acos(dProduct/(eN1*eN2))
    theta=round(theta,2)
    #print("theta :",theta)
    MAX=math.pi
    #print("MAX : ",MAX)
    print("Plagiarism Percent : %d"%((abs(theta-MAX)/MAX)*100))
    #print(theta)
    print("Mentor's Value:",dProduct/(eN1*eN2))
if __name__=="__main__":
    currentDirABSPath=os.path.split(os.path.abspath(__file__))[0]
    print("currentDirABSPath",currentDirABSPath)
    #sourceFolder=input("Enter Folder Absolute Path")
    filesList=getFilesList("txt",sourceFolder="SourceFiles")
    print("\nFList",filesList,"\n")
    filesFreqDicts={}
    for i in filesList:
        temp=getFreqDict(i)
        if temp==-999:
            print("Skipping...",i)
        else:
            filesFreqDicts[i]=temp
    #printDict(filesFreqDicts)
    for i in filesFreqDicts:
        for j in filesFreqDicts:
            if j>i:
                getPlagiarismPercent(i,j)
                print("\n")
        
        
