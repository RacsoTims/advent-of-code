$data = Get-Content -Path "C:\Users\Gebruiker\Downloads\advent2018_day1.txt"
# Write-Host $data.GetType()

# PART 1
$frequency = 0
$frequencies = @()

$iteration = 0

:times While($True) {
    Foreach($shift in $data){
        # Write-Host $shift.GetType()   # output type is 'System.String'
        # Write-Host $iteration
        $direction = $shift[0]
        [int]$magnitude = $shift.Substring(1)

        if ($direction -eq "+"){
            $frequency += $magnitude
        }
        else {
            $frequency -= $magnitude
        }
        # PART 2
        if ($frequencies.Contains($frequency)){
            Write-Host $frequency
            Break times
        }
        else {
            $frequencies += $frequency
        }
    $iteration++
    $frequency
    }
}
Write-Host $frequency

# PART 2
