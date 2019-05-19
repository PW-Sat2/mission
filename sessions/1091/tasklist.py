tasks = [
    # Generated on 2019-05-19 20:02:00.778000, contains telemetry from sessions 1089 to 1091.
    # The session starts on 2019-05-19 21:08:15+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # missing from previous session start
    [tc.DownloadFile(132, '/suns_ps_4', [75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94]), Send, WaitMode.Wait],
    [tc.DownloadFile(133, '/suns_ps_4', [95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114]), Send, WaitMode.Wait],
    [tc.DownloadFile(134, '/suns_ps_4', [115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134]), Send, WaitMode.Wait],
    [tc.DownloadFile(135, '/suns_ps_4', [135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154]), Send, WaitMode.Wait],
    [tc.DownloadFile(136, '/suns_ps_4', [155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173]), Send, WaitMode.Wait],
    [tc.DownloadFile(137, '/suns_ps_4', [174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192]), Send, WaitMode.Wait],
    [tc.DownloadFile(138, '/suns_ps_4', [193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211]), Send, WaitMode.Wait],
    [tc.DownloadFile(139, '/suns_ps_4', [212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230]), Send, WaitMode.Wait],
    [tc.DownloadFile(140, '/suns_ps_4', [231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249]), Send, WaitMode.Wait],
    # missing from previous session end

    # auto-generated telemetry start
    [tc.DownloadFile(39, '/telemetry.current', [722, 772, 822, 872, 922, 972, 1022, 1072, 1122, 1172, 1222, 1272, 1322, 1372, 1422, 1472, 1522, 1572, 747, 797]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [847, 897, 947, 997, 1047, 1097, 1147, 1197, 1247, 1297, 1347, 1397, 1447, 1497, 1547, 1597, 735, 785, 835, 885]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [935, 985, 1035, 1085, 1135, 1185, 1235, 1285, 1335, 1385, 1435, 1485, 1535, 1585, 759, 809, 859, 909, 959, 1009]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.current', [1059, 1109, 1159, 1209, 1259, 1309, 1359, 1409, 1459, 1509, 1559, 1609, 729, 779, 829, 879, 929, 979, 1029, 1079]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.current', [1129, 1179, 1229, 1279, 1329, 1379, 1429, 1479, 1529, 1579, 741, 791, 841, 891, 941, 991, 1041, 1091, 1141, 1191]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.current', [1241, 1291, 1341, 1391, 1441, 1491, 1541, 1591, 753, 803, 853, 903, 953, 1003, 1053, 1103, 1153, 1203, 1253, 1303]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.current', [1353, 1403, 1453, 1503, 1553, 1603, 765, 815, 865, 915, 965, 1015, 1065, 1115, 1165, 1215, 1265, 1315, 1365, 1415]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.current', [1465, 1515, 1565]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]