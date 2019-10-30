import numpy as np
import pandas as pd
import random
# import cPickle as pkl


def split_dataset_1(root_path, tain_percent=0.4, test_percent=0.5, val_percent=0.1):
    df = pd.read_csv(root_path)
    dark_part = df['dark_part']
    light_part = df["light_part"]
    dark_matrix = dark_part.values
    light_matrix = light_part.values
    pair_matrix = []
    for i, j in zip(dark_matrix, light_matrix):
        pair_matrix.append((i,j))

    # print(pair_matrix)
    random.shuffle(pair_matrix)
    print(pair_matrix)
    tmp_list = []

    for img1, img2 in pair_matrix:
        data = img1.split('_')
        idx = data[0].split("-")[0] + "-" + data[0].split("-")[1]
        if idx not in tmp_list:
            tmp_list.append(idx)

    random.shuffle(tmp_list)
    train_num = int(len(tmp_list) * tain_percent)
    test_num = int(len(tmp_list) * test_percent)
    train_tmp_list = tmp_list[:train_num]
    val_tmp_list = tmp_list[train_num+test_num:]
    train_list = []
    test_list = []
    val_list = []
    for img,_ in pair_matrix:
        data = img.split('_')
        idx = data[0].split("-")[0] + "-" + data[0].split("-")[1]
        if idx in val_tmp_list:
            val_list.append((img1+'.jpg', img2+".jpg"))
        elif idx in train_tmp_list:
            train_list.append((img1+'.jpg', img2+".jpg"))
        else:
            test_list.append((img1+'.jpg', img2+".jpg"))
    return train_list, test_list, val_list


if __name__ == '__main__':
    source_path = 'E:\code\darklightpairs_2d-master/split_data.csv'
    train_dict_vla = {}
    # with open('../../data/train_dict.pkl', 'w+') as f:
    split_dataset_1(source_path)
    train_list, test_list, val_list = split_dataset_1(source_path)
    print(train_list)
    # train_dict_vla['train_list'] = train_list
    # train_dict_vla['test_list'] = test_list
    # train_dict_vla['val_list'] = val_list
    # # pkl.dump(train_dict_vla, f)
    # print ('Step 2_val: success split the dataset, train:%s,test:%s, val:%s'%(len(train_list),len(test_list),len(val_list)))













