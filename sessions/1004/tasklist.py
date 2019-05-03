tasks = [
    # Generated on 2019-04-05 18:11:42.351000

     # Get beacons from deep-sleep
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],

     # Wake-up from deep-sleep
    [tc.PingTelecommand(), Send, WaitMode.Wait],

     # Set bitrate
    [tc.SetBitrate(1, BaudRate.BaudRate9600), Send, WaitMode.Wait],

     # Get few beacons from nominal OBC
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # 11th RadFET Experiment
    [tc.PerformRadFETExperiment(10, 150, 110, 'radfet_12'), Send, WaitMode.Wait],

    [tc.ListFiles(5, '/'), Send, WaitMode.Wait],

     # Get beacons from deep-sleep
    [[tc.SendBeacon(), 30], SendLoop, WaitMode.NoWait],
]