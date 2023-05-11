for i in range(1,1001):
    num = str(i).zfill(4)
    with open('C:/Users/11/Downloads/열화상 카메라 이미지/Validation/[V라벨링]08. 사람/정상상황/Validation_HUM_NOM'  '.json', 'r') as f:
        json_data = json.load(f)
        label_info = json_data['label_info']
        
        image_name = label_info['image']['file_name'] # 이미지 파일명
        image_width = label_info['image']['width'] # 이미지 넓이
        image_height = label_info['image']['height'] # 이미지 높이
        annotations =  label_info['annotations']
        image_name = image_name.replace(".jpg", "")
        file = open("./labels/"+image_name + ".txt", "w")
        for annot in annotations:
            x1, y1, x2, y2 = annot['bbox'] 
            x1 = x1/image_width
            y1 = y1/image_height
            x2 = (x2-x1)/image_width
            y2 = (y2-y1)/image_height
            file.write(f"0 {x1:f} {y1:f} {x2:f} {y2:f}\n")
        file.close()