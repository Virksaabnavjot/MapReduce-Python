REM Locally test topTenCars mapper and reducer

REM Run mapper on 1st data split, output to file
type auto-mpg-data-original-split1.txt | topTenCarsMapper.py > topTenCarsMapper_output.txt

REM Run mapper on 2nd data split, append to the same file
type auto-mpg-data-original-split2.txt | topTenCarsMapper.py >> topTenCarsMapper_output.txt

REM View the output of the mappers (sorted)
type topTenCarsMapper_output.txt | sort

REM Run the reducer
type topTenCarsMapper_output.txt | sort | topTenCarsReducer.py

REM Run the reducer, output to file
type topTenCarsMapper_output.txt | sort | topTenCarsReducer.py > topTenCarsReducer_output.txt

REM Wait for user to press a key
PAUSE