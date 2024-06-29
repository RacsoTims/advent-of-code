# Function test

# $getal = 1

# function AddOne {
#     param (
#         [int]$getal
#     )
#     $getal = $getal + 1
# }

# AddOne -Getal $getal
# Write-Host $getal

# [2019] Puzzel 1
# URL: https://adventofcode.com/2019/day/1

# $data = Get-Content -Path ".\test.txt"

# $total = 0

# ForEach ($number in $data){

#     $number = ([Math]::Floor($number / 3) - 2)

#     $total += $number
# }

# Write-Host $total

$data = Get-Content -Path ".\testOfficialdata.txt"

$total = 0

:loop ForEach ($mass in $data){

    while ($mass -gt 0){
        $fuel = ([Math]::Floor($mass / 3) - 2)

        if ($fuel -le 0){
            continue loop
        }

        $total += $fuel

        $mass = $fuel
    }
    
}

Write-Host "De hoeveelheid brandstof die nodig is:$total"