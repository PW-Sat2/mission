tasks = [
    # Generated on 2020-03-13 22:21:23.064000, contains telemetry from sessions 3023 to 3024.
    # The session starts on 2020-03-13 23:25:59+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [4, 54, 104, 154, 204, 29, 79, 129, 179, 229, 17, 67, 117, 167, 217, 41, 91, 141, 191, 11]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [61, 111, 161, 211, 23, 73, 123, 173, 223, 35, 85, 135, 185, 47, 97, 147, 197]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    
    # missing from previous session end


    # auto-generated file download start
    [tc.DownloadFile(7, '/radfet_34', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],

    # Low res photos download
    [tc.DownloadFile(100, '/p1_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(101, '/p2_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(102, '/p3_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(103, '/p4_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(104, '/p5_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(105, '/p6_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(106, '/p7_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(107, '/p8_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(108, '/p9_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(109, '/p10_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],

    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]