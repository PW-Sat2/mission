tasks = [
    [tc.PingTelecommand(), Send, WaitMode.Wait],

    [tc.SetBitrate(1, BaudRate.BaudRate9600), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    # auto-generated telemetry end

    [tc.PerformSunSExperiment(3, 0, 20, 50, datetime.timedelta(seconds=5), 100, datetime.timedelta(seconds=20), 'suns_ps_10'), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]