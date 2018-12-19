tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    # Telemetry between sessions 94 and 95
    [tc.DownloadFile(10, '/telemetry.current', [i for i in range(1700, 1900, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(11, '/telemetry.current', [i for i in range(1706, 1900, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(12, '/telemetry.current', [i for i in range(1703, 1900, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(13, '/telemetry.current', [i for i in range(1709, 1900, 12)]), Send, WaitMode.Wait],

    # Missing suns_5 chunks (still missing)
    [tc.DownloadFile(20, '/suns_5', [1, 13, 14, 95, 173, 202]), Send, WaitMode.Wait],
    [tc.DownloadFile(21, '/suns_5_sec', [55]), Send, WaitMode.Wait],

    # RadFET experiment data
    [tc.DownloadFile(22, '/radfet_4', [i for i in range(0, 16, 1)]), Send, WaitMode.Wait],

    # A few weird telecommands
    [tc.GetCompileInfoTelecommand(), Send, WaitMode.Wait],
    [tc.GetPersistentState(), Send, WaitMode.Wait],
    [tc.ReadMemory(23, 0x8809ec74, 4), Send, WaitMode.Wait], # Read memory to check RAM utilization before power cycle

    # More telemetry between sessions 94 and 95
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(30, '/telemetry.current', [i for i in range(1701, 1900, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [i for i in range(1702, 1900, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [i for i in range(1704, 1900, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [i for i in range(1705, 1900, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [i for i in range(1707, 1900, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [i for i in range(1708, 1900, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [i for i in range(1710, 1900, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [i for i in range(1711, 1900, 12)]), Send, WaitMode.Wait],

    # More telemetry between sessions 93 and 94
    [tc.DownloadFile(74, '/telemetry.current', [i for i in range(480, 1850, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(75, '/telemetry.current', [i for i in range(482, 1850, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(76, '/telemetry.current', [i for i in range(484, 1850, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(77, '/telemetry.current', [i for i in range(485, 1850, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(78, '/telemetry.current', [i for i in range(487, 1850, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(79, '/telemetry.current', [i for i in range(490, 1850, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(80, '/telemetry.current', [i for i in range(492, 1850, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(81, '/telemetry.current', [i for i in range(493, 1850, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(82, '/telemetry.current', [i for i in range(494, 1850, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(83, '/telemetry.current', [i for i in range(496, 1850, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(84, '/telemetry.current', [i for i in range(497, 1850, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(85, '/telemetry.current', [i for i in range(499, 1850, 50)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
