tasks = [
    # Generated on 2021-02-03 11:33:18.768000, contains telemetry from sessions 5092 to 5093.
    # The session starts on 2021-02-03 12:27:42+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(31, '/telemetry.previous', [2169, 2219, 2269, 2194, 2244, 2182, 2232, 2206, 2256, 2176, 2226, 2276, 2188, 2238, 2200, 2250, 2212, 2262]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [39, 89, 14, 64, 2, 52, 102, 26, 76, 46, 96, 8, 58, 20, 70, 32, 82]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]