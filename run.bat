:loop
    call gitbook install
    call node "plugins/gitbook-plugin-pwsat/summary.js"
    call gitbook serve
    echo "Restarting GitBook server..."
goto loop
