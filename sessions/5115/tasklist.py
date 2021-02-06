tasks = [
    # Generated on 2021-02-06 22:19:19.575141, contains telemetry from sessions 5114 to 5115.
    # The session starts on 2021-02-06 23:34:25+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(35, '/telemetry.previous', [2151, 2201, 2251, 2176, 2226, 2276, 2164, 2214, 2264, 2188, 2238, 2158, 2208, 2258, 2170, 2220, 2270, 2182, 2232, 2194]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [21, 71, 46, 34, 84, 8, 58, 28, 78, 40, 2, 52, 14, 64]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.previous', [2244]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    # remove old files
    [tc.RemoveFile(40, '/p0_n_p480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(41, '/p0_w_p480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(42, '/radfet_58'), Send, WaitMode.Wait],
    [tc.RemoveFile(43, '/radfet_59'), Send, WaitMode.Wait],

    # missing from previous session start

    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
