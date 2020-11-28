tasks = [
    # Generated on 2020-11-28 22:46:19.939000, contains telemetry from sessions 4692 to 4693.
    # The session starts on 2020-11-29 00:06:03+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(59, '/telemetry.current', [169, 219, 269, 319, 369, 194, 244, 294, 344, 182, 232, 282, 332, 382, 206, 256, 306, 356, 176, 226]), Send, WaitMode.Wait],
    [tc.DownloadFile(60, '/telemetry.current', [276, 326, 376, 188, 238, 288, 338, 388, 200, 250, 300, 350, 212, 262, 312, 362]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(45, '/w_p480_0_0', [160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171]), Send, WaitMode.Wait],
    # missing from previous session end


    ["Set bootslots for deep_sleep.", Print, WaitMode.Wait],
    [tc.SetBootSlots(200, 0b111000, 0b111), Send, WaitMode.Wait],

    # Wait for good uplink before power cycle
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS B
    [tc.PowerCycleTelecommand(3), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],

    [tc.little_oryx.Echo('PW-SAT2 has new software. More info: https://www.kplabs.pl/en/blog-en/case-study-little-oryx-2/'), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]