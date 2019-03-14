tasks = [
    [[tc.SetBitrate(2, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [tc.PowerCycleTelecommand(1), Send, WaitMode.Wait],
    
    [tc.SetBitrate(150, BaudRate.BaudRate9600), Send, WaitMode.Wait],
    
    [tc.ListFiles(13, '/'), Send, WaitMode.Wait],
    
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]