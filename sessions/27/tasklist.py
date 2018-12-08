tasks = [
    [[tc.SetBitrate(208, 1), 3], SendLoop, WaitMode.NoWait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(52, '/'), Send, WaitMode.Wait],

    # Telemetry between session 25 and 27
    [tc.DownloadFile(85, '/telemetry.current', [i for i in range(0, 450, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(86, '/telemetry.current', [i for i in range(16, 450, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(87, '/telemetry.current', [i for i in range(32, 450, 50)]), Send, WaitMode.Wait],

    [tc.SetBitrate(209, 1), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 15], SendLoop, WaitMode.NoWait],
]
