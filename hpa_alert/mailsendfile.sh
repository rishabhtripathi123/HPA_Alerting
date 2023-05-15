#!/bin/bash 
if [ -s output.txt ]; then
        mailx -a "output.txt" -s "HPA ALERT FOR PRODUCTION :- `TZ=":Asia/Kolkata" date '+DATE: %D'`" camerawithrishu@gmail.com <<< "This Alert is on `TZ=":Asia/Kolkata" date '+DATE: %D at: %T'` IST " 
fi

