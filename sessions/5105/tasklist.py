tasks = [
    # Generated on 2021-02-05 11:09:11.964118, contains telemetry from sessions 5104 to 5105.
    # The session starts on 2021-02-05 12:21:58+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(31, '/telemetry.current', [580, 630, 680, 730, 780, 605, 655, 705, 755, 593, 643, 693, 743, 617, 667, 717, 767, 587, 637, 687]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [737, 787, 599, 649, 699, 749, 611, 661, 711, 761, 623, 673, 723, 773]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    ,
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]