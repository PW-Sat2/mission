tasks = [
    # Generated on 2019-06-28 23:21:15.499000, contains telemetry from sessions 1372 to 1373.
    # The session starts on 2019-06-29 12:53:16+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # man-generated telemetry start
    [tc.DownloadFile(50, '/telemetry.current', [i for i in range(1206, 1400, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.current', [i for i in range(1212, 1400, 12)]), Send, WaitMode.Wait],

    # man-generated telemetry end

    [tc.DownloadFile(30, '/p10_240_0', [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/telemetry.current', [366, 894, 990]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]