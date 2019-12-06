tasks = [
    # Get beacons from deep-sleep
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],

    # Wake-up from deep-sleep
    [tc.PingTelecommand(), Send, WaitMode.Wait],

    # Set bitrate
    [tc.SetBitrate(1, BaudRate.BaudRate9600), Send, WaitMode.Wait],

    # Get beacon
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    # 27th RadFET Experiment
    [tc.PerformRadFETExperiment(10, 150, 110, 'radfet_27'), Send, WaitMode.Wait],

    # Waste session time
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]