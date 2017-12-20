python trend_data.py purchase litecoin > ltcdata.txt
tail ltcdata.txt > ltcdata2.txt
rm ltcdata.txt
head -8 ltcdata2.txt > ltcdata3.txt
rm ltcdata2.txt
tail -3 ltcdata3.txt > ltcdata4.txt
rm ltcdata3.txt 
python data_clean.py ltcdata4.txt > litecoin
python analyze.py litecoin >> finished
rm ltcdata4.txt
rm litecoin


