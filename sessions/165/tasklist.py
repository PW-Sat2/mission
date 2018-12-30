tasks = [
    [[tc.SetBitrate(100, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [[tc.SendBeacon(), 15], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(101, '/'), Send, WaitMode.Wait],

    # Remove donwloaded photos
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.RemoveFile(1, '/sail.photo_1'), Send, WaitMode.NoWait],
    [tc.RemoveFile(3, '/sail.photo_3'), Send, WaitMode.NoWait],
    [tc.RemoveFile(5, '/sail.photo_5'), Send, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.RemoveFile(7, '/sail.photo_7'), Send, WaitMode.NoWait],
    [tc.RemoveFile(9, '/sail.photo_9'), Send, WaitMode.NoWait],
    [tc.RemoveFile(31, '/sail.photo_31'), Send, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.RemoveFile(66, '/sail.photo_66'), Send, WaitMode.NoWait],
    [tc.RemoveFile(73, '/sail.photo_73'), Send, WaitMode.NoWait],
    [tc.RemoveFile(75, '/sail.photo_75'), Send, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.RemoveFile(77, '/sail.photo_77'), Send, WaitMode.NoWait],
    [tc.RemoveFile(79, '/sail.photo_79'), Send, WaitMode.NoWait],
    [tc.RemoveFile(81, '/sail.photo_81'), Send, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.RemoveFile(83, '/sail.photo_83'), Send, WaitMode.NoWait],
    [tc.RemoveFile(85, '/sail.photo_85'), Send, WaitMode.NoWait],
    [tc.RemoveFile(99, '/sail.exp'), Send, WaitMode.NoWait],

    [[tc.SendBeacon(), 15], SendLoop, WaitMode.NoWait],
]