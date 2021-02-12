tasks = [
    # Generated on 2021-02-12 11:09:49.912000, contains telemetry from sessions 5144 to 5145.
    # The session starts on 2021-02-12 12:27:07+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(34, '/telemetry.current', [749, 799, 849, 899, 949, 774, 824, 874, 924, 762, 812, 862, 912, 962, 786, 836, 886, 936, 756, 806]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [856, 906, 956, 768, 818, 868, 918, 780, 830, 880, 930, 792, 842, 892, 942]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/telemetry.current', [7, 19, 31, 57, 69, 81, 107, 119, 131, 157, 169, 181, 207, 219, 231, 257, 269]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [281, 307, 319, 331, 357, 369, 381, 407, 419, 431, 445, 457, 469, 481, 507, 519]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [531, 557, 569, 581, 607, 619, 631, 657, 669, 681, 707, 719, 731, 757, 769, 781]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [1861, 1911, 1961, 2011, 2025, 2037, 2049, 2061, 2099, 2111, 2149, 2161, 2199, 2211, 2249, 2261]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]