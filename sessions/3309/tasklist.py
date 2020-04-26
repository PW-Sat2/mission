tasks = [
    # Generated on 2020-04-26 21:15:53.448000, contains telemetry from sessions 3307 to 3308.
    # The session starts on 2020-04-26 20:27:08+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(31, '/telemetry.current', [694, 744, 794, 844, 894, 944, 994, 1044, 1094, 1144, 1194, 1244, 1294, 1344, 1394, 719, 769, 819, 869, 919]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [969, 1019, 1069, 1119, 1169, 1219, 1269, 1319, 1369, 707, 757, 807, 857, 907, 957, 1007, 1057, 1107, 1157, 1207]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [1257, 1307, 1357, 1407, 731, 781, 831, 881, 931, 981, 1031, 1081, 1131, 1181, 1231, 1281, 1331, 1381, 701, 751]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [801, 851, 901, 951, 1001, 1051, 1101, 1151, 1201, 1251, 1301, 1351, 1401, 713, 763, 813, 863, 913, 963, 1013]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [1063, 1113, 1163, 1213, 1263, 1313, 1363, 725, 775, 825, 875, 925, 975, 1025, 1075, 1125, 1175, 1225, 1275, 1325]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [1375, 737, 787, 837, 887, 937, 987, 1037, 1087, 1137, 1187, 1237, 1287, 1337, 1387]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/telemetry.current', [650]), Send, WaitMode.Wait],
    # missing from previous session end


    # Carefully waste some session time
    [tc.SendBeacon(), Send, WaitMode.Wait],

    ["Set bootslots for deep_sleep.", Print, WaitMode.NoWait],
    [tc.SetBootSlots(103, 0b111000, 0b111), Send, WaitMode.Wait],

    # Wait for good uplink before power cycle
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS B
    [tc.PowerCycleTelecommand(3), Send, WaitMode.Wait],


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]