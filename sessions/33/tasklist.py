tasks = [
    [[tc.SetBitrate(79, 1), 3], SendLoop, WaitMode.NoWait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(150, '/'), Send, WaitMode.Wait],

    # Telemetry between session 32 and 33
    [tc.DownloadFile(32, '/telemetry.current', [i for i in range(600, 800, 25)]), Send, WaitMode.Wait],

    # Missing SunS experiment chunks
    [tc.DownloadFile(42, '/suns_1', [150, 151, 200, 75, 76, 77, 78, 79]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/suns_1', [80, 81, 82, 84, 94, 95, 103, 249]), Send, WaitMode.Wait],

    [[tc.SetBitrate(89, 8), 3], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],

    [tc.DownloadFile(42, '/suns_1', [80]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],
]
