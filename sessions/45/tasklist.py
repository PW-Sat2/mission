tasks = [
    [[tc.SetBitrate(20, BaudRate.BaudRate1200), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(21, '/'), Send, WaitMode.Wait],

    # Telemetry download between session 41 and 44
    [tc.DownloadFile(22, '/telemetry.current', [i for i in range(1300, 1500, 25)]), Send, WaitMode.Wait],

    # RadFET Experiment data download
    [tc.DownloadFile(23, '/radfet', [i for i in range(0, 8, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(24, '/radfet', [i for i in range(8, 16, 1)]), Send, WaitMode.Wait],

    # Goodbye satellite with 1200
    [tc.SetBitrate(25, BaudRate.BaudRate9600), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
]
