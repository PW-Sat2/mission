tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(20, '/telemetry.current', [1, 51, 101, 151, 201, 26, 76, 126, 176, 14, 64, 114, 164, 214, 38, 88, 138, 188, 8, 58]), Send, WaitMode.Wait],
    [tc.DownloadFile(21, '/telemetry.current', [108, 158, 208, 20, 70, 120, 170, 32, 82, 132, 182, 44, 94, 144, 194]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [tc.PerformRadFETExperiment(100, 150, 110, 'radfet_56'), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
