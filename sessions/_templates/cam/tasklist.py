tasks = [
    [[tc.SetBitrate(5, 1), 3], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    # Telemetry between session x and x
    [tc.DownloadFile(32, '/telemetry.current', [i for i in range(750, 1750, 50)]), Send, WaitMode.Wait],
    
    [tc.SetBitrate(3, 8), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],
]
