tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    # Telemetry between session 174 and 175
    [tc.SendBeacon(), Send, WaitMode.Wait],
    # [TODO]

    ["Go/no-go for uplink/downlink?", Print, WaitMode.Wait],
    ["Perform SADS experiment.", Print, WaitMode.Wait],

    # More Telemetry between session 174 and 175
    [tc.SendBeacon(), Send, WaitMode.Wait],
    # [TODO]
]
