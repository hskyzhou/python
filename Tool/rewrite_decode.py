def FAN(n, m):
    i = 0
    z = []
    s = 0
    while n > 0:
        if n % 2 != 0:   #  ����
            z.append(2 - (n % 4))
        else:   #ż��
            z.append(0)
        n = (n - z[i])/2
        i = i + 1
    z = z[::-1]
    l = len(z)
   
    for i in range(0, l):
        s += z[i] * m ** (l - 1 - i)
    return s
   
keys = [ '%02d' % i for i in range(0, 100)]

vals = [ str(FAN(i,3 )) for i in range(0, 100)]

 
keyval = dict(zip(keys, vals))
valkey = dict(zip(vals, keys))

#structList = [
    #['', '8424465873073964565172242657235', 0],
    #['84', '24465873073964565172242657235', 2]
#]

structList = [
    ['', '2712733801194381163880124319146586498182192151917719248224681364019142438188097307292437016388011943193619457377217328473027324319178428', 0],
    ['271', '2733801194381163880124319146586498182192151917719248224681364019142438188097307292437016388011943193619457377217328473027324319178428', 3]
]
searchNum = 4

#��֤�ַ����Ϸ�
def checkStringValid(checkString):
    global valkey
    if valkey.has_key(checkString):
        return True
    else:
        return False
    
def ahead(string, length):
    #��ȡ�ַ���
    slicestring = string[0:length]
    if checkStringValid(slicestring):
        searchList = [slicestring, string[length:], length]
        structList.append(searchList)        
        return True
    else:
        if length < 1:
            resetList() #�����б�
        else:
            ahead(string, length-1)
            
def back():
    pass

#�����б�
def resetList():
    global structList
    #��ȡ���һ���б�
    lastList = structList[len(structList) - 1]
    totalString = lastList[0] + lastList[1]  #�����ַ���
    lastNum = lastList[2]  #��������
    if lastNum <= 1:
        structList = structList[0:len(structList)-1]
        resetList()
    else:
        tempSearchNum = lastNum - 1
        sliceString = totalString[0:tempSearchNum]
        if checkStringValid(sliceString):
            #����
            structList[len(structList) - 1][0] = sliceString
            structList[len(structList) - 1][1] = totalString[tempSearchNum:]
            structList[len(structList) - 1][2] = tempSearchNum
            resetSearchNum()
        else:
            structList[len(structList) - 1][2] = tempSearchNum
            resetList()
        
def resetSearchNum():
    global searchNum
    searchNum = 4
    
while 1:
    ahead(structList[len(structList)-1][1], searchNum)
    
    #print structList
    tems = ''
    for i in structList:
        tems += i[0] + '-'
    tems += '\n'
    fp = open('log.log', 'a+')
    fp.write(tems)
    fp.close()
    #�ж��Ƿ��������
    if structList[len(structList) - 1][1] == '':
        #�������
        istring = ''
        for i in structList:
            liststr = i[0]
            if liststr == '':
                continue
            istring += valkey[liststr]
        #ʮ�����ַ���ת��ʮ������
        hexstring = hex(int(istring))[2:-1]  #ȥ��0x��l
        temi = 0
        resultflag = True
     
        if len(hexstring) % 2 == 0:
            while temi < len(hexstring):
                tempNum = ord(hexstring[temi:temi+2].decode('hex'))
                if tempNum < 21 or tempNum > 126:
                    resultflag = False
                    break
                temi += 2
            #��ȡ����ɹ�
            if resultflag:
                fp = open('result.log', 'a+')
                fp.write(hexstring.decode('hex') + '\n')
                fp.close()    
        resetList()