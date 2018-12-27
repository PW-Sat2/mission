tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate1200), 5], SendLoop, WaitMode.NoWait],
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],

    # ReadMemory, weird telecommands
    [tc.ReadMemory(2, 0x8801b620, 248), Send, WaitMode.Wait], # scrubbing
    [tc.ReadMemory(3, 0x88017fe8, 8), Send, WaitMode.Wait], # _bootTime value

    [tc.SendBeacon(), Send, WaitMode.Wait], # Wait until good communication
    [tc.RawI2C(4, 0, 0x35, 1, [0xE0]), Send, WaitMode.Wait],

    [tc.PingTelecommand(), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Set 9600
    [tc.SetBitrate(6, BaudRate.BaudRate9600), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ReadMemory(7, 0x88017fe8, 8), Send, WaitMode.Wait], # _bootTime value

    [tc.ListFiles(8, '/'), Send, WaitMode.Wait],

    # Telemetry between session 145 and 147
    [tc.DownloadFile(10, '/telemetry.current', [i for i in range(30, 1100, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(11, '/telemetry.current', [i for i in range(55, 1100, 50)]), Send, WaitMode.Wait],

    [tc.DownloadFile(12, '/telemetry.current', [i for i in range(42, 1100, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(13, '/telemetry.current', [i for i in range(67, 1100, 50)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]