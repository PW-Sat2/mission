tasks = [
    # Generated on 2019-08-25 12:21:39.946000, contains telemetry from sessions 1718 to 1719.
    # The session starts on 2019-08-25 13:22:45+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(65, '/telemetry.current', [538, 588, 638, 688, 738, 563, 613, 663, 713, 551, 601, 651, 701, 751, 575, 625, 675, 725, 545, 595]), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/telemetry.current', [645, 695, 745, 557, 607, 657, 707, 757, 569, 619, 669, 719, 581, 631, 681, 731]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(50, '/telemetry.previous', [1450, 1451, 1452, 1453, 1454, 1455, 1456, 1457, 1458, 1459, 1460]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.previous', [1461, 1462, 1463, 1464, 1465, 1466, 1467, 1468, 1469, 1947]), Send, WaitMode.Wait],

    [tc.DownloadFile(42, '/p1_128_0', [11, 12]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/p2_128_0', [14]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/p16_128_0', [3, 5, 6]), Send, WaitMode.Wait],

    [tc.DownloadFile(32, '/p22_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/p14_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/p26_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/p26_128_0', [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]), Send, WaitMode.Wait],

    [tc.DownloadFile(37, '/p15_128_0', [0, 1, 3, 5, 6, 9, 11, 13, 14]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/p12_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/p19_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/p11_128_0', [0, 1, 2, 4, 5, 7, 8, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]), Send, WaitMode.Wait],

    [tc.DownloadFile(46, '/p18_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/p18_128_0', [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/p21_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/p13_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/p20_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), Send, WaitMode.Wait],
    [tc.DownloadFile(60, '/p23_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/p23_128_0', [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/p25_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/p25_128_0', [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/p24_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]), Send, WaitMode.Wait],

    [tc.DownloadFile(40, '/p30_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/p39_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(30, '/p36_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/p28_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/p35_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/p27_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/p33_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/p31_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/p32_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/p34_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/p29_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/p38_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]