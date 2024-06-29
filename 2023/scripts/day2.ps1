# ADVENT OF CODE 2023, DAY 2, PART 1
# URL: https://adventofcode.com/2023/day/2

# OPDRACHT: what games would have been possible given the contents of the bag?
# Bag content: 12 red cubes, 13 green cubes, and 14 blue cubes.

$data = Get-Content -Path "C:\Users\Gebruiker\projects\powershell\advent-of-code\data\2023_day2_data.txt"

# number of cubes of each colour
$r = 12
$g = 13
$b = 14

# here we will store the information pertaining to each game in useful way
$games = @{}

# here we will keep track of the sum of valid game ID's
$sum = 0

$counter = 1

:Games ForEach ($line in $data){
    $reds = @()
    $greens = @()
    $blues = @()

    $parts = $line -split ": |, |; "

    ForEach ($part in $parts){
        if ($part -eq $parts[0]){
            $id = $part.Split(" ")[1]
        }
        else {
            [int]$number = $part.Split(" ")[0]
            $colour = $part.Split(" ")[1]

            if ($colour -eq "red" -and $number -le $r){
                $reds += $number
            }
            elseif ($colour -eq "red" -and $number -gt $r){
                continue Games
                $counter += 1
            }
            
            if ($colour -eq "green" -and $number -le $g){
                $greens += $number
            }
            elseif ($colour -eq "green" -and $number -gt $g){
                continue Games
                $counter += 1
            
            }
            if ($colour -eq "blue" -and $number -le $b){
                $blues += $number
            }
            elseif ($colour -eq "blue" -and $number -gt $b){
                continue Games
                $counter += 1
            }
        }
    }
    $sum += $id
    $games[$counter] = @($reds, $greens, $blues)
    $counter += 1
}

$games
$possible = ($games.Keys).Count
Write-Host "Possible games: $possible`nSum: $sum"
