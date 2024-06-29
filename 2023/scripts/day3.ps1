# URL: https://adventofcode.com/2023/day/3

# OPDRACHT: What is the sum of all of the part numbers in the engine schematic?

$data = Get-Content -Path "C:\Users\Gebruiker\projects\powershell\advent-of-code\data\2023_day3_example.txt"
$symbol = "(?!\d|\.)\W"  # regular expression for isolating 'symbols' - any character that is not a period (".") or a digit
$gear = "\*"
$sum = 0
$counter = 0
$Sum_gear_ratio = 0
for ($i=0; $i -lt $data.Length; $i++){
    $line = $data[$i]
    for ($j=0; $j -lt $line.Length; $j++){
        if ($line[$j] -match "\d+" -and !($line[$j-1] -match "\d+")){   # AND statement added so it only checks the starting digit
            $number = $line[$j]
            $size = 1
            while ($line[$j+$size] -match "\d+"){
                $number += $line[$j+$size]
                $size += 1
            }
            $adjacent_chars = @()
            for ($k = -1; $k -lt 2; $k++){
                # $row = $data[$i+$k]
                for ($l = -1; $l -le $size; $l++){
                    # $char = $row[$j+$l]
                    if ($i+$k -lt 0 -or $i+$k -gt ($data.Length - 1) -or $j+$l -lt 0 -or $j+$l -gt ($line.Length - 1)){
                        continue
                    }
                    else {
                        # Write-Host "Hi"
                        $row = $data[$i+$k]
                        $char = $row[$j+$l]
                        $adjacent_chars += $char
                    }
                }
            }
            # $adjacent_chars
            if ($adjacent_chars -match $symbol){
                $counter += 1
                $sum += [int]$number
            }
        }
        if ($line[$j] -match $gear){
            for ($m = -1; $m -le 2; $m++){
                for ($n = -3; $n -le 3; $n++){
                    if ($i+$m -lt 0 -or $i+$m -gt ($data.Length - 1)){
                        break
                    }
                    elseif ($j+$n -lt 0 -or $j+$n -gt ($line.Length - 1)) {
                        continue
                    }
                    else {
                        $gear_ratio = 1
                        $row = $data[$i+$m]
                        $char = $row[$j+$n]
                        if ($char -match "\d+" -and !($row[$j+$n-1] -match "\d+")){
                            [string]$number1 = $char
                            $size = 1
                            while ($row[$j+$n+$size] -match "\d+"){
                                $number1 += $row[$j+$n+$size]
                                $size += 1
                            }
                            $number1
                            # $gear_ratio *= [int]$number1
                        }
                    }
                }
            }
        }
        $Sum_gear_ratio += $gear_ratio
    }
}

$sum, $counter
$Sum_gear_ratio
# "Symbol" is any character that is not a period (".") or a digit.
