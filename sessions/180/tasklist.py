tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    # Telemetry between session 179 and 180
    [tc.DownloadFile(30, '/telemetry.current', [i for i in range(550, 755, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [i for i in range(556, 755, 12)]), Send, WaitMode.Wait],

    # Low res photos download
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.DownloadFile(3, '/p1_128', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(5, '/p2_128', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(7, '/p3_128', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(9, '/p4_128', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(11, '/p5_128', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(13, '/p6_128', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(15, '/p7_128', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(17, '/p8_128', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(19, '/p9_128', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(21, '/p10_128', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],

    # Much more telemetry between session 176 and 179
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [i for i in range(6, 555, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [i for i in range(18, 555, 48)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.current', [i for i in range(30, 555, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.current', [i for i in range(42, 555, 48)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/telemetry.previous', [i for i in range(1806, 2280, 24)]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.previous', [i for i in range(1818, 2280, 24)]), Send, WaitMode.Wait],

    # More telemetry between session 179 and 180
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.DownloadFile(60, '/telemetry.current', [i for i in range(553, 755, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/telemetry.current', [i for i in range(559, 755, 12)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]