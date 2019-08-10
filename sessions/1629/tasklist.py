tasks = [
    # Generated on 2019-08-03 10:48:57.006000, contains telemetry from sessions 1585 to 1586.
    # The session starts on 2019-08-03 11:44:03+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [183, 233, 283, 333, 383, 208, 258, 308, 358, 196, 246, 296, 346, 396, 220, 270, 320, 370, 190, 240]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [290, 340, 390, 202, 252, 302, 352, 402, 214, 264, 314, 364, 226, 276, 326, 376]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end
    
    # file download start
    [tc.DownloadFile(144, '/radfet_19', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],
    
    [tc.DownloadFile(100, '/p1_128_0', [i for i in range(0, 33, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(101, '/p2_128_0', [i for i in range(0, 38, 1)]), Send, WaitMode.Wait],
    
    [tc.DownloadFile(102, '/p1_480_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(103, '/p1_480_0', [i for i in range(25, 50, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(104, '/p1_480_0', [i for i in range(50, 75, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(105, '/p1_480_0', [i for i in range(75, 100, 1)]), Send, WaitMode.Wait],

    [tc.ListFiles(121, '/'), Send, WaitMode.Wait],


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]