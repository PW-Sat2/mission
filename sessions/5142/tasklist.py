tasks = [
    # Generated on 2021-02-11 21:00:38.203000, contains telemetry from sessions 5141 to 5142.
    # The session starts on 2021-02-11 22:17:14+01:00.

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

    # auto-generated telemetry start
    [tc.DownloadFile(34, '/telemetry.current', [1487, 1537, 1587, 1637, 1687, 1512, 1562, 1612, 1662, 1500, 1550, 1600, 1650, 1524, 1574, 1624, 1674, 1494, 1544, 1594]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [1644, 1694, 1506, 1556, 1606, 1656, 1518, 1568, 1618, 1668, 1530, 1580, 1630, 1680]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/telemetry.current', [676, 688, 700, 712, 719, 726, 738, 744, 750, 762, 776, 788, 800, 812, 819, 826, 838, 850, 862, 869]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [876, 888, 900, 912, 926, 938, 950, 962, 976, 982, 988, 1000, 1012, 1026, 1032, 1038, 1050, 1062, 1076, 1082]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1088, 1100, 1112, 1126, 1138, 1150, 1162, 1176, 1188, 1200, 1212, 1226, 1238, 1250, 1262, 1276, 1288, 1300, 1312, 1326]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [1338, 1350, 1356, 1362, 1376, 1388, 1400, 1406, 1412, 1426, 1438, 1450, 1456, 1462, 1476, 1488, 1500, 1512, 1526]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    [tc.DownloadFile(40, '/t01w_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/t01w_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/t01w_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/t01w_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/t01w_0', range(80, 100)), Send, WaitMode.Wait],

    [tc.DownloadFile(45, '/t01w_0', range(100, 120)), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/t01w_0', range(120, 140)), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/t01w_0', range(140, 160)), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/t01w_0', range(160, 180)), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/t01w_0', range(180, 200)), Send, WaitMode.Wait],

    [tc.DownloadFile(50, '/t01n_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/t01n_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/t01n_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/t01n_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/t01n_0', range(80, 100)), Send, WaitMode.Wait],

    [tc.DownloadFile(55, '/t01n_0', range(100, 120)), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/t01n_0', range(120, 140)), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/t01n_0', range(140, 160)), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/t01n_0', range(160, 180)), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/t01n_0', range(180, 200)), Send, WaitMode.Wait],


    # missing from previous session end
    [tc.DownloadFile(60, '/t02w_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/t02w_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/t02w_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/t02w_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/t02w_0', range(80, 100)), Send, WaitMode.Wait],

    [tc.DownloadFile(65, '/t02w_0', range(100, 120)), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/t02w_0', range(120, 140)), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/t02w_0', range(140, 160)), Send, WaitMode.Wait],
    [tc.DownloadFile(68, '/t02w_0', range(160, 180)), Send, WaitMode.Wait],
    [tc.DownloadFile(69, '/t02w_0', range(180, 200)), Send, WaitMode.Wait],

    [tc.DownloadFile(70, '/t02n_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/t02n_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/t02n_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/t02n_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(74, '/t02n_0', range(80, 100)), Send, WaitMode.Wait],

    [tc.DownloadFile(75, '/t02n_0', range(100, 120)), Send, WaitMode.Wait],
    [tc.DownloadFile(76, '/t02n_0', range(120, 140)), Send, WaitMode.Wait],
    [tc.DownloadFile(77, '/t02n_0', range(140, 160)), Send, WaitMode.Wait],
    [tc.DownloadFile(78, '/t02n_0', range(160, 180)), Send, WaitMode.Wait],
    [tc.DownloadFile(79, '/t02n_0', range(180, 200)), Send, WaitMode.Wait],
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]