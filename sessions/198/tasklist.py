tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate1200), 5], SendLoop, WaitMode.NoWait],
    [[tc.SendBeacon(), 15], SendLoop, WaitMode.NoWait],

    # ReadMemory, weird telecommands
    [tc.ReadMemory(2, 0x8801b620, 248), Send, WaitMode.Wait], # scrubbing

    # Power cycle EPS B
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.PowerCycleTelecommand(3), Send, WaitMode.Wait],
    [tc.PingTelecommand(), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Set 9600
    [tc.SetBitrate(6, BaudRate.BaudRate9600), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(7, '/'), Send, WaitMode.Wait],

    # Telemetry previous between session 191 and 197
    [tc.DownloadFile(10, '/telemetry.previous', [i for i in range(1280, 2280, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(11, '/telemetry.previous', [i for i in range(1304, 2280, 48)]), Send, WaitMode.Wait],

    [tc.DownloadFile(12, '/telemetry.previous', [i for i in range(1292, 2280, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(13, '/telemetry.previous', [i for i in range(1316, 2280, 48)]), Send, WaitMode.Wait],

    [tc.DownloadFile(14, '/telemetry.previous', [i for i in range(1286, 2280, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(15, '/telemetry.previous', [i for i in range(1298, 2280, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(16, '/telemetry.previous', [i for i in range(1310, 2280, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(17, '/telemetry.previous', [i for i in range(1322, 2280, 48)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]