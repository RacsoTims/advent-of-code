# ADVENT OF CODE 2023, DAY 1, PART 2
# URL: https://adventofcode.com/2023/day/1#part2

$data = Get-Content -Path "C:\Users\Gebruiker\projects\powershell\advent-of-code\data\2023_day1_data.txt"
# $data = Get-Content -Path "C:\Users\Gebruiker\projects\powershell\advent-of-code\data\2023_day1_example.txt"

$total = 0
$calibration = @()
# four exceptions: 1) twone, 2) sevenine, 3)eightwo, 4) eighthree, 5) ight
$dict = [ordered]@{"twone" = 21; "sevenine" = 79; "eightwo" = 82; "eighthree" = 83; "oneight" = 18;
        "one" = 1; "two" = 2; "three" = 3; "four" = 4; "five" = 5; "six" = 6;
        "seven" = 7; "eight" = 8; "nine" = 9; "ight" = 8}

ForEach ($line in $data){
    $digits = @()

    # replace all numbers written as words with symbols
    ForEach($key in $dict.Keys){
        if ($line.Contains($key)){
            $line = $line.Replace($key, $dict[$key])
        }
    }
    # $line

    ForEach ($char in $line.ToCharArray()){
        if ($char -match "\d"){
            $digits += $char
        }
        }
    # Write-Host $digits, "digit"
    $first_and_last = [string]$digits[0] + [string]$digits[-1]
    $calibration += [int]$first_and_last
}

$calibration
ForEach ($number in $calibration){
    $total += $number
}

$total

# HOW TO LOOP THROUGH THE CHARACTERS WITHIN A STRING?