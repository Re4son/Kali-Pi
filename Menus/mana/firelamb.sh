#!/bin/bash
### BEGIN INIT INFO
# Provides:          firelamb
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Control firelamb
# Description:       Control firelamb
### END INIT INFO


## Adjust these
phy=wlan1
script=/usr/share/mana-toolkit/firelamb/firelamb.py
cmdline="/usr/bin/env python $script -i $phy"
## End adjustment

PROGLONG=$(realpath $script)
PROGSHORT=$(basename ${PROGLONG})
PIDFILE="/var/run/"${PIDFILE:-"${PROGSHORT}.pid"}

# Get the PID from PIDFILE if we don't have one yet.
if [[ -z "${PID}" && -e ${PIDFILE} ]]; then
  PID=$(cat ${PIDFILE});
fi

start() {
	echo "--------------------------------"
	echo "   STARTING $PROGSHORT"
	echo "--------------------------------"
	$cmdline & echo $! > ${PIDFILE}
}

stop() {

        echo "--------------------------------"
        echo "   STOPPING $PROGSHORT"
        echo "--------------------------------"
        if [[ -z "${PID}" ]]; then
            echo "${PROGSHORT} is not running (missing PID)."
        elif [[ -e "/proc/${PID}/cmdline" && "`tr -d '\0' < /proc/${PID}/cmdline`" == *"$script"* ]]; then
            kill $1 ${PID}
        else
            echo "${PROGSHORT} is not running (tested PID: ${PID})."
fi

}

case "$1" in
    start)
       start
       ;;
    stop)
       stop
       ;;
    restart)
       	stop
       	start
	;;
    force-reload)
	;;
    status)
        if [[ -z "${PID}" ]]; then
            echo "${PROGSHORT} is not running (missing PID)."
        elif [[ -e /proc/${PID}/cmdline && "`tr -d '\0' < /proc/${PID}/cmdline`" == *"$script"* ]]; then
            echo "${PROGSHORT} is running (PID: ${PID})."
            exit 1
        else
            echo "${PROGSHORT} is not running (tested PID: ${PID})."
            exit 0
        fi
        ;;
    *)
       echo "Usage: $0 {start|stop|status|restart}"
esac

