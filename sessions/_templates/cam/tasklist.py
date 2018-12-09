tasks = [
    [[tc.SetBitrate(5, 8), 3], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    # Telemetry between session 33 and 35
    [tc.DownloadFile(32, '/telemetry.current', [i for i in range(750, 1750, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [i for i in range(775, 1750, 50)]), Send, WaitMode.Wait],

    [tc.DownloadFile(34, '/telemetry.current', [i for i in range(762, 1750, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [i for i in range(787, 1750, 50)]), Send, WaitMode.Wait],
    
    [tc.SendBeacon(), Send, WaitMode.Wait],
]
