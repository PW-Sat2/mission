tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Not downloaded telemetry on session 342
    [tc.DownloadFile(69, '/telemetry.current', [1109, 1159, 1209, 1259, 1309, 1359, 21, 71, 121, 171, 221, 271, 321, 371, 421, 471, 521, 571, 621, 671]), Send, WaitMode.Wait],
    [tc.DownloadFile(70, '/telemetry.current', [721, 771, 821, 871, 921, 971, 1021, 1071, 1121, 1171, 1221, 1271, 1321, 1371, 33, 83, 133, 183, 233, 283]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/telemetry.current', [333, 383, 433, 483, 533, 583, 633, 683, 733, 783, 833, 883, 933, 983, 1033, 1083, 1133, 1183, 1233, 1283]), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [1330, 1380, 1430, 1480, 1530, 1355, 1405, 1455, 1505, 1343, 1393, 1443, 1493, 1543, 1367, 1417, 1467, 1517, 1337, 1387]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [1437, 1487, 1537, 1349, 1399, 1449, 1499, 1549, 1361, 1411, 1461, 1511, 1373, 1423, 1473, 1523]), Send, WaitMode.Wait],
    # auto-generated telemetry end
    
    # Low res photos download
    [tc.DownloadFile(100, '/p1_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(101, '/p2_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(102, '/p3_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(103, '/p4_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(104, '/p5_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(105, '/p6_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(106, '/p7_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(107, '/p8_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(108, '/p9_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(109, '/p10_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]