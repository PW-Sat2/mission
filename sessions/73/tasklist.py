tasks = [
    [[tc.SetBitrate(6, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(7, '/'), Send, WaitMode.Wait],

    # Persistent state
    [tc.GetPersistentState(), Send, WaitMode.Wait],

    # Set periodic
    [tc.SetPeriodicMessageTelecommand(correlation_id=4, interval_minutes=1, repeat_count=1, message='We are the Borg.Lower your shields and surrender your ships.We will add your biological and technological distinctiveness to our own.Resistance is futile'), Send, WaitMode.Wait],

    # Persistent state
    [tc.GetPersistentState(), Send, WaitMode.Wait],

    # Telemetry between session 71 and 73
    [tc.DownloadFile(8, '/telemetry.current', [i for i in range(600, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(9, '/telemetry.current', [i for i in range(625, 1500, 50)]), Send, WaitMode.Wait],

    # More telemetry between session 71 and 73
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(10, '/telemetry.current', [i for i in range(612, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(11, '/telemetry.current', [i for i in range(637, 1500, 50)]), Send, WaitMode.Wait],

    [tc.DownloadFile(12, '/telemetry.current', [i for i in range(606, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(13, '/telemetry.current', [i for i in range(618, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(14, '/telemetry.current', [i for i in range(633, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(15, '/telemetry.current', [i for i in range(643, 1500, 50)]), Send, WaitMode.Wait],

    # Much more telemetry
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(20, '/telemetry.current', [i for i in range(603, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(21, '/telemetry.current', [i for i in range(609, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(22, '/telemetry.current', [i for i in range(615, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [i for i in range(621, 1500, 50)]), Send, WaitMode.Wait],

    [tc.DownloadFile(24, '/telemetry.current', [i for i in range(627, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(25, '/telemetry.current', [i for i in range(630, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(26, '/telemetry.current', [i for i in range(636, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(27, '/telemetry.current', [i for i in range(639, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(28, '/telemetry.current', [i for i in range(646, 1500, 50)]), Send, WaitMode.Wait],

    # Chunk by chunk
    [tc.DownloadFile(32, '/telemetry.current', [i for i in range(601, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [i for i in range(602, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [i for i in range(604, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [i for i in range(605, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [i for i in range(607, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [i for i in range(608, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [i for i in range(610, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [i for i in range(613, 1500, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(41, '/telemetry.current', [i for i in range(614, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.current', [i for i in range(616, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.current', [i for i in range(617, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.current', [i for i in range(619, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.current', [i for i in range(620, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.current', [i for i in range(622, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.current', [i for i in range(623, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.current', [i for i in range(624, 1500, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(49, '/telemetry.current', [i for i in range(626, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/telemetry.current', [i for i in range(627, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.current', [i for i in range(628, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/telemetry.current', [i for i in range(629, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/telemetry.current', [i for i in range(630, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/telemetry.current', [i for i in range(632, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/telemetry.current', [i for i in range(634, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/telemetry.current', [i for i in range(637, 1500, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(57, '/telemetry.current', [i for i in range(638, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/telemetry.current', [i for i in range(640, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/telemetry.current', [i for i in range(641, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(60, '/telemetry.current', [i for i in range(642, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/telemetry.current', [i for i in range(644, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/telemetry.current', [i for i in range(645, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/telemetry.current', [i for i in range(647, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/telemetry.current', [i for i in range(649, 1500, 50)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
