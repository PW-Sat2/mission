tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    # Telemetry between session 125 and 126
    [tc.DownloadFile(10, '/telemetry.current', [i for i in range(0, 1150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(11, '/telemetry.current', [i for i in range(25, 1150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(12, '/telemetry.previous', [i for i in range(2250, 2280, 2)]), Send, WaitMode.Wait],
    [tc.DownloadFile(13, '/telemetry.previous', [i for i in range(2251, 2280, 2)]), Send, WaitMode.Wait],

    # Low res photos download
    [tc.DownloadFile(20, '/p1_128_0', [6]), Send, WaitMode.Wait],
    [tc.DownloadFile(21, '/p2_128_0', [1, 2, 4, 5, 6, 7, 8]), Send, WaitMode.Wait],
    [tc.DownloadFile(22, '/p3_128_0', [6]), Send, WaitMode.Wait],
    [tc.DownloadFile(23, '/p4_128_0', [0, 1, 2]), Send, WaitMode.Wait],
    [tc.DownloadFile(24, '/p5_128_0', [i for i in range(0, 8, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(25, '/p6_128_0', [i for i in range(0, 9, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(26, '/p7_128_0', [i for i in range(0, 8, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(27, '/p8_128_0', [i for i in range(0, 7, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(28, '/p9_128_0', [i for i in range(0, 7, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(29, '/p10_128_0', [i for i in range(0, 7, 1)]), Send, WaitMode.Wait],

    # More telemetry between session 125 and 126
    [tc.DownloadFile(30, '/telemetry.current', [i for i in range(12, 1150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [i for i in range(37, 1150, 50)]), Send, WaitMode.Wait],

    [tc.DownloadFile(32, '/telemetry.current', [i for i in range(6, 1150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [i for i in range(18, 1150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [i for i in range(31, 1150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [i for i in range(43, 1150, 50)]), Send, WaitMode.Wait],

    # First high res photos download
    [tc.DownloadFile(40, '/p1_480_0', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/p1_480_0', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/p1_480_0', [i for i in range(40, 67, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(43, '/p2_480_0', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/p2_480_0', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/p2_480_0', [i for i in range(40, 64, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(46, '/p3_480_0', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/p3_480_0', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/p3_480_0', [i for i in range(40, 52, 1)]), Send, WaitMode.Wait],

    # Missing telemetry between session 124 and 125
    [tc.DownloadFile(70, '/telemetry.previous', [2071, 2072, 2074, 2075, 2076, 2077, 2078, 2079, 2080, 2081, 2083, 2084, 2086, 2087, 2089, 2090]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/telemetry.previous', [2091, 2092, 2093, 2095, 2096, 2098, 2099, 2101, 2102, 2103, 2104, 2105, 2107, 2108, 2110, 2111]), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/telemetry.previous', [2113, 2114, 2115, 2116, 2117, 2119, 2120, 2122, 2123, 2124, 2125, 2126, 2128, 2129, 2131, 2132]), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/telemetry.previous', [2134, 2135, 2137, 2138, 2139, 2140, 2141, 2143, 2144, 2146, 2147, 2149, 2150, 2152, 2153, 2155]), Send, WaitMode.Wait],
    [tc.DownloadFile(74, '/telemetry.previous', [2156, 2158, 2159, 2161, 2162, 2164, 2165, 2167, 2168, 2170, 2171, 2173, 2174, 2175, 2176, 2177]), Send, WaitMode.Wait], 
    [tc.DownloadFile(75, '/telemetry.previous', [2179, 2180, 2182, 2183, 2185, 2186, 2188, 2189, 2191, 2192, 2194, 2195, 2197, 2198, 2199, 2200]), Send, WaitMode.Wait],
    [tc.DownloadFile(76, '/telemetry.previous', [2201, 2202, 2203, 2204, 2206, 2207, 2209, 2210, 2211, 2212, 2213, 2215, 2216, 2218, 2219, 2220]), Send, WaitMode.Wait],
    [tc.DownloadFile(77, '/telemetry.previous', [2221, 2222, 2224, 2225, 2226, 2227, 2228, 2229, 2230, 2231, 2233, 2234, 2236, 2237, 2238, 2239]), Send, WaitMode.Wait], 
    [tc.DownloadFile(78, '/telemetry.previous', [2240, 2241, 2242, 2243, 2244, 2245, 2246, 2248, 2249]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]