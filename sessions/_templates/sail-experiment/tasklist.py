tasks = [
    ["Tasklista operatora 1. Downlink na 1200.", Print, WaitMode.Wait],

    [tc.SetBitrate(1, BaudRate.BaudRate1200), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    ["Testowanie uplinku/downlinku na 5x DownloadFile (cid=3 do 7) i 6x SendBeacon.", Print, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.DownloadFile(3, '/telemetry.current', [i for i in range(0, 5, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.DownloadFile(4, '/telemetry.current', [i for i in range(0, 5, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.DownloadFile(5, '/telemetry.current', [i for i in range(0, 5, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.DownloadFile(6, '/telemetry.current', [i for i in range(0, 5, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.DownloadFile(7, '/telemetry.current', [i for i in range(0, 5, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    ["Powiedz go/no-go dla uplinku/downlinku.", Print, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],
]
