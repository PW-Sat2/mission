tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    ["The next step is PowerCycleTelecommand", Print, WaitMode.Wait],
    [tc.PowerCycleTelecommand(3), Send, WaitMode.Wait],

    [tc.PingTelecommand(), Send, WaitMode.Wait],

    [tc.SetBitrate(4, BaudRate.BaudRate9600), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    ["The next step is EraseBootTableEntry.", Print, WaitMode.Wait],
    [tc.EraseBootTableEntry([3]), Send, WaitMode.Wait],
    [tc.EraseBootTableEntry([4]), Send, WaitMode.Wait],
    [tc.EraseBootTableEntry([5]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],

]
