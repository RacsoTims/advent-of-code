# Create a file that shows my Advent of Code progress

$rootFolder = "C:\Users\oscar\my_stuff\advent-of-code"
$targetFile = "C:\Users\oscar\my_stuff\advent-of-code\progress.txt"

$startString = "ADVENT OF CODE PROGRESS OVERVIEW`n`nYear`t`t`tStars earned`t`t`tCompletion"
$testString = "Answer:`t0"

$maximumScore = 50
$adventOfCodeAge = 10
$scores = @()

Set-Content $targetFile -Value $startString

foreach ($year in Get-ChildItem $rootFolder -Directory) {
    $score = 0
    foreach ($day in Get-ChildItem "$year\day*.py") {
        $content = Get-Content $day -Raw
        if ($content -and (-not ($content.Contains($testString)))) {
            $score += 1
        }
    }
    $scores += $score
    $completion = [math]::Round($score/$maximumScore*100)
    $line = "`n$($year.Name)`t`t`t$score`t`t`t`t`t$score/$maximumScore ($completion%)"
    Add-Content $targetFile -Value $line
}

$totalScore = $scores | Measure-Object -Sum | Select-Object -ExpandProperty Sum
$totalCompletion = [math]::Round($totalScore/($maximumScore*$adventOfCodeAge)*100)
$endString = "`nTotal`t`t`t$totalScore`t`t`t`t`t$totalScore/$($maximumScore*$adventOfCodeAge) ($totalCompletion%)"
Add-Content $targetFile -Value $endString
