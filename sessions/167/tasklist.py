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

    # Telemetry between session 165 and 67
    [tc.DownloadFile(10, '/telemetry.current', [i for i in range(1276, 2250, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(11, '/telemetry.current', [i for i in range(1300, 2250, 48)]), Send, WaitMode.Wait],

    [tc.DownloadFile(12, '/telemetry.current', [i for i in range(1288, 2250, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(13, '/telemetry.current', [i for i in range(1312, 2250, 48)]), Send, WaitMode.Wait],

    [tc.DownloadFile(14, '/telemetry.current', [i for i in range(1281, 2250, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(15, '/telemetry.current', [i for i in range(1293, 2250, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(16, '/telemetry.current', [i for i in range(1306, 2250, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(17, '/telemetry.current', [i for i in range(1318, 2250, 48)]), Send, WaitMode.Wait],

    # Missing telemetry between session 156 and 158 - before sail exp
    [tc.DownloadFile(20, '/telemetry.previous', [i for i in range(576, 1000, 24)]), Send, WaitMode.Wait],
    [tc.DownloadFile(21, '/telemetry.previous', [i for i in range(588, 1000, 24)]), Send, WaitMode.Wait],

    [tc.DownloadFile(22, '/telemetry.previous', [i for i in range(582, 1000, 24)]), Send, WaitMode.Wait],
    [tc.DownloadFile(23, '/telemetry.previous', [i for i in range(594, 1000, 24)]), Send, WaitMode.Wait],


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]