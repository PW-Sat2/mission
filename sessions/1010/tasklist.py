tasks = [
    # Generated on 2019-05-06 08:10:45.809000, contains telemetry from sessions 1008 to 1009.
    # The session starts on 2019-05-06 09:45:56+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.previous', [1747, 1797, 1847, 1897, 1947, 1997, 2047, 2097, 2147, 2197, 2247, 1772, 1822, 1872, 1922, 1972, 2022, 2072, 2122, 2172]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [17, 67, 117, 167, 217, 267, 317, 367, 417, 467, 517, 567, 42, 92, 142, 192, 242, 292, 342, 392]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.previous', [2222, 2272, 1760, 1810, 1860, 1910, 1960, 2010, 2060, 2110, 2160, 2210, 2260, 1784, 1834, 1884, 1934, 1984, 2034, 2084]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [442, 492, 542, 592, 30, 80, 130, 180, 230, 280, 330, 380, 430, 480, 530, 580, 4, 54, 104, 154]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.previous', [2134, 2184, 2234, 1754, 1804, 1854, 1904, 1954, 2004, 2054, 2104, 2154, 2204, 2254, 1766, 1816, 1866, 1916, 1966, 2016]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [204, 254, 304, 354, 404, 454, 504, 554, 604, 24, 74, 124, 174, 224, 274, 324, 374, 424, 474, 524]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [574, 36, 86, 136, 186, 236, 286, 336, 386, 436, 486, 536, 586, 48, 98, 148, 198, 248, 298, 348]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.previous', [2066, 2116, 2166, 2216, 2266, 1778, 1828, 1878, 1928, 1978, 2028, 2078, 2128, 2178, 2228, 2278, 1790, 1840, 1890, 1940]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [398, 448, 498, 548, 598, 10, 60, 110, 160, 210, 260, 310, 360, 410, 460, 510, 560]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.previous', [1990, 2040, 2090, 2140, 2190, 2240]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    [tc.DownloadFile(40, '/p4_480_0', [8, 11, 16, 17, 18, 21, 23, 41, 42, 43, 44, 45, 46, 49, 116, 117]), Send, WaitMode.Wait],
	[tc.DownloadFile(41, '/p4_480_0', [118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132]), Send, WaitMode.Wait],
	[tc.DownloadFile(42, '/p7_480_0', [71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88]), Send, WaitMode.Wait],
	[tc.DownloadFile(43, '/p7_480_0', [89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]), Send, WaitMode.Wait],
	[tc.DownloadFile(44, '/p7_480_0', [107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124]), Send, WaitMode.Wait],
	[tc.DownloadFile(45, '/p7_480_0', [125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142]), Send, WaitMode.Wait],

    # missing from previous session start
    
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end

    # Reboot to deep sleep
    # Generated on 2019-05-06 10:02:54.903000 (removed unneeded commands)

    # Carefully waste some session time
    [tc.SendBeacon(), Send, WaitMode.Wait],

    ["Set bootslots for deep_sleep.", Print, WaitMode.NoWait],
    [tc.SetBootSlots(103, 0b111000, 0b111), Send, WaitMode.Wait],

    # Wait for good uplink before power cycle
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS B
    [tc.PowerCycleTelecommand(3), Send, WaitMode.Wait],

    # Get beacons from deep-sleep
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]