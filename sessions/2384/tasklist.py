tasks = [
    # Generated on 2019-12-06 20:52:05.976000, contains telemetry from sessions 2383 to 2384.
    # The session starts on 2019-12-06 22:02:14+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [2, 52, 102, 152, 202, 27, 77, 127, 177, 15, 65, 115, 165, 215, 39, 89, 139, 189, 9, 59]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [109, 159, 209, 21, 71, 121, 171, 221, 33, 83, 133, 183, 45, 95, 145, 195]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    
    # missing from previous session end

    # SunS ps 16
    [tc.PerformSunSExperiment(3, 0, 20, 250, datetime.timedelta(seconds=1), 15, datetime.timedelta(seconds=10), 'suns_ps_16'), Send, WaitMode.Wait],



    # auto-generated file download start
    [tc.DownloadFile(32, '/radfet_27', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]