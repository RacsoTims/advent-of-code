# Create the necessary files for a given year of 'Advent of Code' programming puzzles

$rootFolder = "C:\Users\oscar\my_stuff\advent-of-code"
$days = 25
$year = Read-Host "Year"
$yearFolder = "$rootFolder\{0}" -f $year

try {
    Get-Item $yearFolder -ErrorAction Stop
}
catch {
    New-Item $yearFolder -ItemType Directory
}

$presentFiles = Get-ChildItem "$yearFolder\*input.txt" | Measure-Object
$start = $presentFiles.Count + 1

for ($day=$start; $day -le $days; $day++){
    $part1 = "day{0}.py" -f $day
    $part2 = "day{0}_part2.py" -f $day
    $puzzle_input = "day{0}_input.txt" -f $day
    $example = "day{0}_example.txt" -f $day
    
    $inputPart1 = (Get-Content "$rootFolder\part1-common-text.txt" -Raw) -f $year, $day
    $inputPart2 = (Get-Content "$rootFolder\part2-common-text.txt" -Raw) -f $year, $day
    
    Set-Content "$yearFolder\$part1" -Value $inputPart1
    Set-Content "$yearFolder\$part2" -Value $inputPart2
    New-Item $yearFolder -Name $puzzle_input -ItemType File
    New-Item $yearFolder -Name $example -ItemType File
}
