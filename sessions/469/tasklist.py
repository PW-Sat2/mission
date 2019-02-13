tasks = [
    # Generated on 2019-02-13 21:53:51.518000, contains telemetry from sessions 466 to 469.
    # The session starts on 2019-02-14 10:07:39+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.previous', [1970, 2020, 2070, 2120, 2170, 2220, 2270, 1995, 2045, 2095, 2145, 2195, 2245, 1983, 2033, 2083, 2133, 2183, 2233, 2007]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [40, 90, 140, 190, 240, 290, 340, 390, 440, 490, 540, 590, 640, 690, 740, 790, 840, 890, 940, 990]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1040, 1090, 1140, 15, 65, 115, 165, 215, 265, 315, 365, 415, 465, 515, 565, 615, 665, 715, 765, 815]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [865, 915, 965, 1015, 1065, 1115, 1165, 3, 53, 103, 153, 203, 253, 303, 353, 403, 453, 503, 553, 603]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [653, 703, 753, 803, 853, 903, 953, 1003, 1053, 1103, 1153, 27, 77, 127, 177, 227, 277, 327, 377, 427]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.previous', [2057, 2107, 2157, 2207, 2257, 1977, 2027, 2077, 2127, 2177, 2227, 2277, 1989, 2039, 2089, 2139, 2189, 2239, 2001, 2051]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [477, 527, 577, 627, 677, 727, 777, 827, 877, 927, 977, 1027, 1077, 1127, 1177, 47, 97, 147, 197, 247]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [297, 347, 397, 447, 497, 547, 597, 647, 697, 747, 797, 847, 897, 947, 997, 1047, 1097, 1147, 9, 59]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [109, 159, 209, 259, 309, 359, 409, 459, 509, 559, 609, 659, 709, 759, 809, 859, 909, 959, 1009, 1059]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [1109, 1159, 21, 71, 121, 171, 221, 271, 321, 371, 421, 471, 521, 571, 621, 671, 721, 771, 821, 871]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.previous', [2101, 2151, 2201, 2251, 2013, 2063, 2113, 2163, 2213, 2263]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [921, 971, 1021, 1071, 1121, 1171, 33, 83, 133, 183, 233, 283, 333, 383, 433, 483, 533, 583, 633, 683]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.current', [733, 783, 833, 883, 933, 983, 1033, 1083, 1133]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]