tasks = [
    # Generated on 2019-08-03 12:21:49.143000, contains telemetry from sessions 1586 to 1587.
    # The session starts on 2019-08-03 13:19:41+02:00.

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


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]