tasks = [
    # Generated on 2020-04-11 22:51:40.849000, contains telemetry from sessions 3210 to 3211.
    # The session starts on 2020-04-12 00:04:19+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(59, '/telemetry.current', [1195, 1245, 1295, 1345, 1395, 1220, 1270, 1320, 1370, 1208, 1258, 1308, 1358, 1408, 1232, 1282, 1332, 1382, 1202, 1252]), Send, WaitMode.Wait],
    [tc.DownloadFile(60, '/telemetry.current', [1302, 1352, 1402, 1214, 1264, 1314, 1364, 1414, 1226, 1276, 1326, 1376, 1238, 1288, 1338, 1388]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/telemetry.current', [198, 248, 273, 298, 304, 348, 354, 398, 448, 498, 548]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [598, 648, 698, 748, 798, 848, 898, 948, 998, 1048, 1173]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/suns_ps_17', [14, 19, 21, 24, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/suns_ps_17', [54, 55, 56, 57, 58, 59, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/suns_ps_17', [93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/suns_ps_17', [112, 113, 114, 115, 116, 117, 118, 119, 140, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/suns_ps_17', [250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/suns_ps_17', [269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 300, 301, 302, 303, 304, 305, 306]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/suns_ps_17', [307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/suns_ps_17', [325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 342, 344, 379]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/p3_480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/p4_480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/p6_480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/p8_480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/p10_480_0', [65, 66]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/p3_480_0', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/p3_480_0', [39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/p3_480_0', [58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/p3_480_0', [77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95]), Send, WaitMode.Wait],
    

    ["Set bootslots for deep_sleep.", Print, WaitMode.NoWait],
    [tc.SetBootSlots(103, 0b111000, 0b111), Send, WaitMode.Wait],

    # Wait for good uplink before power cycle
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS B
    [tc.PowerCycleTelecommand(3), Send, WaitMode.Wait],

    # Get beacons from deep-sleep
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],


    [tc.DownloadFile(49, '/p4_480_0', [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/p4_480_0', [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/p4_480_0', [51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/p4_480_0', [67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/p6_480_0', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/p6_480_0', [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/p6_480_0', [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/p8_480_0', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/p8_480_0', [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/p8_480_0', [59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77]), Send, WaitMode.Wait],

    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]