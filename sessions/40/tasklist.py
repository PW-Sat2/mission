tasks = [
    [[tc.SetBitrate(18, 1), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(22, '/'), Send, WaitMode.Wait],

    # Persistent state
    [tc.GetPersistentState(), Send, WaitMode.Wait],

    # Telemetry between session 39 and 40
    [tc.DownloadFile(14, '/telemetry.current', [i for i in range(1100, 2100, 100)]), Send, WaitMode.Wait],

    # Power Cycle EPS controller A
    [tc.RawI2C(10, 0, 0x35, 1, [0xE0]), Send, WaitMode.Wait],
    # Power Cycle EPS controller B
    [tc.PowerCycleTelecommand(88), Send, WaitMode.Wait],

    [tc.PingTelecommand(), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [[tc.SetBitrate(25, 8), 3], SendLoop, WaitMode.NoWait],

    [tc.SendBeacon(), Send, WaitMode.Wait],
]
