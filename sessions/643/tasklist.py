tasks = [
    # Generated on 2019-03-12 20:06:59.743000, contains telemetry from sessions 642 to 643.
    # The session starts on 2019-03-12 21:20:54+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.previous', [2161, 2211, 2261, 2186, 2236, 2174, 2224, 2274, 2198, 2248, 2168, 2218, 2268, 2180, 2230, 2192, 2242, 2204, 2254]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [31, 81, 6, 56, 44, 94, 18, 68, 38, 88, 0, 50, 100, 12, 62, 24, 74]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]