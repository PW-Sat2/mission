tasks = [
    [[tc.PingTelecommand(), 3], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(152, '/'), Send, WaitMode.Wait],

    # Telemetry between session 27 and 29
    [tc.DownloadFile(185, '/telemetry.current', [i for i in range(400, 1450, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(186, '/telemetry.current', [i for i in range(425, 1450, 50)]), Send, WaitMode.Wait],

    [tc.DownloadFile(187, '/telemetry.current', [i for i in range(408, 1450, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(189, '/telemetry.current', [i for i in range(416, 1450, 50)]), Send, WaitMode.Wait],

    [tc.DownloadFile(190, '/telemetry.current', [i for i in range(433, 1450, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(191, '/telemetry.current', [i for i in range(441, 1450, 50)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
