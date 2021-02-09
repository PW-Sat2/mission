tasks = [
    # Generated on 2021-02-09 12:52:30.578000, contains telemetry from sessions 5127 to 5128.
    # The session starts on 2021-02-09 13:36:45+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    # Power cycle EPS B
    [tc.PowerCycleTelecommand(3), Send, WaitMode.Wait],

    [tc.PingTelecommand(), Send, WaitMode.Wait],

    # Set 9600
    [tc.SetBitrate(4, BaudRate.BaudRate9600), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.RemoveFile(44, '/l02n_0'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(10, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=15), 'n01w'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(11, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'n01n'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(12, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=20), 'n02w'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(13, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'n02n'), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(34, '/telemetry.previous', [2107, 2157, 2207, 2257, 2132, 2182, 2232, 2120, 2170, 2220, 2270, 2144, 2194, 2244, 2114, 2164, 2214, 2264, 2126, 2176]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [27, 2, 40, 14, 34, 8, 20]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.previous', [2226, 2276, 2138, 2188, 2238, 2150, 2200, 2250]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/telemetry.current', [767, 817, 1224, 1230, 1236, 1354, 1386, 1398, 1404, 1410, 1424, 1430, 1436, 1442, 1492, 1504]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [1548, 1554, 1560, 1574, 1580, 1586, 1598, 1604, 1610, 1624, 1636, 1660, 1674, 1680, 1698]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1704, 1710, 1724, 1730, 1736, 1748, 1754, 1760, 1774, 1780, 1786, 1798, 1804, 1810, 1824]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [1830, 1836, 1848, 1854, 1860, 1874, 1880, 1886, 1898, 1904, 1910, 1924, 1930, 1948, 1954]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start

    # auto-generated file download end


    # auto-generated file remove start

    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]