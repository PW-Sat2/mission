tasks = [
    # Generated on 2019-09-20 22:57:40.973000, contains telemetry from sessions 1877 to 1878.
    # The session starts on 2019-09-21 00:05:50+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [166, 216, 266, 316, 366, 191, 241, 291, 341, 391, 179, 229, 279, 329, 379, 203, 253, 303, 353, 173]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [223, 273, 323, 373, 185, 235, 285, 335, 385, 197, 247, 297, 347, 209, 259, 309, 359]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [tc.DownloadFile(100, '/dummy_1_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]