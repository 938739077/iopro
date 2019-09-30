import csv
import json


def queryInfo(dataList, pattern):
    for i in range(len(dataList)):
        if dataList[i]["bayonetNum"] == pattern:
            return i
    return -1


content = []
with open('1.csv', 'r') as f:
    csv_file = csv.reader(f)
    print(csv_file)

    e = 0
    for line in csv_file:
        if e == 0:
            e = e + 1
            continue
        print(line)
        FLAG = queryInfo(content, line[3])
        if FLAG == -1:
            if line[2] == '大型汽车':
                tempSet = {
                    "adminRegion": line[1],
                    "bayonetNum": line[3],
                    "bayonetName": line[4],
                    "flowInfoBig": [{
                        "direction": line[5],
                        "timeInfo": line[6:len(line)]
                    }],
                    "flowInfoSmall": [],
                }
            else:
                tempSet = {
                    "adminRegion": line[1],
                    "bayonetNum": line[3],
                    "bayonetName": line[4],
                    "flowInfoBig": [],
                    "flowInfoSmall": [{
                        "direction": line[5],
                        "timeInfo": line[6:len(line)]
                    }],
                }
            content.append(tempSet)
        else:
            tempSet = {
                "direction": line[5],
                "timeInfo": line[6:len(line)]
            }
            if line[2] == '大型汽车':
                content[FLAG]["flowInfoBig"].append(tempSet)
            else:
                content[FLAG]["flowInfoSmall"].append(tempSet)
    f.close()
with open("flow.json", "w", encoding='utf-8') as f1:
    data = {"DATA": content}

    # data = json.dumps(data, ensure_ascii=False)
    #     # print(data)
    json.dump(data, f1, ensure_ascii=False)

