tasks = [
    [[tc.PingTelecommand(), 3], SendLoop, WaitMode.NoWait],
 
    [tc.SetBitrate(28, 1), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(22, '/'), Send, WaitMode.Wait],

    # Telemetry between session 23 and now
    [tc.DownloadFile(35, '/telemetry.current', [i for i in range(1050, 1250, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [i for i in range(1058, 1250, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [i for i in range(1066, 1250, 25)]), Send, WaitMode.Wait],

    [tc.SetBitrate(29, 8), Send, WaitMode.Wait],
    [tc.PingTelecommand(), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 15], SendLoop, WaitMode.NoWait],
]
