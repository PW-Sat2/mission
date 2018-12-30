tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(8, '/'), Send, WaitMode.Wait],

    # Telemetry between session 167 and 168
    [tc.DownloadFile(12, '/telemetry.current', [i for i in range(0, 20, 3)]), Send, WaitMode.Wait],
    [tc.DownloadFile(10, '/telemetry.previous', [i for i in range(2110, 2280, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(11, '/telemetry.previous', [i for i in range(2116, 2280, 12)]), Send, WaitMode.Wait],

    # Missing telemetry between session 164 and 13:00
    [tc.DownloadFile(30, '/telemetry.previous', [i for i in range(1090, 1300, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.previous', [i for i in range(1096, 1300, 12)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],

    # ======== If still in telemetry.current =========

    # Telemetry between session 167 and 168
    [tc.DownloadFile(40, '/telemetry.current', [i for i in range(2110, 2280, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [i for i in range(2116, 2280, 12)]), Send, WaitMode.Wait],

    # Missing telemetry between session 164 and 13:00
    [tc.DownloadFile(50, '/telemetry.current', [i for i in range(1090, 1300, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.current', [i for i in range(1096, 1300, 12)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]