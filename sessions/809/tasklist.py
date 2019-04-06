tasks = [
    # Generated on 2019-04-06 10:31:42.351000

     # Set bitrate
    [tc.SetBitrate(1, BaudRate.BaudRate9600), Send, WaitMode.Wait],

     # Get few beacons from nominal OBC
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # 10th RadFET Experiment
    [tc.PerformRadFETExperiment(10, 150, 110, 'radfet_10'), Send, WaitMode.Wait],

    [tc.ListFiles(5, '/'), Send, WaitMode.Wait],

     # Get beacons
    [[tc.SendBeacon(), 30], SendLoop, WaitMode.NoWait],
]