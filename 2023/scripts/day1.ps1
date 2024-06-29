# ADVENT OF CODE 2023, DAY 1
# URL: https://adventofcode.com/2023/day/1

$data = Get-Content -Path "C:\Users\Gebruiker\projects\powershell\advent-of-code\data\2023_day1_data.txt"
# $data = Get-Content -Path "C:\Users\Gebruiker\projects\powershell\advent-of-code\data\2023_day1_example.txt"

$total = 0
$calibration = @()

ForEach ($line in $data){
    $digits = @()
    ForEach ($char in $line[0..($line.Length - 1)]){
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