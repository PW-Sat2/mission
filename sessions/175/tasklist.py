tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    # Telemetry between session 174 and 175
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.DownloadFile(10, '/telemetry.current', [i for i in range(360, 1700, 72)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.DownloadFile(11, '/telemetry.current', [i for i in range(372, 1700, 72)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.DownloadFile(12, '/telemetry.current', [i for i in range(384, 1700, 72)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    ["Go/no-go for uplink/downlink?", Print, WaitMode.Wait],
    ["Perform SADS experiment.", Print, WaitMode.Wait],

    ["The next step is beacon.", Print, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    ["List files at the end of the experiment", Print, WaitMode.Wait],
    [tc.ListFiles(100, '/'), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],

    ["More Telemetry between session 174 and 175 - run only when you're sure that hi-res photo is saved", Print, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.DownloadFile(20, '/telemetry.current', [i for i in range(408, 1700, 72)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.DownloadFile(21, '/telemetry.current', [i for i in range(420, 1700, 72)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.DownloadFile(22, '/telemetry.current', [i for i in range(432, 1700, 72)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
