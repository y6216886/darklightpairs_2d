import pandas as pd

def readSpecificCol(path):
    df = pd.read_csv(path)
    code = df["Code"]
    # print(list(code))
    list1 = list(code)
    ##### find duplicate id
    # unique_list=[]
    # for i in list1:
    #     if i not in unique_list:
    #         unique_list.append(i)
    #     else:
    #         print(i)
    #
    # #####
    return list1

def generateDf(label_dir):
    df = pd.read_csv(label_dir, index_col='Code',encoding="utf8")
    return df

def reallabel(strings, numberOfSlices):
    # print("strings", strings)
    if str(strings) == "nan":
        ranges = []
        return ranges
    temp = strings.split(",")  ##
    # temp = "".join(strings.split())
    # temp = temp.split(",")
    ranges = []
    for i in temp:
        if i =="-":
            ranges = []
        elif i == '360':
            ranges = range(12)
        elif "-" in i:                ##当标签为范围表示时候
            temp1 = i.split("-")
            # for j in temp1:
            #     ranges.append(j)
            start = float(temp1[0])
            # ranges.append(start)
            if start < float(temp1[1]):      ##当标签范围没有跨越12点
                while start<float(temp1[1]):
                    ranges.append(start%12)
                    start+=1
                    # print(ranges)

                ranges.append(float(temp1[1]) if float(temp1[1])!=12.5 else 0.5)
            else:                 ##当标签范围跨越了12点
                while start<float(temp1[1])+12:
                    ranges.append(start%12)
                    start+=1
                ranges.append(float(temp1[1]) if float(temp1[1]) != 12.5 else 0.5)
        else:                ##当标签是单个钟点时
            try:
                ranges.append(float(i))
            except:
                return []
    # print(ranges, len(ranges))
    return ranges


def generate_new_csv(df):
    print(df)
    eyeId = df
    print(eyeId)


def final_label_table(odrange, osrange, eyeid, slices, df):
    print("start", odrange)
    for i in odrange:
        temp = slices*i/12
        if temp-int(temp) ==0:
            print("index", int(temp))
            df[eyeid+"-"+str(int(temp)), ]   ####over write specific col
        else:
            print("index" , int(temp))
            if int(temp)  < 17:
                print("index", int(temp)+1 )
    return

def writeToCsv(eyeId_list, slices):
    eyeId = []
    od_left = []
    od_right = []
    os_left = []
    os_right  =[]
    for id in eyeId_list:
        for index in range(slices):
            eyeId.append(id+"-"+str(index))
            od_left.append(0)
            od_right.append(0)
            os_left.append(0)
            os_right.append(0)
    dicts = {"eyeId":eyeId, "od_left":od_left, "od_right":od_right, "os_right":os_right, "os_left":os_left}
    dict_df = pd.DataFrame(dicts)
    dict_df.to_csv("E:/code/darklightpairs_2d-master/eyeId_label.csv")

    return 0

def overWriteCsv(csvpath,df):
    target_df = pd.read_csv(csvpath, index_col='eyeId')   ##### the final label csv File
    eyeId_list = readSpecificCol(label_dir)   #### unique eyeId
    for id in eyeId_list:
        print(id)
        strings_od = df.loc[id, "Osclock"]
        strings_os = df.loc[id, "Odclock"]
        ranges_od = reallabel(strings_od, 18)
        ranges_os = reallabel(strings_os, 18)
        print("od range", ranges_od)
        print("os range", ranges_os)
        final_label_table(ranges_od,ranges_os,id, target_df)

if __name__ == '__main__':
    label_dir = "E:/code/darklightpairs_2d-master/brightVsDarkLabels_modified.csv"
    df = generateDf(label_dir)
    # # strings = df.loc["C2-014", "Osclock"]
    # # print(strings)
    # # reallabel(strings, 18)
    # # print(df)
    # generate_new_csv(df)

    eyeId_list = readSpecificCol(label_dir)
    # for id in eyeId_list:
    #     print(id)
    #     strings_od = df.loc[id, "Osclock"]
    #     strings_os = df.loc[id, "Odclock"]
    #     ranges_od = reallabel(strings_od, 18)
    #     ranges_os = reallabel(strings_os, 18)
    #     print("od range", ranges_od)
    #     print("os range", ranges_os)
    #     final_label_table(ranges_od,ranges_os,id)

    # writeToCsv(eyeId_list, 18)

