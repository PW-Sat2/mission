tasks = [
    [tc.PingTelecommand(), Send, WaitMode.Wait],

    [tc.SetBitrate(1, BaudRate.BaudRate9600), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    # auto-generated telemetry end

    # 19th RadFET Experiment
    [tc.PerformRadFETExperiment(10, 150, 110, 'radfet_19'), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]