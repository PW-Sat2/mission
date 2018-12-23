tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    # Telemetry between session 121 and 122
    [tc.DownloadFile(11, '/telemetry.current', [i for i in range(880, 1072, 12)]), Send, WaitMode.Wait],

    # RadFET exp data
    [tc.DownloadFile(20, '/radfet_6', [i for i in range(0, 16, 1)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(30, '/'), Send, WaitMode.Wait],

    # Previous telemetry
    [tc.DownloadFile(100, '/telemetry.previous', [i for i in range(1733, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(101, '/telemetry.previous', [i for i in range(1734, 2280, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],

    # More telemetry between session 121 and 122
    [tc.DownloadFile(102, '/telemetry.current', [i for i in range(881, 1072, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(103, '/telemetry.current', [i for i in range(882, 1072, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(104, '/telemetry.current', [i for i in range(883, 1072, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(105, '/telemetry.current', [i for i in range(884, 1072, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(106, '/telemetry.current', [i for i in range(885, 1072, 12)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(107, '/telemetry.current', [i for i in range(886, 1072, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(108, '/telemetry.current', [i for i in range(887, 1072, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(109, '/telemetry.current', [i for i in range(888, 1072, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(110, '/telemetry.current', [i for i in range(889, 1072, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(111, '/telemetry.current', [i for i in range(810, 1072, 12)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],

    # Missing from previous session
    [tc.DownloadFile(112, '/telemetry.current', [11, 26, 28, 32, 46, 48, 78, 82, 96, 98, 105, 128, 132, 146, 148, 178, 182, 196, 198, 199]), Send, WaitMode.Wait],
    [tc.DownloadFile(113, '/telemetry.current', [205, 210, 224, 228, 232, 246, 248, 278, 282, 296, 298, 311, 328, 332, 346, 348, 355, 541, 546, 548, 552, 578, 582]), Send, WaitMode.Wait],
    [tc.DownloadFile(114, '/telemetry.current', [378, 382, 391, 396, 398, 410, 411, 428, 432, 441, 446, 448, 462, 478, 482, 493, 496, 498, 510, 528, 532, 536]), Send, WaitMode.Wait],
    [tc.DownloadFile(115, '/telemetry.current', [596, 598, 607, 617, 621, 628, 632, 646, 648, 652, 655, 678, 682, 696, 698, 705, 710, 711, 728, 732, 746]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(116, '/telemetry.current', [748, 755, 760, 778, 782, 796, 798, 801, 805, 828, 832, 843, 846, 848, 855, 860, 878, 882, 896, 898]), Send, WaitMode.Wait],
    [tc.DownloadFile(117, '/telemetry.previous', [1710, 1716, 1721, 1723, 1775, 1783, 1785, 1787, 1800, 1845, 1849, 1870, 1880, 1881, 1884, 1905, 1913, 1915, 1919, 1926, 1940, 1975]), Send, WaitMode.Wait],
    [tc.DownloadFile(118, '/telemetry.previous', [1980, 1983, 2010, 2022, 2045, 2055, 2080, 2090, 2096, 2125, 2171, 2195, 2230, 2232, 2239, 2262, 2265, 2277]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
]