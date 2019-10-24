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


def final_label_table(odrange, osrange, eyeid, slices=18):
    print("start", odrange)
    for i in odrange:
        temp = slices*i/12
        if temp-int(temp) ==0:
            print("index", int(temp))
        else:
            print("index" , int(temp))
            if int(temp)  < 17:
                print("index", int(temp)+1 )
    return


if __name__ == '__main__':
    label_dir = "E:/code/darklightpairs_2d-master/brightVsDarkLabels_modified.csv"
    df = generateDf(label_dir)
    # # strings = df.loc["C2-014", "Osclock"]
    # # print(strings)
    # # reallabel(strings, 18)
    # # print(df)
    # generate_new_csv(df)

    eyeId_list = readSpecificCol(label_dir)
    for id in eyeId_list:
        print(id)
        strings_od = df.loc[id, "Osclock"]
        strings_os = df.loc[id, "Odclock"]
        ranges_od = reallabel(strings_od, 18)
        ranges_os = reallabel(strings_os, 18)
        print("od range", ranges_od)
        print("os range", ranges_os)
        final_label_table(ranges_od,ranges_os,id)

