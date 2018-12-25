tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    # Telemetry between session 135 and 136
    [tc.DownloadFile(3, '/telemetry.current', [i for i in range(330, 530, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(4, '/telemetry.current', [i for i in range(336, 530, 12)]), Send, WaitMode.Wait],

    [tc.DownloadFile(5, '/telemetry.current', [i for i in range(333, 530, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(6, '/telemetry.current', [i for i in range(339, 530, 12)]), Send, WaitMode.Wait],

    # Remove files
    [tc.RemoveFile(10, '/p10_480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(11, '/p4_480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(12, '/p9_480_0'), Send, WaitMode.Wait],

    [tc.ListFiles(13, '/'), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 15], SendLoop, WaitMode.NoWait],
]