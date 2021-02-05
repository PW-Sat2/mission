tasks = [
    # Generated on 2021-02-05 15:43:59.799051, contains telemetry from sessions 5106 to 5107.
    # The session starts on 2021-02-05 21:20:55+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    # Wait until good communication
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS A
    [tc.RawI2C(3, 0, 0x35, 1, [0xE0]), Send, WaitMode.Wait],
    [tc.PingTelecommand(), Send, WaitMode.Wait],

    # Set 9600
    [tc.SetBitrate(4, BaudRate.BaudRate9600), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],    

    # remove old files    
    [tc.RemoveFile(40, '/wro_n_p480_21_45_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(41, '/wro_n_p480_22_24_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(42, '/wro_w_p480_21_45_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(43, '/wro_w_p480_22_24_0'), Send, WaitMode.Wait],
    
    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [916, 966, 1016, 1066, 1116, 1166, 1216, 1266, 1316, 1366, 1416, 1466, 1516, 1566, 1616, 1666, 1716, 1766, 941, 991]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [1041, 1091, 1141, 1191, 1241, 1291, 1341, 1391, 1441, 1491, 1541, 1591, 1641, 1691, 1741, 929, 979, 1029, 1079, 1129]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1179, 1229, 1279, 1329, 1379, 1429, 1479, 1529, 1579, 1629, 1679, 1729, 953, 1003, 1053, 1103, 1153, 1203, 1253, 1303]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [1353, 1403, 1453, 1503, 1553, 1603, 1653, 1703, 1753, 923, 973, 1023, 1073, 1123, 1173, 1223, 1273, 1323, 1373, 1423]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [1473, 1523, 1573, 1623, 1673, 1723, 1773, 935, 985, 1035, 1085, 1135, 1185, 1235, 1285, 1335, 1385, 1435, 1485, 1535]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [1585, 1635, 1685, 1735, 947, 997, 1047, 1097, 1147, 1197, 1247, 1297, 1347, 1397, 1447, 1497, 1547, 1597, 1647, 1697]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [1747, 959, 1009, 1059, 1109, 1159, 1209, 1259, 1309, 1359, 1409, 1459, 1509, 1559, 1609, 1659, 1709, 1759]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]