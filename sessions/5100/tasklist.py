tasks = [
    # Generated on 2021-02-04 11:24:45.434000, contains telemetry from sessions 5098 to 5099.
    # The session starts on 2021-02-04 11:39:48+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # manually-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.previous', [1042, 1054, 1066, 1078, 1090, 1102, 1114, 1126, 1138, 1150, 1162, 1174, 1186, 1198]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.previous', [1210, 1222, 1234, 1246, 1258, 1270, 1282, 1294, 1306, 1318, 1330, 1342, 1354, 1366]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.previous', [1378, 1390, 1402, 1414, 1426, 1438, 1450, 1462, 1474, 1486, 1498, 1510, 1522, 1534]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [1546, 1558, 1570, 1582, 1594, 1606, 1618, 1630, 1642, 1654, 1666, 1678, 1690, 1702]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.previous', [1714, 1726, 1738, 1750, 1762, 1774, 1786, 1798, 1810, 1822, 1834, 1846, 1858, 1870]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.previous', [1882, 1894, 1906, 1918, 1930, 1942, 1954, 1966, 1978, 1990, 2002, 2014, 2026, 2038]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.previous', [2050, 2062, 2074, 2086, 2098, 2110, 2122, 2134, 2146, 2158, 2170, 2182, 2194, 2206]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.previous', [2218, 2230, 2242, 2254, 2266, 2278]), Send, WaitMode.Wait],
    
    [tc.DownloadFile(38, '/telemetry.current', [290, 302, 314, 326, 338, 350, 362, 374, 386, 398, 410, 422, 434, 446]), Send, WaitMode.Wait],
    # manually-generated telemetry end



    # auto-generated file download start

    # auto-generated file download end


    # auto-generated file remove start

    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]