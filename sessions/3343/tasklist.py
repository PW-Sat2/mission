tasks = [
    # Generated on 2020-05-01 23:09:13.390000, contains telemetry from sessions 3342 to 3343.
    # The session starts on 2020-05-02 00:24:38+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [7, 57, 107, 157, 207, 32, 82, 132, 182, 20, 70, 120, 170, 220, 44, 94, 144, 194, 14, 64]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [114, 164, 214, 26, 76, 126, 176, 226, 38, 88, 138, 188, 50, 100, 150, 200]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [tc.DownloadFile(42, '/a1w_480_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/a1n_480_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/a2w_480_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/a2n_480_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/a3w_480_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/a3n_480_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/a4w_480_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/a4n_480_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(100, '/a5w_480_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(101, '/a5n_480_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(102, '/a6w_480_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(103, '/a6n_480_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(104, '/a7w_480_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(105, '/a7n_480_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(106, '/a8w_480_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(107, '/a8n_480_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(108, '/a9w_480_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(109, '/a9n_480_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(110, '/a10w_480_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(111, '/a10n_480_0', range(0, 20)), Send, WaitMode.Wait],

    [tc.DownloadFile(112, '/a1w_480_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(113, '/a1n_480_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(114, '/a2w_480_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(115, '/a2n_480_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(116, '/a3w_480_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(117, '/a3n_480_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(118, '/a4w_480_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(119, '/a4n_480_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(120, '/a5w_480_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(121, '/a5n_480_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(122, '/a6w_480_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(123, '/a6n_480_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(124, '/a7w_480_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(125, '/a7n_480_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(126, '/a8w_480_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(127, '/a8n_480_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(128, '/a9w_480_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(129, '/a9n_480_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(130, '/a10w_480_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(131, '/a10n_480_0', range(20, 40)), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]