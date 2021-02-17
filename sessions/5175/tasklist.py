tasks = [
    # Generated on 2021-02-17 21:26:21.366000, contains telemetry from sessions 5174 to 5175.
    # The session starts on 2021-02-17 22:37:38+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    # Wait until good communication
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS B
    [tc.PowerCycleTelecommand(3), Send, WaitMode.Wait],

    [tc.PingTelecommand(), Send, WaitMode.Wait],

    # Set 9600
    [tc.SetBitrate(4, BaudRate.BaudRate9600), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(5, '/'), Send, WaitMode.Wait],

    # Skip this if photos are already taken, if not then photos are taken immediately 
    [tc.TakePhotoTelecommand(60, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p5174_0_n_p480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(61, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p5174_1_w_p480'), Send, WaitMode.Wait],

    # This should show the new photos
    [tc.ListFiles(6, '/'), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(38, '/telemetry.current', [100, 150, 200, 250, 300, 125, 175, 225, 275, 113, 163, 213, 263, 137, 187, 237, 287, 107, 157, 207]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [257, 307, 119, 169, 219, 269, 131, 181, 231, 281, 143, 193, 243, 293]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    # missing from previous session start
    [tc.DownloadFile(30, '/telemetry.current', [34, 41, 72, 84, 122, 134]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.previous', [78, 84, 240, 360, 703, 716, 928, 990, 1134, 1140, 1146, 1178, 1184, 1190, 1196, 1237, 1261, 1402, 1408, 1414]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.previous', [1420, 1426, 1432, 1438, 1452, 1458, 1464, 1476, 1482, 1488, 1495, 1502, 1508, 1514, 1526, 1532, 1538, 1552, 1564, 1571]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [1576, 1578, 1582, 1584, 1588, 1590, 1602, 1608, 1614, 1628, 1634, 1640, 1652, 1658, 1664, 1678, 1684, 1690, 1702]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.previous', [1708, 1714, 1728, 1734, 1740, 1752, 1758, 1764, 1778, 1784, 1790, 1802, 1808, 1814, 1828, 1834, 1840, 1846, 1852]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.previous', [1858, 1864, 1878, 1884, 1890, 1902, 1908, 1914, 1921, 1928, 1934, 1940, 1952, 1958, 1964, 1971, 1978, 1984, 1990]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.previous', [2002, 2008, 2014, 2028, 2034, 2040, 2052, 2058, 2064, 2078, 2084, 2090, 2096, 2102, 2108, 2114, 2128, 2134, 2140]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.previous', [2146, 2152, 2158, 2164, 2178, 2184, 2190, 2196, 2202, 2208, 2214, 2228, 2234, 2240, 2246, 2252, 2258, 2264, 2278]), Send, WaitMode.Wait],
    # missing from previous session end
    
    # Blind download photos
    [tc.DownloadFile(40, '/p5174_0_n_p480_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/p5174_0_n_p480_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/p5174_0_n_p480_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/p5174_0_n_p480_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/p5174_0_n_p480_0', range(80, 100)), Send, WaitMode.Wait],

    [tc.DownloadFile(45, '/p5174_0_n_p480_0', range(100, 120)), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/p5174_0_n_p480_0', range(120, 140)), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/p5174_0_n_p480_0', range(140, 160)), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/p5174_0_n_p480_0', range(160, 180)), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/p5174_0_n_p480_0', range(180, 200)), Send, WaitMode.Wait],

    [tc.DownloadFile(50, '/p5174_1_w_p480_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/p5174_1_w_p480_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/p5174_1_w_p480_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/p5174_1_w_p480_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/p5174_1_w_p480_0', range(80, 100)), Send, WaitMode.Wait],

    [tc.DownloadFile(55, '/p5174_1_w_p480_0', range(100, 120)), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/p5174_1_w_p480_0', range(120, 140)), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/p5174_1_w_p480_0', range(140, 160)), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/p5174_1_w_p480_0', range(160, 180)), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/p5174_1_w_p480_0', range(180, 200)), Send, WaitMode.Wait],


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]