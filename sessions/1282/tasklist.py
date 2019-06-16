tasks = [
    # Generated on 2019-06-16 11:34:35.756000, contains telemetry from sessions 1281 to 1282.
    # The session starts on 2019-06-16 12:37:32+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(33, '/telemetry.current', [371, 421, 471, 521, 571, 396, 446, 496, 546, 384, 434, 484, 534, 584, 408, 458, 508, 558, 378, 428]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [478, 528, 578, 390, 440, 490, 540, 590, 402, 452, 502, 552, 414, 464, 514, 564]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/suns_ps_7', [1, 2, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/suns_ps_7', [34, 35, 36, 37, 38, 39, 45, 46, 47, 48, 49, 76, 77, 93, 94, 226]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/p2_480_0', [72, 73, 74, 77, 79, 80, 81, 82, 83, 84, 85]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]