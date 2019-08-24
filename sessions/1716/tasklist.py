tasks = [
    # Generated on 2019-08-24 23:13:12.316000, contains telemetry from sessions 1715 to 1716.
    # The session starts on 2019-08-25 00:16:19+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(79, '/telemetry.current', [1377, 1427, 1477, 1527, 1577, 1402, 1452, 1502, 1552, 1602, 1390, 1440, 1490, 1540, 1590, 1414, 1464, 1514, 1564, 1384]), Send, WaitMode.Wait],
    [tc.DownloadFile(80, '/telemetry.current', [1434, 1484, 1534, 1584, 1396, 1446, 1496, 1546, 1596, 1408, 1458, 1508, 1558, 1420, 1470, 1520, 1570]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(43, '/p1_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/p1_128_0', [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), Send, WaitMode.Wait],
    [tc.DownloadFile(60, '/p2_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/p2_128_0', [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/p3_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/p3_128_0', [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/p4_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/p5_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/p5_128_0', [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/p6_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), Send, WaitMode.Wait],
    [tc.DownloadFile(69, '/p7_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/p8_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), Send, WaitMode.Wait],
    [tc.DownloadFile(76, '/p9_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), Send, WaitMode.Wait],
    [tc.DownloadFile(77, '/p9_128_0', [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]), Send, WaitMode.Wait],

    [tc.DownloadFile(47, '/p10_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/p11_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/p11_128_0', [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/p12_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/p13_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/p14_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/p15_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/p16_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/p16_128_0', [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]), Send, WaitMode.Wait],
    [tc.DownloadFile(70, '/p17_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/p18_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/p18_128_0', [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/p19_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), Send, WaitMode.Wait],
 
    [tc.DownloadFile(65, '/p20_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/p21_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), Send, WaitMode.Wait], 
    [tc.DownloadFile(32, '/p22_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/p23_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/p23_128_0', [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), Send, WaitMode.Wait],
    [tc.DownloadFile(78, '/p24_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]), Send, WaitMode.Wait],
    [tc.DownloadFile(74, '/p25_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), Send, WaitMode.Wait],
    [tc.DownloadFile(75, '/p25_128_0', [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/p26_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/p26_128_0', [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]), Send, WaitMode.Wait],
    
    
    [tc.DownloadFile(66, '/p27_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/p28_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],    
    [tc.DownloadFile(55, '/p29_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/p30_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],    
    [tc.DownloadFile(68, '/p31_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/p32_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/p33_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],   
    [tc.DownloadFile(36, '/p34_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/p35_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(30, '/p36_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/p38_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/p39_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]