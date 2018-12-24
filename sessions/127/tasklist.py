tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    # Telemetry between session 125 and 127
    [tc.DownloadFile(10, '/telemetry.current', [i for i in range(0, 1342, 70)]), Send, WaitMode.Wait],
    [tc.DownloadFile(11, '/telemetry.current', [i for i in range(35, 1342, 70)]), Send, WaitMode.Wait],
    [tc.DownloadFile(12, '/telemetry.previous', [i for i in range(2250, 2280, 2)]), Send, WaitMode.Wait],
    [tc.DownloadFile(13, '/telemetry.previous', [i for i in range(2251, 2280, 2)]), Send, WaitMode.Wait],

    # Eighth SunS experiment
    [tc.PerformSunSExperiment(20, 0, 20, 254, datetime.timedelta(seconds=2), 7, datetime.timedelta(seconds=10), 'suns_8'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],

    # Low res photos download
    [tc.DownloadFile(30, '/p1_128_0', [6]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/p2_128_0', [1, 2, 4, 5, 6, 7, 8]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/p3_128_0', [6]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/p4_128_0', [0, 1, 2]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/p5_128_0', [i for i in range(0, 8, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/p6_128_0', [i for i in range(0, 9, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/p7_128_0', [i for i in range(0, 8, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/p8_128_0', [i for i in range(0, 7, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/p9_128_0', [i for i in range(0, 7, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/p10_128_0', [i for i in range(0, 7, 1)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],

    # More telemetry between session 125 and 127
    [tc.DownloadFile(40, '/telemetry.current', [i for i in range(1, 1342, 70)]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [i for i in range(2, 1342, 70)]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.current', [i for i in range(3, 1342, 70)]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.current', [i for i in range(4, 1342, 70)]), Send, WaitMode.Wait],

    # First high res photos download
    [tc.DownloadFile(50, '/p1_480_0', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/p1_480_0', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/p1_480_0', [i for i in range(40, 67, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(53, '/p2_480_0', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/p2_480_0', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/p2_480_0', [i for i in range(40, 64, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(56, '/p3_480_0', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/p3_480_0', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/p3_480_0', [i for i in range(40, 52, 1)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],

    [tc.DownloadFile(60, '/telemetry.current', [i for i in range(5, 1342, 70)]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/telemetry.current', [i for i in range(6, 1342, 70)]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/telemetry.current', [i for i in range(7, 1342, 70)]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/telemetry.current', [i for i in range(8, 1342, 70)]), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/telemetry.current', [i for i in range(9, 1342, 70)]), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/telemetry.current', [i for i in range(10, 1342, 70)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],

    # Missing telemetry between session 124 and 125
    [tc.DownloadFile(200, '/telemetry.previous', [2071, 2072, 2074, 2075, 2076, 2077, 2078, 2079, 2080, 2081, 2083, 2084, 2086, 2087, 2089, 2090]), Send, WaitMode.Wait],
    [tc.DownloadFile(201, '/telemetry.previous', [2091, 2092, 2093, 2095, 2096, 2098, 2099, 2101, 2102, 2103, 2104, 2105, 2107, 2108, 2110, 2111]), Send, WaitMode.Wait],
    [tc.DownloadFile(202, '/telemetry.previous', [2113, 2114, 2115, 2116, 2117, 2119, 2120, 2122, 2123, 2124, 2125, 2126, 2128, 2129, 2131, 2132]), Send, WaitMode.Wait],
    [tc.DownloadFile(203, '/telemetry.previous', [2134, 2135, 2137, 2138, 2139, 2140, 2141, 2143, 2144, 2146, 2147, 2149, 2150, 2152, 2153, 2155]), Send, WaitMode.Wait],
    [tc.DownloadFile(204, '/telemetry.previous', [2156, 2158, 2159, 2161, 2162, 2164, 2165, 2167, 2168, 2170, 2171, 2173, 2174, 2175, 2176, 2177]), Send, WaitMode.Wait], 
    [tc.DownloadFile(205, '/telemetry.previous', [2179, 2180, 2182, 2183, 2185, 2186, 2188, 2189, 2191, 2192, 2194, 2195, 2197, 2198, 2199, 2200]), Send, WaitMode.Wait],
    [tc.DownloadFile(206, '/telemetry.previous', [2201, 2202, 2203, 2204, 2206, 2207, 2209, 2210, 2211, 2212, 2213, 2215, 2216, 2218, 2219, 2220]), Send, WaitMode.Wait],
    [tc.DownloadFile(207, '/telemetry.previous', [2221, 2222, 2224, 2225, 2226, 2227, 2228, 2229, 2230, 2231, 2233, 2234, 2236, 2237, 2238, 2239]), Send, WaitMode.Wait], 
    [tc.DownloadFile(208, '/telemetry.previous', [2240, 2241, 2242, 2243, 2244, 2245, 2246, 2248, 2249]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],

    # More telemetry between session 125 and 127
    [tc.DownloadFile(70, '/telemetry.current', [i for i in range(11, 1342, 70)]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/telemetry.current', [i for i in range(12, 1342, 70)]), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/telemetry.current', [i for i in range(13, 1342, 70)]), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/telemetry.current', [i for i in range(14, 1342, 70)]), Send, WaitMode.Wait],
    [tc.DownloadFile(74, '/telemetry.current', [i for i in range(15, 1342, 70)]), Send, WaitMode.Wait],
    [tc.DownloadFile(75, '/telemetry.current', [i for i in range(16, 1342, 70)]), Send, WaitMode.Wait],
    [tc.DownloadFile(76, '/telemetry.current', [i for i in range(17, 1342, 70)]), Send, WaitMode.Wait],
    [tc.DownloadFile(77, '/telemetry.current', [i for i in range(18, 1342, 70)]), Send, WaitMode.Wait],
    [tc.DownloadFile(78, '/telemetry.current', [i for i in range(19, 1342, 70)]), Send, WaitMode.Wait],
    [tc.DownloadFile(79, '/telemetry.current', [i for i in range(20, 1342, 70)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],

    [tc.DownloadFile(80, '/telemetry.current', [i for i in range(21, 1342, 70)]), Send, WaitMode.Wait],
    [tc.DownloadFile(81, '/telemetry.current', [i for i in range(22, 1342, 70)]), Send, WaitMode.Wait],
    [tc.DownloadFile(82, '/telemetry.current', [i for i in range(23, 1342, 70)]), Send, WaitMode.Wait],
    [tc.DownloadFile(83, '/telemetry.current', [i for i in range(24, 1342, 70)]), Send, WaitMode.Wait],
    [tc.DownloadFile(84, '/telemetry.current', [i for i in range(25, 1342, 70)]), Send, WaitMode.Wait],
    [tc.DownloadFile(85, '/telemetry.current', [i for i in range(26, 1342, 70)]), Send, WaitMode.Wait],
    [tc.DownloadFile(86, '/telemetry.current', [i for i in range(27, 1342, 70)]), Send, WaitMode.Wait],
    [tc.DownloadFile(87, '/telemetry.current', [i for i in range(28, 1342, 70)]), Send, WaitMode.Wait],
    [tc.DownloadFile(88, '/telemetry.current', [i for i in range(29, 1342, 70)]), Send, WaitMode.Wait],
    [tc.DownloadFile(89, '/telemetry.current', [i for i in range(70, 1342, 70)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],

    [tc.DownloadFile(90, '/telemetry.current', [i for i in range(31, 1342, 70)]), Send, WaitMode.Wait],
    [tc.DownloadFile(91, '/telemetry.current', [i for i in range(32, 1342, 70)]), Send, WaitMode.Wait],
    [tc.DownloadFile(92, '/telemetry.current', [i for i in range(33, 1342, 70)]), Send, WaitMode.Wait],
    [tc.DownloadFile(93, '/telemetry.current', [i for i in range(34, 1342, 70)]), Send, WaitMode.Wait],
    [tc.DownloadFile(94, '/telemetry.current', [i for i in range(35, 1342, 70)]), Send, WaitMode.Wait],
    [tc.DownloadFile(95, '/telemetry.current', [i for i in range(36, 1342, 70)]), Send, WaitMode.Wait],
    [tc.DownloadFile(96, '/telemetry.current', [i for i in range(37, 1342, 70)]), Send, WaitMode.Wait],
    [tc.DownloadFile(97, '/telemetry.current', [i for i in range(38, 1342, 70)]), Send, WaitMode.Wait],
    [tc.DownloadFile(98, '/telemetry.current', [i for i in range(39, 1342, 70)]), Send, WaitMode.Wait],
    [tc.DownloadFile(99, '/telemetry.current', [i for i in range(40, 1342, 70)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],

    [tc.DownloadFile(110, '/telemetry.current', [i for i in range(41, 1342, 70)]), Send, WaitMode.Wait],
    [tc.DownloadFile(111, '/telemetry.current', [i for i in range(42, 1342, 70)]), Send, WaitMode.Wait],
    [tc.DownloadFile(112, '/telemetry.current', [i for i in range(43, 1342, 70)]), Send, WaitMode.Wait],
    [tc.DownloadFile(113, '/telemetry.current', [i for i in range(44, 1342, 70)]), Send, WaitMode.Wait],
    [tc.DownloadFile(114, '/telemetry.current', [i for i in range(45, 1342, 70)]), Send, WaitMode.Wait],
    [tc.DownloadFile(115, '/telemetry.current', [i for i in range(46, 1342, 70)]), Send, WaitMode.Wait],
    [tc.DownloadFile(116, '/telemetry.current', [i for i in range(47, 1342, 70)]), Send, WaitMode.Wait],
    [tc.DownloadFile(117, '/telemetry.current', [i for i in range(48, 1342, 70)]), Send, WaitMode.Wait],
    [tc.DownloadFile(118, '/telemetry.current', [i for i in range(49, 1342, 70)]), Send, WaitMode.Wait],
    [tc.DownloadFile(119, '/telemetry.current', [i for i in range(50, 1342, 70)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],

    [tc.DownloadFile(120, '/telemetry.current', [i for i in range(51, 1342, 70)]), Send, WaitMode.Wait],
    [tc.DownloadFile(121, '/telemetry.current', [i for i in range(52, 1342, 70)]), Send, WaitMode.Wait],
    [tc.DownloadFile(122, '/telemetry.current', [i for i in range(53, 1342, 70)]), Send, WaitMode.Wait],
    [tc.DownloadFile(123, '/telemetry.current', [i for i in range(54, 1342, 70)]), Send, WaitMode.Wait],
    [tc.DownloadFile(124, '/telemetry.current', [i for i in range(55, 1342, 70)]), Send, WaitMode.Wait],
    [tc.DownloadFile(125, '/telemetry.current', [i for i in range(56, 1342, 70)]), Send, WaitMode.Wait],
    [tc.DownloadFile(126, '/telemetry.current', [i for i in range(57, 1342, 70)]), Send, WaitMode.Wait],
    [tc.DownloadFile(127, '/telemetry.current', [i for i in range(58, 1342, 70)]), Send, WaitMode.Wait],
    [tc.DownloadFile(128, '/telemetry.current', [i for i in range(59, 1342, 70)]), Send, WaitMode.Wait],
    [tc.DownloadFile(129, '/telemetry.current', [i for i in range(60, 1342, 70)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],

    [tc.DownloadFile(130, '/telemetry.current', [i for i in range(61, 1342, 70)]), Send, WaitMode.Wait],
    [tc.DownloadFile(131, '/telemetry.current', [i for i in range(62, 1342, 70)]), Send, WaitMode.Wait],
    [tc.DownloadFile(132, '/telemetry.current', [i for i in range(63, 1342, 70)]), Send, WaitMode.Wait],
    [tc.DownloadFile(133, '/telemetry.current', [i for i in range(64, 1342, 70)]), Send, WaitMode.Wait],
    [tc.DownloadFile(134, '/telemetry.current', [i for i in range(65, 1342, 70)]), Send, WaitMode.Wait],
    [tc.DownloadFile(135, '/telemetry.current', [i for i in range(66, 1342, 70)]), Send, WaitMode.Wait],
    [tc.DownloadFile(136, '/telemetry.current', [i for i in range(67, 1342, 70)]), Send, WaitMode.Wait],
    [tc.DownloadFile(137, '/telemetry.current', [i for i in range(68, 1342, 70)]), Send, WaitMode.Wait],
    [tc.DownloadFile(138, '/telemetry.current', [i for i in range(69, 1342, 70)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]