# URL: https://adventofcode.com/2023/day/4

$data = Get-Content -Path "C:\Users\Gebruiker\projects\powershell\advent\2023\data\day4.txt"
# $data
$score = 0

ForEach ($card in $data){
    # $identifier = $card.Split(": ")[0]
    $card_score = 0
    $numbers = $card.Split(": ")[1]
    # $identifier
    # $numbers
    $winning_numbers = @()
    $winning = ($numbers -split "\s+\|\s+")[0]     # $numbers -split "\s+\|\s+"
    $winning_numbers += $winning -split "\s+"
    $personal_numbers = @()
    $personal = ($numbers -split "\s+\|\s+")[1]
    $personal_numbers += $personal -split "\s+"
    # $numbers, $winning, $personal
    # $winning_numbers
    # $personal_numbers
    $wins = 0
    $personal_numbers
    foreach ($number in $personal_numbers){
        if ($winning_numbers -contains $number){
            $wins += 1
            Write-Host "Number is: $number, $wins"
        }
    }
    $wins
    if ($wins -gt 0){
    $card_score = [Math]::Pow(2, $wins-1)
    # Add-Content -Path "C:\Users\Gebruiker\projects\powershell\advent\2023\data\day4_output.txt" -Value $card_score
    $score += $card_score
    }
}

$score
