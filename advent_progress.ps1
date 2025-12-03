# Create a file that shows my Advent of Code progress

$targetFile = ".\progress.txt"

$header = "ADVENT OF CODE PROGRESS OVERVIEW`n`nYear`t`t`tStars earned`t`t`tCompletion"
$testString = "Answer:`t0"

$startingYear = 2015
$adventOfCodeAge = (Get-Date -Format "yyyy") - $startingYear + 1
$scores = @()

Set-Content $targetFile -Value $header

foreach ($year in Get-ChildItem -Directory) {
    $files = Get-ChildItem "$year\day*.py"
    $maximumScore = ($files | Measure-Object).Count
    $score = 0
    foreach ($day in $files) {
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
