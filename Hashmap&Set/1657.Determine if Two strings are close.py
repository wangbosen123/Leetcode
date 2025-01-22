class Solution:
    def closeStrings(self, word1, word2) :
        word1_hashmap = {}
        word2_hashmap = {}

        for word in word1:
            if word in word1_hashmap:
                word1_hashmap[word] += 1
            else:
                word1_hashmap[word] = 0

        for word in word2:
            if word in word2_hashmap:
                word2_hashmap[word] += 1
            else:
                word2_hashmap[word] = 0

        word1_type, word1_num = set(), set()
        word2_type, word2_num = set(), set()

        for (key, value) in word1_hashmap.items():
            if key not in word1_type:
                word1_type.add(key)
            if value not in word1_num:
                word1_num.add(value)
        for (key, value) in word2_hashmap.items():
            if key not in word2_type:
                word2_type.add(key)
            if value not in word2_num:
                word2_num.add(value)
        print(word1_type, word1_num, word2_type, word2_num)
        print(word1_type == word2_type)
        return (word1_type == word2_type) and (word1_num == word2_num)

if __name__ == '__main__':
    # s = Solution()
    # word1 = 'aaabbbbccddeeeeefffff'
    # word2 = 'aaaaabbcccdddeeeeffff'
    # print(s.closeStrings(word1, word2))

    import os
    import matplotlib.pyplot as plt
    import cv2
    import numpy as np
    import shutil
    shutil.rmtree('C:/Users/240503/Desktop/PCB_Background')
    if os.path.exists('C:/Users/240503/Desktop/PCB_Background'): pass
    else: os.mkdir('C:/Users/240503/Desktop/PCB_Background')

    if os.path.exists('C:/Users/240503/Desktop/PCB_Background/train'): pass
    else:
        os.mkdir('C:/Users/240503/Desktop/PCB_Background/train_HR')
        os.mkdir('C:/Users/240503/Desktop/PCB_Background/train_LR')

    if os.path.exists('C:/Users/240503/Desktop/PCB_Background/test'): pass
    else:
        os.mkdir('C:/Users/240503/Desktop/PCB_Background/test_HR')
        os.mkdir('C:/Users/240503/Desktop/PCB_Background/test_LR')

    def sliding_window(image, h, w):
        images = []
        for x in range(0, w, 640):
            for y in range(0, h, 640):
                crop_image = image[y: y+640, x: x+640]
                if crop_image.shape != (640, 640, 3): continue
                images.append(crop_image)
        return np.array(images)

    path = 'D:/PCB defect detection/PCB_Automation_crop/PCBA_V9300/'
    for num, filename in enumerate(os.listdir(path)):
        if num > 5: break
        image = cv2.imread(path + filename)
        h, w = image.shape[0], image.shape[1]
        subimages = sliding_window(image, h, w)
        print(subimages.shape)
        if num < 5:
            for subnum, image in enumerate(subimages):
                L = cv2.resize(image, (160, 160), cv2.INTER_CUBIC)
                cv2.imwrite(f'C:/Users/240503/Desktop/PCB_Background/train_HR/{num}_{subnum}.jpg', image)
                cv2.imwrite(f'C:/Users/240503/Desktop/PCB_Background/train_LR/{num}_{subnum}.jpg', L)

        if num == 5:
            for subnum, image in enumerate(subimages):
                L = cv2.resize(image, (160, 160), cv2.INTER_CUBIC)
                cv2.imwrite(f'C:/Users/240503/Desktop/PCB_Background/test_HR/{num}_{subnum}.jpg', image)
                cv2.imwrite(f'C:/Users/240503/Desktop/PCB_Background/test_LR/{num}_{subnum}.jpg', L)



