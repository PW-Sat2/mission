tasks = [
    # Generated on 2019-04-05 21:21:02.361000

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    ["The next step is download RadFET experiment", Print, WaitMode.Wait],

    [tc.DownloadFile(40, '/radfet_12', range(0, 8)), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/radfet_12', range(8, 16)), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]