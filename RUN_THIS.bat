@ECHO OFF
cls
set local
# YOU WILL NEED TO SET THE PYTHON PATH manually on the next line... 
# point it to your installed python exe and remove the hashtag 
set PYTHONPATH=C:\Users\%USERNAME%\anaconda3\python.exe
set CURRPATH=%CD%

echo "Trying Basic Cars Export"
%PYTHONPATH% %CURRPATH%\basic_car_export.py
echo "Trying Full Car Export"
%PYTHONPATH% %CURRPATH%\full_car_export.py
echo "Trying Basic Track Export"
%PYTHONPATH% %CURRPATH%\basic_track_export.py
echo "Trying Full Track Export"
%PYTHONPATH% %CURRPATH%\full_track_export.py
echo "SCRIPT COMPLETED!!!"  
echo "Were there errors? Scroll up and find out... but hopefully not. If there were, try installing python setting the python path in the batch file, and run it again."
echo "If everything worked OK you'll have 4 CSV files in this folder now. "
pause