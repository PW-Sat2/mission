tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Remove SADS experiment files
    [tc.RemoveFile(10, '/sads.exp'), Send, WaitMode.NoWait],
    [tc.RemoveFile(11, '/sads.photo_wing'), Send, WaitMode.Wait],

    # Remove SADS experiment files once again
    [tc.RemoveFile(20, '/sads.exp'), Send, WaitMode.NoWait],
    [tc.RemoveFile(21, '/sads.photo_wing'), Send, WaitMode.Wait],

    [tc.ListFiles(100, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],
]
