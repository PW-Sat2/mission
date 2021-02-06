tasks = [
    # Generated on 2021-02-06 12:08:22.351000, contains telemetry from sessions 5111 to 5112.
    # The session starts on 2021-02-06 13:05:11+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [1005, 1055, 1105, 1155, 1205, 1030, 1080, 1130, 1180, 1018, 1068, 1118, 1168, 1218, 1042, 1092, 1142, 1192, 1012, 1062]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [1112, 1162, 1212, 1024, 1074, 1124, 1174, 1036, 1086, 1136, 1186, 1048, 1098, 1148, 1198]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    [tc.DownloadFile(40, '/radfet_59', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],


    [tc.TakePhotoTelecommand(4, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p0_w_p480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(5, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=2), 'p0_n_p480'), Send, WaitMode.Wait],


    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(3, '/'), Send, WaitMode.Wait],


    # Try to download the photos without knowing sizes
    [tc.DownloadFile(42, '/p0_w_p480_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/p0_w_p480_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/p0_w_p480_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/p0_w_p480_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/p0_w_p480_0', range(80, 100)), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/p0_w_p480_0', range(100, 120)), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/p0_w_p480_0', range(120, 140)), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/p0_w_p480_0', range(140, 160)), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/p0_w_p480_0', range(160, 180)), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/p0_w_p480_0', range(180, 200)), Send, WaitMode.Wait],

    [tc.DownloadFile(47, '/p0_n_p480_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/p0_n_p480_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/p0_n_p480_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/p0_n_p480_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/p0_n_p480_0', range(80, 100)), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/p0_n_p480_0', range(100, 120)), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/p0_n_p480_0', range(120, 140)), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/p0_n_p480_0', range(140, 160)), Send, WaitMode.Wait],
    [tc.DownloadFile(68, '/p0_n_p480_0', range(160, 180)), Send, WaitMode.Wait],
    [tc.DownloadFile(69, '/p0_n_p480_0', range(180, 200)), Send, WaitMode.Wait],

    # missing from previous session start
    
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]