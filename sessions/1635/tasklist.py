tasks = [
    # Generated on 2019-08-11 12:20:54.242536, contains telemetry from sessions 1634 to 1635.
    # The session starts on 2019-08-11 13:21:51+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [543, 593, 643, 693, 743, 568, 618, 668, 718, 556, 606, 656, 706, 756, 580, 630, 680, 730, 550, 600]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [650, 700, 750, 562, 612, 662, 712, 762, 574, 624, 674, 724, 586, 636, 686, 736]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    ["Set bootslots for deep_sleep.", Print, WaitMode.NoWait],
    [tc.SetBootSlots(103, 0b111000, 0b111), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS B
    [tc.PowerCycleTelecommand(3), Send, WaitMode.Wait],

    # Get beacons from deep-sleep
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
