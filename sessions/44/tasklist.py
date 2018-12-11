tasks = [
    [[tc.SetBitrate(200, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(201, '/'), Send, WaitMode.Wait],

    # Telemetry download between session 41 and 44
    [tc.DownloadFile(100, '/telemetry.current', [i for i in range(8, 1350, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(101, '/telemetry.current', [i for i in range(16, 1350, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(102, '/telemetry.current', [i for i in range(24, 1350, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(103, '/telemetry.current', [i for i in range(33, 1350, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(104, '/telemetry.current', [i for i in range(41, 1350, 50)]), Send, WaitMode.Wait],

    [tc.DownloadFile(105, '/telemetry.previous', [i for i in range(2106, 2280, 12)]), Send, WaitMode.Wait],

    # RadFET Experiment data download
    [tc.DownloadFile(106, '/radfet', [i for i in range(0, 16, 1)]), Send, WaitMode.Wait],

    # Last hi res photo
    [tc.DownloadFile(107, '/p2_480_0', [i for i in range(0, 15, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(108, '/p2_480_0', [i for i in range(15, 30, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(109, '/p2_480_0', [i for i in range(30, 45, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(110, '/p2_480_0', [i for i in range(45, 60, 1)]), Send, WaitMode.Wait],

    # Goodbye satellite
    [tc.SendBeacon(), Send, WaitMode.Wait],
]
