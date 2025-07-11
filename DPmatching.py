import math
import os

demention = int(14)
dir1 = "city011"#話者の選択
dir2 = "city022"#話者の選択
p = 0

for file_index1 in range(1, 101):
    resualt_max = 1000
    count = 0
    count_max = 0
    

    file1 = f"{dir1}/{dir1}_{file_index1:03}.txt"#ファイル1
    print(f"{dir1}_{file_index1:03}.txt")#確認用
    
    for file_index2 in range(1, 101):
        file2 = f"{dir2}/{dir2}_{file_index2:03}.txt"#ファイル2

    # ファイル1の読み込み
        with open(file1, "r", encoding="utf-8") as file:
            lines_1 = file.readlines()
            frame_count_1 = int(lines_1[2].strip())
            data_1 = [list(map(float, line.strip().split())) for line in lines_1[3:]]

        # ファイル2の読み込み
        with open(file2, "r", encoding="utf-8") as file:
            lines_2 = file.readlines()
            frame_count_2 = int(lines_2[2].strip())
            data_2 = [list(map(float, line.strip().split())) for line in lines_2[3:]]

        #局所距離の計算
        local_dist = []
        for i in range(frame_count_1):
            row = []
            for j in range(frame_count_2):
                dist_sq = 0
                for k in range(demention):  
                    dist_sq += (data_1[i][k] - data_2[j][k]) ** 2
                row.append(math.sqrt(dist_sq))
            local_dist.append(row)
        
        #累積距離の計算
        cumu_dist = []
        value_init = [local_dist[0][0]]

        #初期値(n行　m,m+1列　加算)
        for i in range(frame_count_2 - 1):
            value_1 = value_init[i] + local_dist[0][i + 1]
            value_init.append(value_1)
        cumu_dist.append(value_init)

        for i in range(frame_count_1 - 1):
            cumu_dist.append([])
            v_list = []
            d_list = [cumu_dist[i][0] + local_dist[i + 1][0]]
            v2_list = []

            #n行m列 n+1行m列　縦加算
            for j in range(frame_count_2):
                value_v = cumu_dist[i][j] + local_dist[i + 1][j]
                v_list.append(value_v)

            #n行m列n+1行m+1列　斜め加算
            for k in range(frame_count_2 - 1):
                value_d = cumu_dist[i][k]*2 + local_dist[i + 1][k + 1]
                d_list.append(value_d)

            resualt_sum = [v_list[0]]
            #n+1行m列n+1行m+1列　横加算
            for m in range(frame_count_2 - 1):
                value_v2 = resualt_sum[m] + local_dist[i + 1][m + 1]
                v2_list.append(value_v2)
                hoge_add = min(v_list[m + 1], d_list[m + 1], v2_list[m])
                resualt_sum.append(hoge_add)
            
            cumu_dist[i + 1] = resualt_sum
        count += 1#ファイル番号の管理

        #最小値の取得
        if resualt_max > cumu_dist[frame_count_1 - 1][frame_count_2 - 1]:
            resualt_max = cumu_dist[frame_count_1 - 1][frame_count_2 - 1]
            count_max = count
    if file_index1 == count_max:
        p += 1
    print(f"{dir2}_{count_max:03}.txt")
    print("////////////////////",resualt_max)
#認識確率
p_resualt = p
print("認識確率は",p_resualt,"%")
