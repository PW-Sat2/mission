tasks = [
    [[tc.SetBitrate(200, BaudRate.BaudRate1200), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(201, '/'), Send, WaitMode.Wait],

    # Telemetry download between session 41 and 43
    [tc.DownloadFile(202, '/telemetry.current', [i for i in range(0, 1000, 100)]), Send, WaitMode.Wait],
    [tc.DownloadFile(203, '/telemetry.previous', [i for i in range(2100, 2280, 50)]), Send, WaitMode.Wait],

    # First RadFET experiment triggering
    [tc.PerformRadFETExperiment(13, 150, 110, 'radfet'), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Goodbye satellite with 9600
    [[tc.SetBitrate(204, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
]
