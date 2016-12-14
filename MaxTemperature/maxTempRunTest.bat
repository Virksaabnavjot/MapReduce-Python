REM Loccaly test MaxTemperature mapper and reducer

type sample.txt

type sample.txt | maxTempMapper.py

type sample.txt | maxTempMapper.py | sort

type sample.txt | maxTempMapper.py | sort | maxTempReducer.py

REM Wait for user to press a key
PAUSE