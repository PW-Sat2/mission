tasks = [
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],

    # Delay the automatic reboot for entire week
    [tc.little_oryx.DelayRebootToNormal(10, 82), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]