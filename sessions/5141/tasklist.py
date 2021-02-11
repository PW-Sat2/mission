tasks = [
    # Generated on 2021-02-11 19:52:33.113000, contains telemetry from sessions 5140 to 5141.
    # The session starts on 2021-02-11 20:48:40+01:00.

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

    [tc.ListFiles(5, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(10, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=12), 't01w'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(11, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 't01n'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(12, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 't02w'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(13, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 't02n'), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(31, '/telemetry.current', [669, 719, 769, 819, 869, 919, 969, 1019, 1069, 1119, 1169, 1219, 1269, 1319, 1369, 1419, 1469, 1519, 694, 744]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [794, 844, 894, 944, 994, 1044, 1094, 1144, 1194, 1244, 1294, 1344, 1394, 1444, 1494, 682, 732, 782, 832, 882]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [932, 982, 1032, 1082, 1132, 1182, 1232, 1282, 1332, 1382, 1432, 1482, 706, 756, 806, 856, 906, 956, 1006, 1056]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [1106, 1156, 1206, 1256, 1306, 1356, 1406, 1456, 1506, 676, 726, 776, 826, 876, 926, 976, 1026, 1076, 1126, 1176]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [1226, 1276, 1326, 1376, 1426, 1476, 1526, 688, 738, 788, 838, 888, 938, 988, 1038, 1088, 1138, 1188, 1238, 1288]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [1338, 1388, 1438, 1488, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [1500, 712, 762, 812, 862, 912, 962, 1012, 1062, 1112, 1162, 1212, 1262, 1312, 1362, 1412, 1462, 1512]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]