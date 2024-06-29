# URL: https://adventofcode.com/2017/day/2

$data = Get-Content -Path "C:\Users\Gebruiker\projects\powershell\advent\2017\data\day2.txt"
# $data
$checksum = 0
foreach ($line in $data){
    $numbers = @()
    foreach ($number in $line -split "\s+"){
        $numbers += [int]$number
    }
    $min = $numbers | Measure-Object -Minimum | Select-Object -ExpandProperty Minimum
    $max = $numbers | Measure-Object -Maximum | Select-Object -ExpandProperty Maximum
    $diff = $max - $min

    $checksum += $diff
}

# $checksum

# PART 2
$answer = 0
foreach ($line in $data){
    $numbers = @()
    foreach ($number in $line -split "\s+"){
        $numbers += [int]$number
    }
    # $numbers
    $ordered = $numbers | Sort-Object -Descending
:Division for ($i = 0; $i -le $ordered.Length; $i++){
        $num = $ordered[$i]
        foreach ($num1 in $ordered[($i+1)..($ordered.Length - 1)]){
            if ($num % $num1 -eq 0){
                $answer += $num / $num1
                break Division
            }
        }
    }
}

$answer
