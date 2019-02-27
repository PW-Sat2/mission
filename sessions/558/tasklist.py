tasks = [
    # Generated on 2019-02-27 21:09:49.975496, contains telemetry from sessions 557 to 558.
    # The session starts on 2019-02-27 22:01:08+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.previous', [2247, 2272, 2260, 2254, 2266, 2278]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [17, 67, 117, 167, 42, 92, 142, 30, 80, 130, 180, 4, 54, 104, 154, 24, 74, 124, 174, 36]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [86, 136, 186, 48, 98, 148, 10, 60, 110, 160]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]