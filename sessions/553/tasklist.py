tasks = [
    # Generated on 2019-02-26 23:03:53.738000, contains telemetry from sessions 551 to 553.
    # The session starts on 2019-02-27 09:31:59+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.previous', [2058, 2108, 2158, 2208, 2258, 2083, 2133, 2183, 2233, 2071, 2121, 2171, 2221, 2271, 2095, 2145, 2195, 2245, 2065, 2115]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [28, 78, 128, 178, 228, 278, 328, 378, 428, 478, 528, 578, 628, 678, 728, 778, 828, 878, 928, 978]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1028, 1078, 3, 53, 103, 153, 203, 253, 303, 353, 403, 453, 503, 553, 603, 653, 703, 753, 803, 853]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [903, 953, 1003, 1053, 41, 91, 141, 191, 241, 291, 341, 391, 441, 491, 541, 591, 641, 691, 741, 791]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [841, 891, 941, 991, 1041, 1091, 15, 65, 115, 165, 215, 265, 315, 365, 415, 465, 515, 565, 615, 665]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [715, 765, 815, 865, 915, 965, 1015, 1065, 35, 85, 135, 185, 235, 285, 335, 385, 435, 485, 535, 585]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.previous', [2165, 2215, 2265, 2077, 2127, 2177, 2227, 2277, 2089, 2139, 2189, 2239, 2101, 2151, 2201, 2251]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [635, 685, 735, 785, 835, 885, 935, 985, 1035, 1085, 47, 97, 147, 197, 247, 297, 347, 397, 447, 497]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [547, 597, 647, 697, 747, 797, 847, 897, 947, 997, 1047, 9, 59, 109, 159, 209, 259, 309, 359, 409]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [459, 509, 559, 609, 659, 709, 759, 809, 859, 909, 959, 1009, 1059, 21, 71, 121, 171, 221, 271, 321]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [371, 421, 471, 521, 571, 621, 671, 721, 771, 821, 871, 921, 971, 1021, 1071]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]