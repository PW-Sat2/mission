tasks = [
    # Generated on 2021-02-10 21:53:01.674932, contains telemetry from sessions 5135 to 5136.
    # The session starts on 2021-02-10 23:10:35+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    # ReadMemory, weird telecommands
    [tc.ReadMemory(2, 0x8801b620, 248), Send, WaitMode.Wait], # scrubbing

    # Wait until good communication
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS A
    [tc.RawI2C(3, 0, 0x35, 1, [0xE0]), Send, WaitMode.Wait],

    [tc.PingTelecommand(), Send, WaitMode.Wait],

    # Set 9600
    [tc.SetBitrate(4, BaudRate.BaudRate9600), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.RemoveFile(100, '/p0_n_p480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(101, '/p0_w_p480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(102, '/p1_n_p480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(103, '/p1_w_p480_0'), Send, WaitMode.Wait],

    [tc.ListFiles(5, '/'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(10, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=19), 'photo01w'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(11, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'photo01n'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(12, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 'photo02w'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(13, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'photo02n'), Send, WaitMode.Wait],
    
    # auto-generated telemetry start
    [tc.DownloadFile(69, '/telemetry.current', [1239, 1289, 1339, 1389, 1439, 1264, 1314, 1364, 1414, 1252, 1302, 1352, 1402, 1452, 1276, 1326, 1376, 1426, 1246, 1296]), Send, WaitMode.Wait],
    [tc.DownloadFile(70, '/telemetry.current', [1346, 1396, 1446, 1258, 1308, 1358, 1408, 1270, 1320, 1370, 1420, 1282, 1332, 1382, 1432]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    # missing from previous session start
    [tc.DownloadFile(30, '/telemetry.current', [319, 337, 363, 369, 413, 419, 657, 707, 757, 907, 957, 975, 1125, 1175]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.previous', [1274, 1278, 1279, 1298, 1299, 1373, 1374, 1484, 1554, 1558, 1559]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]