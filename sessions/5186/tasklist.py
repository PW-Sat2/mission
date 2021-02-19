tasks = [
    # Generated on 2021-02-19 22:27:11.061688, contains telemetry from sessions 5185 to 5186.
    # The session starts on 2021-02-19 23:31:53+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(31, '/telemetry.current', [888, 938, 988, 1038, 1088, 913, 963, 1013, 1063, 901, 951, 1001, 1051, 1101, 925, 975, 1025, 1075, 895, 945]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [995, 1045, 1095, 907, 957, 1007, 1057, 919, 969, 1019, 1069, 931, 981, 1031, 1081]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [tc.DownloadFile(100, '/p1_w_480', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(101, '/p1_w_480', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(102, '/p1_w_480', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    
    [tc.SendBeacon(), Send, WaitMode.Wait],
    
    [tc.DownloadFile(103, '/p1_n_480', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(104, '/p1_n_480', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(105, '/p1_n_480', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    
    [tc.SendBeacon(), Send, WaitMode.Wait],
    
    [tc.DownloadFile(106, '/p2_w_480', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(107, '/p2_w_480', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(108, '/p2_w_480', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    
    [tc.SendBeacon(), Send, WaitMode.Wait],
    
    [tc.DownloadFile(109, '/p2_n_480', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(110, '/p2_n_480', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(111, '/p2_n_480', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],


    # missing from previous session start
    ,
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]