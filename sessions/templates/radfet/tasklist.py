tasks = [
    [tc.SetBitrate(1, 8), Send, WaitMode.NoWait],
    [tc.SetBitrate(2, 8), Send, WaitMode.NoWait],
    [tc.SetBitrate(3, 8), Send, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.ListFiles(4, '/'), Send, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(5, '/telemetry.current', [i for i in range(0, 500, 20)]), Send, WaitMode.Wait],
    # TBD more downloads
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.PerformRadFETExperiment(6, 50, 25, '/radfet'), Send,  WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.SetBitrate(7, 1), Send, WaitMode.NoWait],
    [tc.SetBitrate(8, 1), Send, WaitMode.NoWait],
    [tc.SetBitrate(9, 1), Send, WaitMode.NoWait],
]
