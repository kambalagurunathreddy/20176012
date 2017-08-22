import os,glob,time,math
from temp import euclideanNorm,dotProduct
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
def getAbsFilepath(a):
    temp=str(os.path.join(currentDirABSPath,a))
    return temp
def getFilename(filepath):
    return os.path.split(filepath)[1]
def getFreqDict(filePath,caseSensitive=False):
    ABSFilePath=getAbsFilepath(filePath)
    file=open(ABSFilePath,"r")
    fileContents=file.read()
    words=fileContents.split()
    freqDict={}
    for i in words:
        if not caseSensitive:
            i=i.lower()
        if i not in freqDict:
            freqDict[i]=1
        else:
            freqDict[i]+=1
    return freqDict
def getPlagiarismPercent(file1,file2):
    print("File1 : ",getFilename(file1))
    print("File2 : ",getFilename(file2))
    dict1=getFreqDict(file1)
    dict2=getFreqDict(file2)
    eN1=euclideanNorm(dict1)
    eN2=euclideanNorm(dict2)
    dProduct=dotProduct(dict1,dict2)
    #print(euclideanNorm(dict1))
    #print(euclideanNorm(dict2))
    #print(dProduct)
    theta=math.acos(dProduct/(eN1*eN2))
    theta=round(theta,2)
    #print("theta :",theta)
    MAX=math.pi
    #print("MAX : ",MAX)
    print("Value %d"%((abs(theta-MAX)/MAX)*100))
    #print(theta)
    #print("Mentor Value:",dProduct/(eN1*eN2))
if __name__=="__main__":
    currentDirABSPath=os.path.split(os.path.abspath(__file__))[0]
    #print("os.getcwd()",os.getcwd())
    print("currentDirABSPath",currentDirABSPath)
    #print(glob.glob(currentDirABSPath))
    #print(getFilesList(".txt",sourceFolder="SourceFiles",currentDirABSPath=currentDirABSPath))
    ##################
    filesList=getFilesList(".txt",sourceFolder="SourceFiles")
    print("FList",filesList)
    filesFreqDicts={}
    for i in filesList:
        filesFreqDicts[i]=getFreqDict(i)
    print(filesFreqDicts)
    for i in filesFreqDicts:
        for j in filesFreqDicts:
            getPlagiarismPercent(i,j)
            print("\n")
        
        
