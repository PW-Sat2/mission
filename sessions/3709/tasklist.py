tasks = [
    # Generated on 2020-06-27 22:57:34.057000, contains telemetry from sessions 3708 to 3709.
    # The session starts on 2020-06-28 00:15:17+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(84, '/telemetry.current', [1017, 1067, 1117, 1167, 1217, 1042, 1092, 1142, 1192, 1030, 1080, 1130, 1180, 1230, 1054, 1104, 1154, 1204, 1024, 1074]), Send, WaitMode.Wait],
    [tc.DownloadFile(85, '/telemetry.current', [1124, 1174, 1224, 1036, 1086, 1136, 1186, 1236, 1048, 1098, 1148, 1198, 1060, 1110, 1160, 1210]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/a_n_17_00_0', [47]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/a_n_17_02_0', [49]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/a_n_17_03_0', [43, 44]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/a_n_20_02_0', [34]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/a_w_17_00_0', [57, 58, 59]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/a_w_17_01_0', [27, 45, 59]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/a_w_17_02_0', [31, 45]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/a_w_17_03_0', [13, 16, 17, 19, 30, 43, 44, 45, 46]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/a_w_17_04_0', [15, 20, 22, 30, 54]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/a_w_20_02_0', [54, 57]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/a_w_20_03_0', [47, 48, 49]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/dummy_15_33_0', [20, 21, 22, 23, 24, 25, 27, 41, 42]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/dummy_16_33_0', [23, 26]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/dummy_19_04_0', [47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]), Send, WaitMode.Wait],
    # missing from previous session end


    # jestem kretynem i nie zauwazylem, ze dwie sesje temu liczby chunkow byly strzelone
    [tc.DownloadFile(44, '/a_n_17_00_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/a_n_17_00_0', range(80, 100)), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/a_n_17_00_0', range(120, 140)), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/a_n_17_00_0', range(140, 160)), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/a_n_17_00_0', range(160, 168)), Send, WaitMode.Wait],

    [tc.DownloadFile(47, '/a_n_17_01_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/a_n_17_01_0', range(80, 100)), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/a_n_17_01_0', range(100, 120)), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/a_n_17_01_0', range(120, 137)), Send, WaitMode.Wait],

    [tc.DownloadFile(51, '/a_n_17_02_0', range(60, 74)), Send, WaitMode.Wait],

    [tc.DownloadFile(52, '/a_n_17_03_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/a_n_17_03_0', range(80, 100)), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/a_n_17_03_0', range(100, 120)), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/a_n_17_03_0', range(120, 140)), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/a_n_17_03_0', range(140, 152)), Send, WaitMode.Wait],

    [tc.DownloadFile(53, '/a_n_17_04_0', range(60, 76)), Send, WaitMode.Wait],

    [tc.DownloadFile(54, '/a_n_20_02_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/a_n_20_02_0', range(80, 100)), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/a_n_20_02_0', range(100, 120)), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/a_n_20_02_0', range(120, 142)), Send, WaitMode.Wait],

    [tc.DownloadFile(55, '/a_n_20_03_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/a_n_20_03_0', range(80, 100)), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/a_n_20_03_0', range(100, 120)), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/a_n_20_03_0', range(120, 140)), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/a_n_20_03_0', range(140, 162)), Send, WaitMode.Wait],

    [tc.DownloadFile(56, '/a_w_17_00_0', range(60, 87)), Send, WaitMode.Wait],

    [tc.DownloadFile(57, '/a_w_17_01_0', range(60, 87)), Send, WaitMode.Wait],

    [tc.DownloadFile(58, '/a_w_17_02_0', range(60, 80)), Send, WaitMode.Wait],

    [tc.DownloadFile(59, '/a_w_17_03_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/a_w_17_03_0', range(80, 100)), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/a_w_17_03_0', range(100, 120)), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/a_w_17_03_0', range(120, 140)), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/a_w_17_03_0', range(140, 167)), Send, WaitMode.Wait],

    [tc.DownloadFile(60, '/a_w_17_04_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(60, '/a_w_17_04_0', range(80, 96)), Send, WaitMode.Wait],

    [tc.DownloadFile(61, '/a_w_20_02_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/a_w_20_02_0', range(80, 100)), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/a_w_20_02_0', range(100, 123)), Send, WaitMode.Wait],

    [tc.DownloadFile(62, '/a_w_20_03_0', range(60, 89)), Send, WaitMode.Wait],

    [tc.DownloadFile(63, '/dummy_15_33_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/dummy_15_33_0', range(80, 100)), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/dummy_15_33_0', range(100, 120)), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/dummy_15_33_0', range(120, 136)), Send, WaitMode.Wait],

    [tc.DownloadFile(64, '/dummy_16_33_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/dummy_16_33_0', range(80, 100)), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/dummy_16_33_0', range(100, 120)), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/dummy_16_33_0', range(120, 140)), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/dummy_16_33_0', range(140, 166)), Send, WaitMode.Wait],

    [tc.DownloadFile(65, '/dummy_18_04_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/dummy_18_04_0', range(80, 100)), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/dummy_18_04_0', range(100, 120)), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/dummy_18_04_0', range(120, 140)), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/dummy_18_04_0', range(140, 159)), Send, WaitMode.Wait],


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
