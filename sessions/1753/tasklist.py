tasks = [
    # Generated on 2019-08-30 21:30:36.838000

    # Get beacons from deep-sleep
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],

    # Wake-up from deep-sleep
    [tc.PingTelecommand(), Send, WaitMode.Wait],

    # Set bitrate
    [tc.SetBitrate(1, BaudRate.BaudRate9600), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(5, '/'), Send, WaitMode.Wait],

    # suns experiment
    [tc.PerformSunSExperiment(3, 0, 20, 250, datetime.timedelta(seconds=3), 5, datetime.timedelta(seconds=10), 'suns_ps_12'), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
