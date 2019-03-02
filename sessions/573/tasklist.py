tasks = [
    # Generated on 2019-03-02 10:03:02.361000, contains telemetry from sessions 572 to 573.
    # The session starts on 2019-03-02 11:20:32+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.previous', [2124, 2174, 2224, 2274, 2149, 2199, 2249, 2137, 2187, 2237, 2161, 2211, 2261, 2131, 2181, 2231, 2143, 2193, 2243, 2155]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [44, 19, 7, 57, 31, 1, 51, 13, 63, 25, 37]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.previous', [2205, 2255, 2167, 2217, 2267]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [tc.DownloadFile(50, '/radfet_9', range(0, 8)), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/radfet_9', range(8, 16)), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/radfet_9', range(16, 24)), Send, WaitMode.Wait],
    
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]