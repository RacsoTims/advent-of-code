# URL: https://adventofcode.com/2017/day/1

$data = Get-Content -Path "C:\Users\Gebruiker\projects\powershell\advent\2017\data\day1.txt"
# $data
# $asciiOfset = 48

foreach ($number in $data){
    $score = 0
    $step_size = [int]($number.Length / 10)

    for ($i=0; $i -lt $number.Length; $i++){
        $digit = [int]$number[$i].ToString()
        $next_digit = [int]$number[($i+$step_size) % ($number.Length)].ToString()
        
        if ($digit -eq $next_digit){
            $score += $digit
        }
    }
    Write-Host "Score:", $score
}

# PART 2
foreach ($number in $data){
    $score = 0
    $step_size = [int]($number.Length / 2)

    for ($i=0; $i -lt $number.Length; $i++){
        $digit = [int]$number[$i].ToString()
        $next_digit = [int]$number[($i+$step_size) % ($number.Length)].ToString()
        
        if ($digit -eq $next_digit){
            $score += $digit
        }
    }
    Write-Host "Score:", $score
}
