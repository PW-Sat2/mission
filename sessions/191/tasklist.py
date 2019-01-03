tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate1200), 5], SendLoop, WaitMode.NoWait],
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],

    # ReadMemory, weird telecommands
    [tc.ReadMemory(2, 0x8801b620, 248), Send, WaitMode.Wait], # scrubbing

    [tc.SendBeacon(), Send, WaitMode.Wait], # Wait until good communication
    [tc.RawI2C(4, 0, 0x35, 1, [0xE0]), Send, WaitMode.Wait],

    [tc.PingTelecommand(), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Set 9600
    [tc.SetBitrate(6, BaudRate.BaudRate9600), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(8, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.RemoveFile(100, '/p10_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(101, '/p1_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(102, '/p2_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(103, '/p3_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(104, '/p4_128_0'), Send, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.RemoveFile(105, '/p4_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(106, '/p7_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(107, '/p8_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(108, '/p8_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(109, '/p9_480_0'), Send, WaitMode.NoWait],

    

    # Telemetry previous starting in session 184
    [tc.DownloadFile(40, '/telemetry.previous', [i for i in range(1100, 2280, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.previous', [i for i in range(1124, 2280, 48)]), Send, WaitMode.Wait],

    [tc.DownloadFile(42, '/telemetry.previous', [i for i in range(1112, 2280, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.previous', [i for i in range(1136, 2280, 48)]), Send, WaitMode.Wait],

    [tc.DownloadFile(44, '/telemetry.previous', [i for i in range(1106, 2280, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.previous', [i for i in range(1118, 2280, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.previous', [i for i in range(1130, 2280, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.previous', [i for i in range(1142, 2280, 48)]), Send, WaitMode.Wait],

    [tc.ListFiles(50, '/'), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]