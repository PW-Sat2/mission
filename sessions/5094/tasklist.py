tasks = [
    # Generated on 2021-02-03 13:09:52.228000, contains telemetry from sessions 5093 to 5094.
    # The session starts on 2021-02-03 14:00:50+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(31, '/telemetry.current', [62, 112, 162, 212, 262, 87, 137, 187, 237, 75, 125, 175, 225, 275, 99, 149, 199, 249, 69, 119]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [169, 219, 269, 81, 131, 181, 231, 93, 143, 193, 243, 105, 155, 205, 255]), Send, WaitMode.Wait],
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