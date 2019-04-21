tasks = [
    # Generated on 2019-04-21 11:05:10.309468, contains telemetry from sessions 907 to 908.
    # The session starts on 2019-04-21 12:14:20+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [377, 427, 477, 527, 577, 402, 452, 502, 552, 390, 440, 490, 540, 590, 414, 464, 514, 564, 384, 434]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [484, 534, 584, 396, 446, 496, 546, 596, 408, 458, 508, 558, 420, 470, 520, 570]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    # auto-generated file remove start
    [tc.RemoveFile(63, 'radfet_11'), Send, WaitMode.Wait],
    [tc.ListFiles(64, '/'), Send, WaitMode.Wait],
    # auto-generated file remove end

    # auto-generated file download start
    [tc.DownloadFile(32, '/p7_480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/p7_480_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/p7_480_0', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/p7_480_0', [54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/p7_480_0', [72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/p7_480_0', [90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/p7_480_0', [108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/p7_480_0', [126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/p7_480_0', [144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/p2_480_0', [79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/p2_480_0', [98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/p2_480_0', [117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/p2_480_0', [136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154]), Send, WaitMode.Wait],
    # auto-generated file download end

    # SunS suns_ps_4 experiment file download
    [tc.DownloadFile(71, '/suns_ps_4', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/suns_ps_4', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/suns_ps_4', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(74, '/suns_ps_4', [i for i in range(60, 80, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(75, '/suns_ps_4', [i for i in range(80, 100, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(76, '/suns_ps_4', [i for i in range(100, 120, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(77, '/suns_ps_4', [i for i in range(120, 140, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(78, '/suns_ps_4', [i for i in range(140, 160, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(79, '/suns_ps_4', [i for i in range(160, 180, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(80, '/suns_ps_4', [i for i in range(180, 200, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(81, '/suns_ps_4', [i for i in range(200, 220, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(82, '/suns_ps_4', [i for i in range(220, 240, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(83, '/suns_ps_4', [i for i in range(240, 250, 1)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]