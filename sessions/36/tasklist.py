tasks = [
    [[tc.SetBitrate(2, 1), 3], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(1, '/'), Send, WaitMode.Wait],

    # Telemetry between session 35 and 36
    [tc.DownloadFile(12, '/telemetry.current', [i for i in range(1750, 1950, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(13, '/telemetry.current', [i for i in range(1762, 1950, 25)]), Send, WaitMode.Wait],

    [tc.SetBitrate(3, 8), Send, WaitMode.Wait],

    # Missing telemetry current: session 35
    [tc.DownloadFile(14, '/telemetry.current', [1025, 775, 1550, 1712, 1062, 1575, 825, 850, 1112, 1625, 862, 1375, 875, 1162, 912]), Send, WaitMode.Wait],
    [tc.DownloadFile(15, '/telemetry.current', [1175, 925, 1700, 1075, 1200, 1737, 1725, 1525, 962, 1475, 1225, 975, 1250, 1012, 762, 1125]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],
]
