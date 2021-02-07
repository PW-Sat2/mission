tasks = [
    # Generated on 2021-02-07 19:14:30.049000, contains telemetry from sessions 5118 to 5119.
    # The session starts on 2021-02-07 21:13:59+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    # ReadMemory, weird telecommands
    [tc.ReadMemory(2, 0x8801b620, 248), Send, WaitMode.Wait], # scrubbing

    # Wait until good communication
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS B
    [tc.PowerCycleTelecommand(3), Send, WaitMode.Wait],

    [tc.PingTelecommand(), Send, WaitMode.Wait],

    # Set 9600
    [tc.SetBitrate(4, BaudRate.BaudRate9600), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(5, '/'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(10, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=17), 't01w'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(11, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 't01n'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(12, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 't02w'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(13, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 't02n'), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.previous', [1601, 1651, 1701, 1751, 1801, 1851, 1901, 1951, 2001, 2051, 2101, 2151, 2201, 2251, 1626, 1676, 1726, 1776, 1826, 1876]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [21, 71, 121, 171, 46, 96, 146, 34, 84, 134, 8, 58, 108, 158, 28, 78, 128, 178, 40, 90]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.previous', [1926, 1976, 2026, 2076, 2126, 2176, 2226, 2276, 1614, 1664, 1714, 1764, 1814, 1864, 1914, 1964, 2014, 2064, 2114, 2164]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [2214, 2264, 1638, 1688, 1738, 1788, 1838, 1888, 1938, 1988, 2038, 2088, 2138, 2188, 2238, 1608, 1658, 1708, 1758, 1808]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.previous', [1858, 1908, 1958, 2008, 2058, 2108, 2158, 2208, 2258, 1620, 1670, 1720, 1770, 1820, 1870, 1920, 1970, 2020, 2070, 2120]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.previous', [2170, 2220, 2270, 1632, 1682, 1732, 1782, 1832, 1882, 1932, 1982, 2032, 2082, 2132, 2182, 2232, 1644, 1694, 1744, 1794]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [140, 2, 52, 102, 152, 14, 64, 114, 164]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.previous', [1844, 1894, 1944, 1994, 2044, 2094, 2144, 2194, 2244]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]