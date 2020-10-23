tasks = [
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.little_oryx.Reboot(), Send, WaitMode.Wait],

    [tc.little_oryx.DelayRebootToNormal(10, 7), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
