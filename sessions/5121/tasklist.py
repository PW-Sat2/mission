tasks = [
    # Generated on 2021-02-07 23:04:27.585000, contains telemetry from sessions 5120 to 5121.
    # The session starts on 2021-02-08 00:17:23+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [295, 345, 395, 445, 495, 320, 370, 420, 470, 308, 358, 408, 458, 508, 332, 382, 432, 482, 302, 352]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [402, 452, 502, 314, 364, 414, 464, 514, 326, 376, 426, 476, 338, 388, 438, 488]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.RemoveFile(100, '/t01w_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(101, '/t01n_0'), Send, WaitMode.NoWait],

    [tc.RemoveFile(102, '/t02w_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(103, '/t02n_0'), Send, WaitMode.NoWait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]