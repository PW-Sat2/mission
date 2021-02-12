tasks = [
    # Generated on 2021-02-12 00:04:05.585000, contains telemetry from sessions 5143 to 5144.
    # The session starts on 2021-02-12 10:56:05+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(31, '/telemetry.previous', [1818, 1868, 1918, 1968, 2018, 2068, 2118, 2168, 2218, 2268, 1843, 1893, 1943, 1993, 2043, 2093, 2143, 2193, 2243, 1831]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [38, 88, 138, 188, 238, 288, 338, 388, 438, 488, 538, 588, 638, 688, 738, 788, 13, 63, 113, 163]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [213, 263, 313, 363, 413, 463, 513, 563, 613, 663, 713, 763, 1, 51, 101, 151, 201, 251, 301, 351]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.previous', [1881, 1931, 1981, 2031, 2081, 2131, 2181, 2231, 1855, 1905, 1955, 2005, 2055, 2105, 2155, 2205, 2255, 1825, 1875, 1925]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [401, 451, 501, 551, 601, 651, 701, 751, 25, 75, 125, 175, 225, 275, 325, 375, 425, 475, 525, 575]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [625, 675, 725, 775, 45, 95, 145, 195, 245, 295, 345, 395, 445, 495, 545, 595, 645, 695, 745, 795]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.previous', [1975, 2025, 2075, 2125, 2175, 2225, 2275, 1837, 1887, 1937, 1987, 2037, 2087, 2137, 2187, 2237, 1849, 1899, 1949, 1999]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [7, 57, 107, 157, 207, 257, 307, 357, 407, 457, 507, 557, 607, 657, 707, 757, 19, 69, 119, 169]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.previous', [2049, 2099, 2149, 2199, 2249, 1861, 1911, 1961, 2011, 2061, 2111, 2161, 2211, 2261]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [219, 269, 319, 369, 419, 469, 519, 569, 619, 669, 719, 769, 31, 81, 131, 181, 231, 281, 331, 381]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [431, 481, 531, 581, 631, 681, 731, 781]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start

    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]