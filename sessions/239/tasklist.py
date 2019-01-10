tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate1200), 5], SendLoop, WaitMode.NoWait],
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],

    # ReadMemory, weird telecommands
    [tc.ReadMemory(2, 0x8801b620, 248), Send, WaitMode.Wait], # scrubbing

    # Wait until good communication
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS B
    [tc.PowerCycleTelecommand(3), Send, WaitMode.Wait],

    [tc.PingTelecommand(), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Set 9600
    [tc.SetBitrate(4, BaudRate.BaudRate9600), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(5, '/'), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(30, '/telemetry.current', [i for i in range(300, 1500, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [i for i in range(324, 1500, 48)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(32, '/telemetry.current', [i for i in range(312, 1500, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [i for i in range(336, 1500, 48)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(34, '/telemetry.current', [i for i in range(306, 1500, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [i for i in range(318, 1500, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [i for i in range(330, 1500, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [i for i in range(342, 1500, 48)]), Send, WaitMode.Wait],
    
    # High res photos download
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(60, '/p1_480_0', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/p1_480_0', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/p1_480_0', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/p1_480_0', [i for i in range(60, 80, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(64, '/p1_480_0', [i for i in range(80, 100, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/p1_480_0', [i for i in range(100, 120, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/p1_480_0', [i for i in range(120, 145, 1)]), Send, WaitMode.Wait],

    # Remove downloaded low res photos
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.RemoveFile(100, '/p1_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(101, '/p2_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(102, '/p3_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(103, '/p4_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(104, '/p5_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(105, '/p6_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(106, '/p7_128_0'), Send, WaitMode.NoWait],

    [tc.ListFiles(6, '/'), Send, WaitMode.Wait],
    
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(70, '/p2_480_0', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/p2_480_0', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/p2_480_0', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(73, '/p2_480_0', [i for i in range(60, 80, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(74, '/p2_480_0', [i for i in range(80, 100, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(75, '/p2_480_0', [i for i in range(100, 120, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(76, '/p2_480_0', [i for i in range(120, 136, 1)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(80, '/p3_480_0', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(81, '/p3_480_0', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(82, '/p3_480_0', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(83, '/p3_480_0', [i for i in range(60, 80, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(84, '/p3_480_0', [i for i in range(80, 100, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(85, '/p3_480_0', [i for i in range(100, 120, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(86, '/p3_480_0', [i for i in range(120, 140, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(87, '/p3_480_0', [i for i in range(140, 154, 1)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]