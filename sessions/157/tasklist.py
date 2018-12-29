tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate1200), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.DownloadFile(3, '/telemetry.current', [i for i in range(600, 605, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.DownloadFile(4, '/telemetry.current', [i for i in range(605, 610, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.DownloadFile(5, '/telemetry.current', [i for i in range(610, 615, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.DownloadFile(6, '/telemetry.current', [i for i in range(615, 620, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.DownloadFile(7, '/telemetry.current', [i for i in range(620, 625, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    ["Go/no-go for uplink/downlink?", Print, WaitMode.Wait],
]
