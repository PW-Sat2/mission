tasks = [
    # Generated on 2019-07-29 08:52:01.901000, contains telemetry from sessions 1553 to 1555.
    # The session starts on 2019-07-29 10:07:09+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(31, '/telemetry.previous', [1721, 1771, 1821, 1871, 1921, 1971, 2021, 2071, 2121, 2171, 2221, 2271, 1746, 1796, 1846, 1896, 1946, 1996, 2046, 2096]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [41, 91, 141, 191, 241, 291, 341, 391, 441, 491, 541, 591, 641, 691, 741, 16, 66, 116, 166, 216]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [2146, 2196, 2246, 1734, 1784, 1834, 1884, 1934, 1984, 2034, 2084, 2134, 2184, 2234, 1758, 1808, 1858, 1908, 1958, 2008]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [266, 316, 366, 416, 466, 516, 566, 616, 666, 716, 4, 54, 104, 154, 204, 254, 304, 354, 404, 454]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [504, 554, 604, 654, 704, 28, 78, 128, 178, 228, 278, 328, 378, 428, 478, 528, 578, 628, 678, 728]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.previous', [2058, 2108, 2158, 2208, 2258, 1728, 1778, 1828, 1878, 1928, 1978, 2028, 2078, 2128, 2178, 2228, 2278, 1740, 1790, 1840]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [48, 98, 148, 198, 248, 298, 348, 398, 448, 498, 548, 598, 648, 698, 748, 10, 60, 110, 160, 210]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.previous', [1890, 1940, 1990, 2040, 2090, 2140, 2190, 2240, 1752, 1802, 1852, 1902, 1952, 2002, 2052, 2102, 2152, 2202, 2252, 1764]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [260, 310, 360, 410, 460, 510, 560, 610, 660, 710, 22, 72, 122, 172, 222, 272, 322, 372, 422, 472]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [522, 572, 622, 672, 722, 34, 84, 134, 184, 234, 284, 334, 384, 434, 484, 534, 584, 634, 684, 734]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.previous', [1814, 1864, 1914, 1964, 2014, 2064, 2114, 2164, 2214, 2264]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    ,
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]