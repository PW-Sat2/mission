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
    
    # Telemetry between session 197 and 204
    [tc.DownloadFile(40, '/telemetry.previous', [i for i in range(1460, 2280, 36)]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.previous', [i for i in range(1478, 2280, 36)]), Send, WaitMode.Wait],

    [tc.DownloadFile(42, '/telemetry.current', [i for i in range(0, 1828, 96)]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.current', [i for i in range(48, 1828, 96)]), Send, WaitMode.Wait],

    [tc.DownloadFile(44, '/telemetry.previous', [i for i in range(1466, 2280, 36)]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.previous', [i for i in range(1472, 2280, 36)]), Send, WaitMode.Wait],

    [tc.DownloadFile(46, '/telemetry.current', [i for i in range(24, 1828, 96)]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.current', [i for i in range(72, 1828, 96)]), Send, WaitMode.Wait],

    [tc.DownloadFile(48, '/telemetry.previous', [i for i in range(1484, 2280, 36)]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/telemetry.previous', [i for i in range(1490, 2280, 36)]), Send, WaitMode.Wait],

    [tc.DownloadFile(50, '/telemetry.current', [i for i in range(6, 1828, 96)]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.current', [i for i in range(12, 1828, 96)]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/telemetry.current', [i for i in range(18, 1828, 96)]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/telemetry.current', [i for i in range(30, 1828, 96)]), Send, WaitMode.Wait],

    [tc.DownloadFile(54, '/telemetry.current', [i for i in range(36, 1828, 96)]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/telemetry.current', [i for i in range(42, 1828, 96)]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/telemetry.current', [i for i in range(54, 1828, 96)]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/telemetry.current', [i for i in range(60, 1828, 96)]), Send, WaitMode.Wait],

    [tc.DownloadFile(58, '/telemetry.current', [i for i in range(66, 1828, 96)]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/telemetry.current', [i for i in range(78, 1828, 96)]), Send, WaitMode.Wait],
    [tc.DownloadFile(60, '/telemetry.current', [i for i in range(84, 1828, 96)]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/telemetry.current', [i for i in range(90, 1828, 96)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]