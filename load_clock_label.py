import pandas as pd


def generateDf(label_dir):
    df = pd.read_csv(label_dir, index_col='Code',encoding="utf8")
    return df

def reallabel(strings, numberOfSlices):
    temp = strings.split(",")  ##
    # temp = "".join(strings.split())
    # temp = temp.split(",")
    ranges = []
    for i in temp:
        if i == '360':
            ranges = range(numberOfSlices-1)
        elif "-" in i:                ##当标签是范围时候
            temp1 = i.split("-")
            # for j in temp1:
            #     ranges.append(j)
            start = float(temp1[0])
            # ranges.append(start)
            if start < float(temp1[1]):      ##当标签范围没有跨越12点
                while start<float(temp1[1]):
                    ranges.append(start%12)
                    start+=1
                    print(ranges)

                ranges.append(float(temp1[1]) if float(temp1[1])!=12.5 else 0.5)
            else:                 ##当标签范围跨越了12点
                while start<float(temp1[1])+12:
                    ranges.append(start%12)
                    start+=1
        else:                ##当标签是单个钟点时
            ranges.append(i)
    print(ranges, len(ranges))
    return ranges


def generate_new_csv(df):
    print(df)
    eyeId = df["Code"]
    print(eyeId)





if __name__ == '__main__':
    label_dir = "G:\CODE\\2019.10\dark_light_pair\sample\\brightVsDarkLabels-utf-8.csv"
    df = generateDf(label_dir)
    # strings = df.loc["C2-014", "Osclock"]
    # print(strings)
    # reallabel(strings, 18)
    # print(df)
    generate_new_csv(df)

