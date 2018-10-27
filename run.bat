:loop
    call gitbook install
    call gitbook serve
    echo "Restarting GitBook server..."
goto loop
