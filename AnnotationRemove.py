with open('E:/DataSet/FLIR_ADAS_v2/video_thermal_test/coco.json', 'r') as f:
    lines = ""
    count = 0
    print("Reading...")
    for line in f:
        lines += line
        
        #print("\rReadLine: "+ str(count),end="")
        count += 1
    print("Read End")
    lineList = lines.split('''},
    {''')
    print(lineList[0])
    nonePersonlineList = [ i for i in lines.split('''},
    {''') if ('"category_id":' in i and '"category_id": 1' not in i)]
    
    imageList = [ i for i in lines.split('''},
    {''') if ("video_id" in i)]
    
    print(imageList[0])
    
    imageIdList = []
    for i in imageList:
        temp = i.split(',')
        imageIdList += [j.split()[1] for j in temp if ('"id":'in j)]
    
    print(imageIdList[-1])
    
    nonePersonIdList = []
    for i in range(imageIdList[-1]):
        nonePersonlineList = [ i for i in nonePersonlineList if ('"id:"'i)]
        
    print("Remove...")
    for i in nonePersonlineList:
        lineList.remove(i)
    
    print(lineList[0])
    fomat_string = '''},
    {'''.join(lineList)
    with open('E:/DataSet/FLIR_ADAS_v2/video_thermal_test/coco2.json', 'w') as f:
        f.write(fomat_string)