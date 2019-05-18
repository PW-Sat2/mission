tasks = [
    # Generated on 2019-05-18 12:13:00.126000, contains telemetry from sessions 1082 to 1083.
    # The session starts on 2019-05-18 13:23:38+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(31, '/telemetry.current', [184, 234, 284, 334, 384, 209, 259, 309, 359, 197, 247, 297, 347, 397, 221, 271, 321, 371, 191, 241]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [291, 341, 391, 203, 253, 303, 353, 403, 215, 265, 315, 365, 227, 277, 327, 377]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/p3_128_0', [0, 3, 5, 6, 8, 9, 12, 13, 14, 16, 20, 28, 31, 34]), Send, WaitMode.Wait],
    # missing from previous session end


    # file download start
    [tc.DownloadFile(100, '/p4_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(101, '/p5_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(102, '/p6_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(103, '/p7_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(104, '/p8_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(105, '/p9_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(106, '/p10_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    # file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]