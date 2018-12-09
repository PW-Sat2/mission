tasks = [
    [[tc.SetBitrate(8, 1), 3], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(220, '/'), Send, WaitMode.Wait],

    # Power Cycle EPS controller A
    [tc.RawI2C(10, 0, 0x35, 1, [0xE0]), Send, WaitMode.Wait],
    # Power Cycle EPS controller B
    [tc.PowerCycleTelecommand(55), Send, WaitMode.Wait],

    [tc.PingTelecommand(), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [[tc.SetBitrate(9, 8), 3], SendLoop, WaitMode.NoWait],

    [tc.SendBeacon(), Send, WaitMode.Wait],
]
