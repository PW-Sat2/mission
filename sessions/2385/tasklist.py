tasks = [
    # Generated on 2019-12-06 23:19:49.472000, contains telemetry from sessions 2384 to 2385.
    # The session starts on 2019-12-06 23:40:30+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [173, 223, 273, 323, 373, 198, 248, 298, 348, 398, 186, 236, 286, 336, 386, 210, 260, 310, 360, 180]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [230, 280, 330, 380, 192, 242, 292, 342, 392, 204, 254, 304, 354, 216, 266, 316, 366]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]