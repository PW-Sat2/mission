1. Włącz ANTs LCL przez EPS_A
2. Delay 10 sekund
3. Reset kontrolera A anten
4. Delay 60 sekund
5. Arm kontrolera A anten
6. Delay 60 sekund
7. Automated antenna deployment (30s per antenna)
8. Delay 180 sekund
9. Disarm kontrolera A anten
10. Wyłącz ANTs LCL przez EPS_A
11. Delay 120 sekund

`for ANTENNA in [1, 2, 3, 4]:`
1. Włącz ANTs LCL przez EPS_A
2. Delay 10 sekund
3. Reset kontrolera A anten
4. Delay 60 sekund
5. Arm kontrolera A anten
6. Delay 60 sekund
7. Manual antenna `$ANTENNA` deployment with switches override (30s)
8. Delay 90 sekund
9. Disarm kontrolera A anten
10. Wyłącz ANTs LCL przez EPS_A
11. Delay 120 sekund


Identyczna procedura dla strony B (EPS B oraz kontroler B anten), wykonywana po zakończeniu strony A:

1. Włącz ANTs LCL przez EPS_B
2. Delay 10 sekund
3. Reset kontrolera B anten
4. Delay 60 sekund
5. Arm kontrolera B anten
6. Delay 60 sekund
7. Automated antenna deployment (30s per antenna)
8. Delay 180 sekund
9. Disarm kontrolera B anten
10. Wyłącz ANTs LCL przez EPS_B
11. Delay 120 sekund

`for ANTENNA in [1, 2, 3, 4]:`
1. Włącz ANTs LCL przez EPS_B
2. Delay 10 sekund
3. Reset kontrolera B anten
4. Delay 60 sekund
5. Arm kontrolera B anten
6. Delay 60 sekund
7. Manual antenna `$ANTENNA` deployment with switches override (30s)
8. Delay 90 sekund
9. Disarm kontrolera B anten
10. Wyłącz ANTs LCL przez EPS_B
11. Delay 120 sekund
