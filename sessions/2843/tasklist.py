tasks = [
    # Generated on 2020-02-15 11:15:43.495000, contains telemetry from sessions 2842 to 2843.
    # The session starts on 2020-02-15 12:11:36+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [3, 53, 103, 153, 203, 28, 78, 128, 178, 16, 66, 116, 166, 216, 40, 90, 140, 190, 10, 60]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [110, 160, 210, 22, 72, 122, 172, 222, 34, 84, 134, 184, 46, 96, 146, 196]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    
    # missing from previous session end


    # auto-generated file download start
    [tc.DownloadFile(7, '/radfet_32', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],

    [tc.DownloadFile(10, '/p0_480', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(11, '/p0_480', range(20, 40)), Send, WaitMode.Wait],

    [tc.DownloadFile(12, '/p1_480', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(13, '/p1_480', range(20, 40)), Send, WaitMode.Wait],

    [tc.DownloadFile(14, '/p2_480', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(15, '/p2_480', range(20, 40)), Send, WaitMode.Wait],

    [tc.DownloadFile(16, '/p3_480', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(17, '/p3_480', range(20, 40)), Send, WaitMode.Wait],

    [tc.DownloadFile(18, '/p4_480', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(19, '/p4_480', range(20, 40)), Send, WaitMode.Wait],

    [tc.DownloadFile(20, '/p5_480', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(21, '/p5_480', range(20, 40)), Send, WaitMode.Wait],

    [tc.DownloadFile(22, '/p6_480', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(23, '/p6_480', range(20, 40)), Send, WaitMode.Wait],

    [tc.DownloadFile(24, '/p7_480', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(25, '/p7_480', range(20, 40)), Send, WaitMode.Wait],

    [tc.DownloadFile(26, '/p8_480', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(27, '/p8_480', range(20, 40)), Send, WaitMode.Wait],

    [tc.DownloadFile(28, '/p9_480', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(29, '/p9_480', range(20, 40)), Send, WaitMode.Wait],


    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]