tasks = [
    # Generated on 2021-02-05 00:02:27.633009, contains telemetry from sessions 5103 to 5104.
    # The session starts on 2021-02-05 10:51:57+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(31, '/telemetry.previous', [1634, 1684, 1734, 1784, 1834, 1884, 1934, 1984, 2034, 2084, 2134, 2184, 2234, 1659, 1709, 1759, 1809, 1859, 1909, 1959]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [4, 54, 104, 154, 204, 254, 304, 354, 404, 454, 504, 554, 604, 29, 79, 129, 179, 229, 279, 329]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [2009, 2059, 2109, 2159, 2209, 2259, 1647, 1697, 1747, 1797, 1847, 1897, 1947, 1997, 2047, 2097, 2147, 2197, 2247, 1671]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [379, 429, 479, 529, 579, 17, 67, 117, 167, 217, 267, 317, 367, 417, 467, 517, 567, 617, 41, 91]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.previous', [1721, 1771, 1821, 1871, 1921, 1971, 2021, 2071, 2121, 2171, 2221, 2271, 1641, 1691, 1741, 1791, 1841, 1891, 1941, 1991]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [141, 191, 241, 291, 341, 391, 441, 491, 541, 591, 11, 61, 111, 161, 211, 261, 311, 361, 411, 461]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.previous', [2041, 2091, 2141, 2191, 2241, 1653, 1703, 1753, 1803, 1853, 1903, 1953, 2003, 2053, 2103, 2153, 2203, 2253, 1665, 1715]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [511, 561, 611, 23, 73, 123, 173, 223, 273, 323, 373, 423, 473, 523, 573, 35, 85, 135, 185, 235]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.previous', [1765, 1815, 1865, 1915, 1965, 2015, 2065, 2115, 2165, 2215, 2265, 1677, 1727, 1777, 1827, 1877, 1927, 1977, 2027, 2077]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [285, 335, 385, 435, 485, 535, 585, 47, 97, 147, 197, 247, 297, 347, 397, 447, 497, 547, 597]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.previous', [2127, 2177, 2227, 2277]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
