tasks = [
    # Generated on 2021-02-12 12:54:35.935000, contains telemetry from sessions 5145 to 5146.
    # The session starts on 2021-02-12 13:59:46+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(31, '/telemetry.current', [917, 967, 1017, 1067, 1117, 942, 992, 1042, 1092, 930, 980, 1030, 1080, 1130, 954, 1004, 1054, 1104, 924, 974]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1024, 1074, 1124, 936, 986, 1036, 1086, 948, 998, 1048, 1098, 960, 1010, 1060, 1110]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]