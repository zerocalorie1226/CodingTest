def solution(x):
    listX=list(str(x))
    listXInt=[int(x) for x in listX]
    sumX=sum(listXInt)

    if(x%sumX==0):
        return True
    else:
        return False
    