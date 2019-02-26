tasks = [
    # Generated on 2019-02-26 20:51:55.343000, contains telemetry from sessions 550 to 551.
    # The session starts on 2019-02-26 21:56:37+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [1891, 1941, 1991, 2041, 2091, 1916, 1966, 2016, 2066, 1904, 1954, 2004, 2054, 2104, 1928, 1978, 2028, 2078, 1898, 1948]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [1998, 2048, 2098, 1910, 1960, 2010, 2060, 2110, 1922, 1972, 2022, 2072, 1934, 1984, 2034, 2084]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [tc.DownloadFile(40, '/telemetry.previous', [1661, 1923, 2273, 2223, 1761, 2123, 2161, 1949, 1799, 1861, 1811, 2023, 1899, 2073, 2149, 2049, 2249, 1773, 1673, 2011]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.previous', [1723, 2261, 1973, 1911, 2099, 1711, 2061, 2199, 1623, 1999, 1611, 2111, 1823, 1573, 2211, 1873, 1849, 1561, 2173, 1961]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.current', [1481, 893, 993, 943, 1593, 131, 719, 643, 1581, 1431, 93, 1681, 1831, 969, 1281, 1231, 1331, 1319, 243, 231]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.current', [293, 1781, 1093, 1531, 619, 669, 1081, 181, 919, 443, 193, 519, 631, 1631, 931, 819, 1669, 331, 681, 693]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.current', [869, 1731, 1343, 81, 1519, 593, 143, 1719, 1381, 1619, 381, 1493, 1569, 569, 1893, 769, 531, 31, 1393, 1031]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.current', [1543, 1819, 1487, 393, 1269, 493, 1169, 1243, 1069, 369, 743, 781, 419, 431, 1181, 581, 1643, 793, 731, 281]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.current', [343, 1219, 1743, 1043, 1419, 1693, 1469, 1769, 1131, 1919, 1369, 1869, 1793, 1293, 831, 1019, 469, 1119, 1843, 881]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.current', [1193, 981, 1881, 43, 843, 319, 1443, 481, 543, 1143]), Send, WaitMode.Wait],

    # remove files
    [tc.RemoveFile(100, 'p1_480_0' ), Send, WaitMode.Wait],
    [tc.RemoveFile(101, 'p4_480_0' ), Send, WaitMode.Wait],
    [tc.RemoveFile(102, 'p7_480_0' ), Send, WaitMode.Wait],
    
    [tc.ListFiles(112, '/'), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]