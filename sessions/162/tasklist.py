tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 7], SendLoop, WaitMode.NoWait],
    [[tc.SendBeacon(), 15], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    # Remove fully downloaded photos
    # 11 downloaded and removed
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.RemoveFile(13, '/sail.photo_13'), Send, WaitMode.NoWait],
    [tc.RemoveFile(15, '/sail.photo_15'), Send, WaitMode.NoWait],
    # 17 and 19 downloaded and removed
    [tc.RemoveFile(21, '/sail.photo_21'), Send, WaitMode.NoWait],
    [tc.RemoveFile(23, '/sail.photo_23'), Send, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.RemoveFile(25, '/sail.photo_25'), Send, WaitMode.NoWait],
    [tc.RemoveFile(27, '/sail.photo_27'), Send, WaitMode.NoWait],
    [tc.RemoveFile(29, '/sail.photo_29'), Send, WaitMode.NoWait],
    # 31 and 33 have few missings
    [tc.RemoveFile(35, '/sail.photo_35'), Send, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.RemoveFile(37, '/sail.photo_37'), Send, WaitMode.NoWait],
    [tc.RemoveFile(39, '/sail.photo_39'), Send, WaitMode.NoWait],
    [tc.RemoveFile(41, '/sail.photo_41'), Send, WaitMode.NoWait],
    [tc.RemoveFile(43, '/sail.photo_43'), Send, WaitMode.NoWait],
    # 45 downloaded and removed
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.RemoveFile(47, '/sail.photo_47'), Send, WaitMode.NoWait],
    [tc.RemoveFile(49, '/sail.photo_49'), Send, WaitMode.NoWait],
    [tc.RemoveFile(51, '/sail.photo_51'), Send, WaitMode.NoWait],
    [tc.RemoveFile(53, '/sail.photo_53'), Send, WaitMode.NoWait],
    # 55 downloaded and removed
    [tc.RemoveFile(57, '/sail.photo_57'), Send, WaitMode.NoWait],

    # Remove black photos (covered by solar panels)
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.RemoveFile(234, '/sail.photo_60'), Send, WaitMode.NoWait],
    [tc.RemoveFile(236, '/sail.photo_64'), Send, WaitMode.NoWait],
    [tc.RemoveFile(237, '/sail.photo_66'), Send, WaitMode.NoWait],
    [tc.RemoveFile(238, '/sail.photo_68'), Send, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.RemoveFile(239, '/sail.photo_70'), Send, WaitMode.NoWait],
    [tc.RemoveFile(240, '/sail.photo_72'), Send, WaitMode.NoWait],
    [tc.RemoveFile(242, '/sail.photo_74'), Send, WaitMode.NoWait],
    [tc.RemoveFile(243, '/sail.photo_76'), Send, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.RemoveFile(244, '/sail.photo_78'), Send, WaitMode.NoWait],
    [tc.RemoveFile(245, '/sail.photo_80'), Send, WaitMode.NoWait],
    [tc.RemoveFile(246, '/sail.photo_82'), Send, WaitMode.NoWait],
    [tc.RemoveFile(247, '/sail.photo_84'), Send, WaitMode.NoWait],
    [tc.RemoveFile(248, '/sail.photo_86'), Send, WaitMode.NoWait],

    [[tc.SendBeacon(), 15], SendLoop, WaitMode.NoWait],
]