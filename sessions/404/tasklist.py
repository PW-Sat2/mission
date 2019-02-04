tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(5, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.RemoveFile(206, '/p3_480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(208, '/p4_480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(209, '/p6_480_0'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.RemoveFile(210, '/p7_480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(211, '/p9_480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(212, '/p10_480_0'), Send, WaitMode.Wait],
   
    [tc.ListFiles(220, '/'), Send, WaitMode.Wait],    

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]