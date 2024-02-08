#!/bin/bash
# wait_for_db.sh

host="$1"
port="$2"
timeout="${3:-30}"

until nc -z "$host" "$port"; do
  >&2 echo "Waiting for $host:$port..."
  sleep 1
  timeout=$((timeout - 1))
  if [ $timeout -eq 0 ]; then
    >&2 echo "Timeout occurred while waiting for $host:$port"
    exit 1
  fi
done

>&2 echo "$host:$port is available"
alembic upgrade head &
python app.py
