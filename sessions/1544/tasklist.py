tasks = [
    # Generated on 2019-06-28 23:21:15.499000, contains telemetry from sessions 1372 to 1373.
    # The session starts on 2019-06-29 12:53:16+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [12, 62, 112, 162, 212, 37, 87, 137, 187, 25, 75, 125, 175, 225, 49, 99, 149, 199, 19, 69]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [119, 169, 219, 31, 81, 131, 181, 231, 43, 93, 143, 193, 55, 105, 155, 205]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # file download start
    # [TODO]
    # file download end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]