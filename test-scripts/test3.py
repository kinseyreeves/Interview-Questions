import numpy as np

SCORES = {
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "10",
    11: "11",
    12: "12",
    13: "13",
    14: "14",
    15: "15",
    16: "16",
    17: "17",
    18: "18",
    19: "19",
    20: "20",
    21: "t7",
    22: "d11",
    24: "d12",
    25: "outer",
    26: "d13",
    27: "t9",
    28: "d14",
    30: "d15",
    32: "d16",
    33: "t11",
    34: "d17",
    36: "d18",
    38: "d19",
    39: "t13",
    40: "d20",
    42: "t14",
    45: "t15",
    48: "t16",
    50: "bull",
    51: "t17",
    54: "t18",
    57: "t19",
    60: "t20",
}
all_scores = []
def find_dart_throws(score):
    arr = np.zeros((len(SCORES)+1, score+2))
    count = 1
    for sc in SCORES:
        arr[count][0] = sc
        count+=1
    count = 1
    #print(arr)
    for i in range(0,score+1):
        arr[0][count] = i
        count+=1
    #print(arr)

    for i in range(1,len(arr)):
        for j in range(1,len(arr[0])):
            t_score = int(arr[i][0])
            if(j > t_score):
                arr[i][j] = min(arr[i-1][j],arr[i][j-t_score]+1)
            else:
                arr[i][j] = arr[i-1][j]

    score_tots = []
    i = len(SCORES)
    j = score + 1
    curr = arr[i][j]
    while(i > 1 and j > 1):
        t_score = int(arr[i][0])
        if(arr[i-1][j] == curr):
            score_tots.append(arr[i-1][j])
            print(arr[0][j])
            i-=1
            
        if(arr[i][j-t_score] == curr):
            score_tots.append(arr[i][j-t_score])
            print(arr[i-1][0])
            j-=t_score

    print(score_tots)


    


    



find_dart_throws(100)

