tasks = [
    # Generated on 2021-02-05 12:35:40.300944, contains telemetry from sessions 5105 to 5106.
    # The session starts on 2021-02-05 13:54:49+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [746, 796, 846, 896, 946, 771, 821, 871, 921, 759, 809, 859, 909, 959, 783, 833, 883, 933, 753, 803]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [853, 903, 953, 765, 815, 865, 915, 777, 827, 877, 927, 789, 839, 889, 939]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]