# URL: https://adventofcode.com/2016/day/1

$x = 0; $y = 0  # oorsprong
$windrichting = @("N", "E", "S", "W")
$direction = 0

$raw = Get-Content -Path ".\data-day1.txt"
$clean = $raw.Split(", ")

$coordinates = $null

forEach($segment in $clean){
    # Write-Host $direction
    $turn = $segment[0]
    [int]$steps = $segment.Substring(1, ($segment.Length) - 1)

switch ($turn) {
    "L"{
        $direction -= 1
        if($direction -eq -1){
            $direction = 3
        }
    }
    "R"{
        $direction += 1
        if($direction -eq 4){
            $direction = 0
        }
    }
}

switch ($windrichting[$direction]){
    "N"{
        $y += $steps
    }
    "E"{
        $x += $steps
    }
    "S"{
        $y -= $steps
    }
    "W"{
        $x -= $steps
    }
}
$coordinate = $x, $y
$coordinates += , $coordinate
# Write-Host $turn, $direction, $windrichting[$direction], $steps, $x, $y
}

# $result = $null
# # Write-Host $coordinates
# ForEach($pair in $coordinates){
#     if ($coordinates.Contains($pair)){
#         $result += , $pair
#     }
# }

$totaal = [Math]::Abs($x) + [Math]::Abs($y)
Write-Host "x:"$x, "y:"$y, "Totaal gelopen: $totaal"
