# ADVENT OF CODE 2023, DAY 2, PART 2
# URL: https://adventofcode.com/2023/day/2#part2

# OPDRACHT: For each game, find the minimum set of cubes that must have been present.
# What is the sum of the power of these sets?

$data = Get-Content -Path "C:\Users\Gebruiker\projects\powershell\advent-of-code\data\2023_day2_data.txt"

# here we will store the information pertaining to each game in useful way
$games = @{}

# here we will keep track of the sum of powers of cube sets
$sum_powers = 0

$counter = 1

:Games ForEach ($line in $data){
    $reds = @()
    $greens = @()
    $blues = @()

    $parts = $line -split ": |, |; "

    ForEach ($part in $parts){
        if ($part -eq $parts[0]){
            continue
        }
        else {
            [int]$number = $part.Split(" ")[0]
            $colour = $part.Split(" ")[1]

            if ($colour -eq "red"){
                $reds += $number
            }
            # elseif ($colour -eq "red" -and $number -gt $r){
            #     continue Games
            #     $counter += 1
            # }
            elseif ($colour -eq "green"){
                $greens += $number
            }
            # elseif ($colour -eq "green" -and $number -gt $g){
            #     continue Games
            #     $counter += 1
            # }
            elseif ($colour -eq "blue"){
                $blues += $number
            }
            # elseif ($colour -eq "blue" -and $number -gt $b){
            #     continue Games
            #     $counter += 1
            # }
        }
    }
    $r_minimum = $reds | Measure-Object -Maximum | Select-Object -ExpandProperty Maximum
    $g_minimum = $greens | Measure-Object -Maximum | Select-Object -ExpandProperty Maximum
    $b_minimum = $blues | Measure-Object -Maximum | Select-Object -ExpandProperty Maximum
    $power = $r_minimum * $g_minimum * $b_minimum

    $sum_powers += $power
    $games[$counter] = @($reds, $greens, $blues)
    $counter += 1
}

$games
# $possible = ($games.Keys).Count
Write-Host "Sum of powers: $sum_powers"
