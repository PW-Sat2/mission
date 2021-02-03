tasks = [
    # Generated on 2021-02-03 21:41:03.989000, contains telemetry from sessions 5095 to 5096.
    # The session starts on 2021-02-03 22:57:59+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # files
    [tc.DownloadFile(41, '/wro_w_p480_21_45_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/wro_n_p480_21_45_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/wro_w_p480_22_24_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/wro_n_p480_22_24_0', range(0, 20)), Send, WaitMode.Wait],

    [tc.DownloadFile(45, '/wro_w_p480_21_45_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/wro_n_p480_21_45_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/wro_w_p480_22_24_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/wro_n_p480_22_24_0', range(20, 40)), Send, WaitMode.Wait],

    [tc.DownloadFile(49, '/wro_w_p480_21_45_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/wro_n_p480_21_45_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/wro_w_p480_22_24_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/wro_n_p480_22_24_0', range(40, 60)), Send, WaitMode.Wait],

    [tc.DownloadFile(53, '/wro_w_p480_21_45_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/wro_n_p480_21_45_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/wro_w_p480_22_24_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/wro_n_p480_22_24_0', range(60, 80)), Send, WaitMode.Wait],

    [tc.DownloadFile(57, '/wro_w_p480_21_45_0', range(80, 100)), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/wro_n_p480_21_45_0', range(80, 100)), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/wro_w_p480_22_24_0', range(80, 100)), Send, WaitMode.Wait],
    [tc.DownloadFile(60, '/wro_n_p480_22_24_0', range(80, 100)), Send, WaitMode.Wait],

    [tc.DownloadFile(61, '/wro_w_p480_21_45_0', range(100, 120)), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/wro_n_p480_21_45_0', range(100, 120)), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/wro_w_p480_22_24_0', range(100, 120)), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/wro_n_p480_22_24_0', range(100, 120)), Send, WaitMode.Wait],

    [tc.DownloadFile(65, '/wro_w_p480_21_45_0', range(120, 140)), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/wro_n_p480_21_45_0', range(120, 140)), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/wro_w_p480_22_24_0', range(120, 140)), Send, WaitMode.Wait],
    [tc.DownloadFile(68, '/wro_n_p480_22_24_0', range(120, 140)), Send, WaitMode.Wait],

    [tc.DownloadFile(69, '/wro_w_p480_21_45_0', range(140, 160)), Send, WaitMode.Wait],
    [tc.DownloadFile(70, '/wro_n_p480_21_45_0', range(140, 160)), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/wro_w_p480_22_24_0', range(140, 160)), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/wro_n_p480_22_24_0', range(140, 160)), Send, WaitMode.Wait],

    [tc.DownloadFile(73, '/wro_w_p480_21_45_0', range(160, 180)), Send, WaitMode.Wait],
    [tc.DownloadFile(74, '/wro_n_p480_21_45_0', range(160, 180)), Send, WaitMode.Wait],
    [tc.DownloadFile(75, '/wro_w_p480_22_24_0', range(160, 180)), Send, WaitMode.Wait],
    [tc.DownloadFile(76, '/wro_n_p480_22_24_0', range(160, 180)), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(31, '/telemetry.current', [1042, 1092, 1142, 1192, 1242, 1067, 1117, 1167, 1217, 1055, 1105, 1155, 1205, 1255, 1079, 1129, 1179, 1229, 1049, 1099]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1149, 1199, 1249, 1061, 1111, 1161, 1211, 1073, 1123, 1173, 1223, 1085, 1135, 1185, 1235]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/telemetry.current', [137, 149, 212, 262, 312, 319, 769, 881]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start

    # auto-generated file download end


    # auto-generated file remove start

    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]