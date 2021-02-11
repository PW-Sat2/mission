tasks = [
    # Generated on 2021-02-11 12:09:09.762000, contains telemetry from sessions 5139 to 5140.
    # The session starts on 2021-02-11 13:21:40+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(34, '/telemetry.current', [497, 547, 597, 647, 697, 522, 572, 622, 672, 510, 560, 610, 660, 710, 534, 584, 634, 684, 504, 554]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [604, 654, 704, 516, 566, 616, 666, 528, 578, 628, 678, 540, 590, 640, 690]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/photo01w_0', [13, 15, 16, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/photo01w_0', [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/photo01w_0', [52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/photo01w_0', [70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]