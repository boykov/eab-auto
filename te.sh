username="storage";
password="Nf1SkPeY";
sleep 2
echo user $username
sleep 1
echo pass $password
sleep 2
for (( j = 63; j <= 70; j++))
do
echo list $j
sleep 0.1
echo retr $j
sleep 1
# echo top $j
# sleep 0.2
done

echo quit
