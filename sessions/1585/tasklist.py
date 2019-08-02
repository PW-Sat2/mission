tasks = [

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    # auto-generated telemetry end

    [tc.PerformSunSExperiment(3, 0, 20, 250, datetime.timedelta(seconds=3), 40, datetime.timedelta(seconds=10), 'suns_ps_10'), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]