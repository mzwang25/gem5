
cat $1 \
	| grep "sim_seconds" \
	| grep -oE "[0-9]+\.[0-9]+" \
    | tr "\n" "," \
    | sed '$s/,$/\n/'

