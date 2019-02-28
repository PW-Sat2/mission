tasks = [
    # Generated on 2019-02-28 20:53:20.780000, contains telemetry from sessions 564 to 565.
    # The session starts on 2019-02-28 22:05:38+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(50, '/telemetry.current', [327, 377, 427, 477, 527, 352, 402, 452, 502, 340, 390, 440, 490, 540, 364, 414, 464, 514, 334, 384]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.current', [434, 484, 534, 346, 396, 446, 496, 546, 358, 408, 458, 508, 370, 420, 470, 520]), Send, WaitMode.Wait],
    # auto-generated telemetry end
    
    # Session 564 missings
    [tc.DownloadFile(30, '/telemetry.previous', [177, 227, 265, 277, 315, 327, 365, 377, 415, 427, 465, 477, 515, 527, 565, 577, 615]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.previous', [627, 665, 677, 715, 727, 765, 777, 815, 827, 865, 877, 915, 927, 965, 977, 1015, 1027]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.previous', [1065, 1077, 1115, 1127, 1165, 1177, 1215, 1227, 1265, 1277, 1315, 1327, 1365, 1377, 1415, 1427, 1465]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [1477, 1515, 1527, 1565, 1577, 1615, 1627, 1665, 1677, 1715, 1727, 1765, 1777, 1815, 1827, 1865, 1877]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.previous', [1915, 1927, 1965, 1977, 2015, 2027, 2065, 2077, 2115, 2127, 2165, 2177, 2215, 2227, 2265, 2277]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]