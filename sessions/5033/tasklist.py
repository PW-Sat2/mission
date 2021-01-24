tasks = [
    # Generated on 2021-01-24 11:13:40.504000, contains telemetry from sessions 5032 to 5033.
    # The session starts on 2021-01-24 12:10:44+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(44, '/telemetry.current', [857, 907, 957, 1007, 1057, 882, 932, 982, 1032, 870, 920, 970, 1020, 1070, 894, 944, 994, 1044, 864, 914]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.current', [964, 1014, 1064, 876, 926, 976, 1026, 888, 938, 988, 1038, 900, 950, 1000, 1050]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/telemetry.current', [18, 94, 400, 606, 656, 706, 756, 806, 832]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.previous', [1905, 1955, 1962, 2005, 2030, 2080]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/p2_n_p480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/p0_n_p480_0', [8, 10, 11, 63, 64, 65, 66, 67, 68, 69, 70, 71]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/p0_n_p480_0', [72, 74, 75, 76, 77, 78, 92, 106, 107, 139, 146]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/p1_w_p480_0', [20, 40, 51, 54, 56, 59, 60, 62, 64, 65, 85, 86, 87, 88, 89]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/p2_n_p480_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/p2_n_p480_0', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 73]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/p3_w_p480_0', [25, 26, 27, 28, 29, 30, 31, 32, 33, 51, 52, 53, 54, 55, 56, 57, 58, 59]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/p3_w_p480_0', [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/p3_w_p480_0', [78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/p3_w_p480_0', [95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/p3_w_p480_0', [112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/p3_w_p480_0', [129, 130, 131, 132]), Send, WaitMode.Wait],
    # missing from previous session end


    ["Set bootslots for deep_sleep.", Print, WaitMode.NoWait],
    [tc.SetBootSlots(200, 0b111000, 0b111), Send, WaitMode.Wait],

    # Wait for good uplink before power cycle
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS B
    [tc.PowerCycleTelecommand(3), Send, WaitMode.Wait],

    # Get beacons from deep-sleep
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]