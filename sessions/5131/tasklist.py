tasks = [
    # Generated on 2021-02-09 22:48:47.509000, contains telemetry from sessions 5130 to 5131.
    # The session starts on 2021-02-10 00:03:32+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(39, '/telemetry.current', [973, 1023, 1073, 1123, 1173, 998, 1048, 1098, 1148, 986, 1036, 1086, 1136, 1186, 1010, 1060, 1110, 1160, 980, 1030]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [1080, 1130, 1180, 992, 1042, 1092, 1142, 1004, 1054, 1104, 1154, 1016, 1066, 1116, 1166]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/n02n_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/n02n_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/n02n_0', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/n02n_0', [54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/n02n_0', [72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/n02n_0', [90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]