tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate1200), 5], SendLoop, WaitMode.NoWait],
    [[tc.SendBeacon(), 15], SendLoop, WaitMode.NoWait],

    # ReadMemory, weird telecommands
    [tc.ReadMemory(2, 0x8801b620, 248), Send, WaitMode.Wait], # scrubbing

    # Power cycle EPS B
    [tc.PowerCycleTelecommand(3), Send, WaitMode.Wait],
    [tc.PingTelecommand(), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Set 9600
    [tc.SetBitrate(6, BaudRate.BaudRate9600), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(7, '/'), Send, WaitMode.Wait],

    # Telemetry between session 171 and 173
    [tc.DownloadFile(10, '/telemetry.current', [i for i in range(0, 250, 12)]), Send, WaitMode.Wait],

    [tc.DownloadFile(11, '/telemetry.previous', [i for i in range(1450, 2280, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(12, '/telemetry.previous', [i for i in range(1474, 2280, 48)]), Send, WaitMode.Wait],

    [tc.DownloadFile(13, '/telemetry.previous', [i for i in range(1462, 2280, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(14, '/telemetry.previous', [i for i in range(1486, 2280, 48)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]