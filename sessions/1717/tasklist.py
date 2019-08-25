tasks = [
    # Generated on 2019-08-25 00:40:46.986000, contains telemetry from sessions 1716 to 1717.
    # The session starts on 2019-08-25 10:12:34+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(68, '/telemetry.previous', [1554, 1604, 1654, 1704, 1754, 1804, 1854, 1904, 1954, 2004, 2054, 2104, 2154, 2204, 2254, 1579, 1629, 1679, 1729, 1779]), Send, WaitMode.Wait],
    [tc.DownloadFile(69, '/telemetry.current', [24, 74, 124, 174, 224, 274, 324, 374, 49, 99, 149, 199, 249, 299, 349, 399, 37, 87, 137, 187]), Send, WaitMode.Wait],
    [tc.DownloadFile(70, '/telemetry.previous', [1829, 1879, 1929, 1979, 2029, 2079, 2129, 2179, 2229, 2279, 1567, 1617, 1667, 1717, 1767, 1817, 1867, 1917, 1967, 2017]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/telemetry.previous', [2067, 2117, 2167, 2217, 2267, 1591, 1641, 1691, 1741, 1791, 1841, 1891, 1941, 1991, 2041, 2091, 2141, 2191, 2241, 1561]), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/telemetry.current', [237, 287, 337, 387, 11, 61, 111, 161, 211, 261, 311, 361, 31, 81, 131, 181, 231, 281, 331, 381]), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/telemetry.previous', [1611, 1661, 1711, 1761, 1811, 1861, 1911, 1961, 2011, 2061, 2111, 2161, 2211, 2261, 1573, 1623, 1673, 1723, 1773, 1823]), Send, WaitMode.Wait],
    [tc.DownloadFile(74, '/telemetry.previous', [1873, 1923, 1973, 2023, 2073, 2123, 2173, 2223, 2273, 1585, 1635, 1685, 1735, 1785, 1835, 1885, 1935, 1985, 2035, 2085]), Send, WaitMode.Wait],
    [tc.DownloadFile(75, '/telemetry.current', [43, 93, 143, 193, 243, 293, 343, 393, 5, 55, 105, 155, 205, 255, 305, 355, 405, 17, 67, 117]), Send, WaitMode.Wait],
    [tc.DownloadFile(76, '/telemetry.previous', [2135, 2185, 2235, 1597, 1647, 1697, 1747, 1797, 1847, 1897, 1947, 1997, 2047, 2097, 2147, 2197, 2247, 1477]), Send, WaitMode.Wait],
    [tc.DownloadFile(77, '/telemetry.current', [167, 217, 267, 317, 367]), Send, WaitMode.Wait],
    # auto-generated telemetry end
    
    # more telemetry during reboot start
    [tc.DownloadFile(170, '/telemetry.previous', [i for i in range(1370, 1390, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(171, '/telemetry.previous', [i for i in range(1390, 1410, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(172, '/telemetry.previous', [i for i in range(1410, 1430, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(173, '/telemetry.previous', [i for i in range(1430, 1450, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(174, '/telemetry.previous', [i for i in range(1450, 1470, 1)]), Send, WaitMode.Wait],
    # more telemetry during reboot end

    # missing from previous session start
    [tc.DownloadFile(33, '/p1_128_0', [11, 12]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/p2_128_0', [3, 5, 6, 14, 17]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/p4_128_0', [6, 8]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/p5_128_0', [24]), Send, WaitMode.Wait],

    [tc.DownloadFile(46, '/p11_128_0', [0, 1, 2, 4, 5, 7, 8, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/p12_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/p13_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/p14_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/p15_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/p16_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), Send, WaitMode.Wait],    
    [tc.DownloadFile(45, '/p16_128_0', [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/p17_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/p18_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/p18_128_0', [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/p19_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), Send, WaitMode.Wait],

    [tc.DownloadFile(57, '/p20_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/p21_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/p22_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/p23_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/p23_128_0', [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/p24_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]), Send, WaitMode.Wait],    
    [tc.DownloadFile(65, '/p25_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/p25_128_0', [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/p26_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/p26_128_0', [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]), Send, WaitMode.Wait],

    [tc.DownloadFile(58, '/p27_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/p28_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/p29_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/p30_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(60, '/p31_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/p32_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/p33_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/p34_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/p35_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(30, '/p36_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/p38_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/p39_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]