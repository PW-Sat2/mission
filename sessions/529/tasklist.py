tasks = [
    # Generated on 2019-02-23 18:56:41.733096, contains telemetry from sessions 526 to 529.
    # The session starts on 2019-02-23 20:08:43+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    # ReadMemory, weird telecommands
    [tc.ReadMemory(2, 0x8801b620, 248), Send, WaitMode.Wait], # scrubbing

    # Wait until good communication
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS B
    [tc.PowerCycleTelecommand(3), Send, WaitMode.Wait],

    [tc.PingTelecommand(), Send, WaitMode.Wait],

    # Set 9600
    [tc.SetBitrate(4, BaudRate.BaudRate9600), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(5, '/'), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.previous', [2088, 2138, 2188, 2238, 2113, 2163, 2213, 2263, 2101, 2151, 2201, 2251, 2125, 2175, 2225, 2275, 2095, 2145, 2195, 2245]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [8, 58, 108, 158, 208, 258, 308, 358, 408, 458, 508, 558, 608, 658, 708, 758, 808, 858, 33, 83]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [133, 183, 233, 283, 333, 383, 433, 483, 533, 583, 633, 683, 733, 783, 833, 21, 71, 121, 171, 221]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [271, 321, 371, 421, 471, 521, 571, 621, 671, 721, 771, 821, 871, 45, 95, 145, 195, 245, 295, 345]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [395, 445, 495, 545, 595, 645, 695, 745, 795, 845, 15, 65, 115, 165, 215, 265, 315, 365, 415, 465]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [515, 565, 615, 665, 715, 765, 815, 865, 27, 77, 127, 177, 227, 277, 327, 377, 427, 477, 527, 577]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.previous', [2107, 2157, 2207, 2257, 2119, 2169, 2219, 2269, 2131, 2181, 2231]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [627, 677, 727, 777, 827, 39, 89, 139, 189, 239, 289, 339, 389, 439, 489, 539, 589, 639, 689, 739]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [789, 839, 1, 51, 101, 151, 201, 251, 301, 351, 401, 451, 501, 551, 601, 651, 701, 751, 801, 851]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    # Low res photos download
    [tc.DownloadFile(100, '/p1_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(101, '/p2_128_0', [i for i in range(0, 27, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(102, '/p3_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(103, '/p4_128_0', [i for i in range(0, 23, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(104, '/p5_128_0', [i for i in range(0, 18, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(105, '/p6_128_0', [i for i in range(0, 19, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(106, '/p7_128_0', [i for i in range(0, 22, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(107, '/p8_128_0', [i for i in range(0, 13, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(108, '/p9_128_0', [i for i in range(0, 17, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(109, '/p10_128_0', [i for i in range(0, 24, 1)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]