# Create the necessary files for a given year of 'Advent of Code' programming puzzles

$days = 25
if ((Read-Host "Current year? Yes (0) or No (1)") -eq "0") {
    $year = Get-Date -Format "yyyy"
}
else {
    $year = Read-Host "Enter year"
}

$folder = ".\$year"

try {
    Get-Item $folder -ErrorAction Stop
}
catch {
    New-Item $folder -ItemType Directory
}

$start = (Get-ChildItem "$folder\*input.txt" | Measure-Object).Count + 1

for ($day=$start; $day -le $days; $day++){
    $part1 = "day{0}.py" -f $day
    $part2 = "day{0}_part2.py" -f $day
    $puzzle_input = "day{0}_input.txt" -f $day
    $example = "day{0}_example.txt" -f $day
    
    $inputPart1 = (Get-Content ".\part1_common_text.txt" -Raw) -f $year, $day
    $inputPart2 = (Get-Content ".\part2_common_text.txt" -Raw) -f $year, $day
    
    Set-Content "$folder\$part1" -Value $inputPart1
    Set-Content "$folder\$part2" -Value $inputPart2
    New-Item $folder -Name $puzzle_input -ItemType File
    New-Item $folder -Name $example -ItemType File
}
