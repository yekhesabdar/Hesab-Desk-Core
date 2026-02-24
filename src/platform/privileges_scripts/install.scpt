on run {daemon_file, agent_file, user}

  set sh1 to "echo " & quoted form of daemon_file & " > /Library/LaunchDaemons/com.carriez.HesabDesk_service.plist && chown root:wheel /Library/LaunchDaemons/com.carriez.HesabDesk_service.plist;"

  set sh2 to "echo " & quoted form of agent_file & " > /Library/LaunchAgents/com.carriez.HesabDesk_server.plist && chown root:wheel /Library/LaunchAgents/com.carriez.HesabDesk_server.plist;"

  set sh3 to "cp -rf /Users/" & user & "/Library/Preferences/com.carriez.HesabDesk/HesabDesk.toml /var/root/Library/Preferences/com.carriez.HesabDesk/;"

  set sh4 to "cp -rf /Users/" & user & "/Library/Preferences/com.carriez.HesabDesk/HesabDesk2.toml /var/root/Library/Preferences/com.carriez.HesabDesk/;"

  set sh5 to "launchctl load -w /Library/LaunchDaemons/com.carriez.HesabDesk_service.plist;"

  set sh to sh1 & sh2 & sh3 & sh4 & sh5

  do shell script sh with prompt "HesabDesk wants to install daemon and agent" with administrator privileges
end run
