tasks = [
    # Generated on 2020-12-27 12:33:50.650281, contains telemetry from sessions 4866 to 4867.
    # The session starts on 2020-12-27 13:51:52+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(40, '/telemetry.current', [477, 527, 577, 627, 677, 502, 552, 602, 652, 490, 540, 590, 640, 690, 514, 564, 614, 664, 484, 534]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [584, 634, 684, 496, 546, 596, 646, 696, 508, 558, 608, 658, 520, 570, 620, 670]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/telemetry.current', [24, 124, 130, 242, 248]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.previous', [1716, 2134, 2160, 2172]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/a_w_p480_11_32_0', [90, 108, 114, 140]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/a_w_p480_11_40_0', [55, 57, 81]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/a_w_p480_11_52_0', [29, 55, 57]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/a_w_p480_11_56_0', [67]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/a_w_p480_12_00_0', [19, 38]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/a_w_p480_12_04_0', [99, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/a_w_p480_12_04_0', [127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/a_w_p480_12_04_0', [145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start

    # auto-generated file download end


    # auto-generated file remove start

    # auto-generated file remove end
    [tc.SendBeacon(), Send, WaitMode.Wait],

    ["Set bootslots for deep_sleep.", Print, WaitMode.NoWait],
    [tc.SetBootSlots(200, 0b111000, 0b111), Send, WaitMode.Wait],

    # Wait for good uplink before power cycle
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS B
    [tc.PowerCycleTelecommand(3), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]