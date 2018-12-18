tasks = [
    [[tc.SetBitrate(3, BaudRate.BaudRate1200), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.PowerCycleTelecommand(2), Send, WaitMode.Wait],

    [tc.PingTelecommand(), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Set 9600
    [tc.SetBitrate(1, BaudRate.BaudRate9600), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(4, '/'), Send, WaitMode.Wait],

    # Telemetry between session 90 and 91
    [tc.DownloadFile(5, '/telemetry.previous', [i for i in range(1700, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(6, '/telemetry.current', [i for i in range(0, 300, 25)]), Send, WaitMode.Wait],

    [tc.DownloadFile(7, '/telemetry.previous', [i for i in range(1725, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(8, '/telemetry.current', [i for i in range(12, 300, 25)]), Send, WaitMode.Wait],

    [tc.DownloadFile(9, '/telemetry.previous', [i for i in range(1712, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(10, '/telemetry.current', [i for i in range(6, 300, 25)]), Send, WaitMode.Wait],

    [tc.DownloadFile(11, '/telemetry.previous', [i for i in range(1737, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(12, '/telemetry.current', [i for i in range(18, 300, 25)]), Send, WaitMode.Wait],


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
