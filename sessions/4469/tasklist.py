tasks = [
    # verify that we're in normal mode
    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],
    
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    # wait for good communication
    [tc.SendBeacon(), Send, WaitMode.Wait],

    ["The next step is SetBootSlots.", Print, WaitMode.Wait],
    [tc.SetBootSlots(76, 0b111000, 0b111), Send, WaitMode.Wait],

    ["The next step is Power Cycle B.", Print, WaitMode.Wait],
    [tc.PowerCycleTelecommand(100), Send, WaitMode.Wait],

    ["The satellite shall boot to the new software.", Print, WaitMode.Wait],
    [tc.PingTelecommand(), Send, WaitMode.Wait],
    
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]