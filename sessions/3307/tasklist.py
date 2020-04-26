tasks = [
    # Generated on 2020-04-26 13:03:07.722364, contains telemetry from sessions 3306 to 3307.
    # The session starts on 2020-04-26 14:19:54+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(31, '/telemetry.current', [519, 569, 619, 669, 719, 544, 594, 644, 694, 532, 582, 632, 682, 732, 556, 606, 656, 706, 526, 576]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [626, 676, 726, 538, 588, 638, 688, 738, 550, 600, 650, 700, 562, 612, 662, 712]), Send, WaitMode.Wait],
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