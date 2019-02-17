tasks = [
    # Generated on 2019-02-17 21:39:06.077000, contains telemetry from sessions 492 to 493.
    # The session starts on 2019-02-17 22:52:32+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [1119, 1169, 1219, 1269, 1319, 1144, 1194, 1244, 1294, 1344, 1132, 1182, 1232, 1282, 1332, 1156, 1206, 1256, 1306, 1126]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [1176, 1226, 1276, 1326, 1138, 1188, 1238, 1288, 1338, 1150, 1200, 1250, 1300, 1162, 1212, 1262, 1312]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    # missings from 492
    [tc.DownloadFile(40, '/p7_480_0', [111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/p1_480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/p1_480_0', [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/p1_480_0', [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/p1_480_0', [56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/p1_480_0', [74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91]), Send, WaitMode.Wait],

    # big photos download
    # p3_128_0 - 152
    [tc.DownloadFile(60, '/p3_480_0', [i for i in range(0, 26, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/p3_480_0', [i for i in range(26, 52, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/p3_480_0', [i for i in range(52, 78, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/p3_480_0', [i for i in range(78, 92, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/p3_480_0', [i for i in range(92, 104, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/p3_480_0', [i for i in range(104, 129, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/p3_480_0', [i for i in range(129, 152, 1)]), Send, WaitMode.Wait],

    # p2_128_0 - 146
    [tc.DownloadFile(70, '/p2_480_0', [i for i in range(0, 26, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/p2_480_0', [i for i in range(26, 52, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/p2_480_0', [i for i in range(52, 78, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/p2_480_0', [i for i in range(78, 92, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(74, '/p2_480_0', [i for i in range(92, 104, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(75, '/p2_480_0', [i for i in range(104, 132, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(76, '/p2_480_0', [i for i in range(132, 146, 1)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]