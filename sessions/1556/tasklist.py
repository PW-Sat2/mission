tasks = [
    # Generated on 2019-07-29 08:52:01.901000, contains telemetry from sessions 1553 to 1555.
    # The session starts on 2019-07-29 10:07:09+02:00.

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    # buffor to not wake up the sat accidentally 
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    
    # Get beacons from deep-sleep
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],

    # only in case it's not already in the deep sleep
    ["Set bootslots for deep_sleep.", Print, WaitMode.NoWait],
    [tc.SetBootSlots(103, 0b111000, 0b111), Send, WaitMode.Wait],

    # Wait for good uplink before power cycle
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS B
    [tc.PowerCycleTelecommand(3), Send, WaitMode.Wait],

    # Get beacons from deep-sleep
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
