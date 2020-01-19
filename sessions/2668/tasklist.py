tasks = [
    # Generated on 2020-01-19 12:06:20.916000, contains telemetry from sessions 2667 to 2668.
    # The session starts on 2020-01-19 12:58:04+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(40, '/telemetry.current', [364, 414, 464, 514, 564, 389, 439, 489, 539, 377, 427, 477, 527, 577, 401, 451, 501, 551, 371, 421]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [471, 521, 571, 383, 433, 483, 533, 583, 395, 445, 495, 545, 407, 457, 507, 557]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/p07w_480_0', [50, 53, 54, 72, 108, 109, 111, 123, 128, 129, 131]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/p08n_480_0', [23, 40, 45, 50, 78]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/p09n_480_0', [25, 26, 31, 94]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/p09w_480_0', [43, 44, 45, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/p09w_480_0', [70, 71, 72, 73, 74, 75, 76, 77, 80, 82, 124, 125, 126]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/p08w_480_0', [34, 35, 36, 37, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/p08w_480_0', [56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/p08w_480_0', [75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/p08w_480_0', [94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/p08w_480_0', [113, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]