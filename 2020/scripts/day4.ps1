$text = Get-Content -Path "C:\Users\Gebruiker\Downloads\advent2020_day4_2.txt"

$data = $text.Split(" ")
$list = @()
$obj = [PSCustomObject]@{

}
$counter = 0

foreach($line in $data){

    if([string]::IsNullOrEmpty($line)){
        $list += $obj
        $obj = [PSCustomObject]@{

        }
    }else{
        $parts = $line.Split(":")
        $obj | Add-Member -NotePropertyName $parts[0] -NotePropertyValue $parts[1]
    }
}

$list += $obj

$valid_passport = @()

ForEach ($passport in $list){
    $fields = ($passport | Get-Member | Where-Object MemberType -eq NoteProperty | Measure-Object)

    if ($fields.Count -eq 8){
        $valid_passport += $passport
    }
    elseif ($fields.Count -eq 7) {
        if (($passport -match "cid") -eq $False){
            $valid_passport += $passport
        }
        else {
            Write-Host "Passport is not valid."
        }
    }
    else {
        Write-Host "Passport is not valid."
    }
}

ForEach ($passport in $valid_passport){

    $test_byr = $passport.byr
    if ([int]$test_byr -ge 1920 -and [int]$test_byr -le 2002){
        Write-Host $test_byr, valid
    }
    else {
        Write-Host $test_byr, not valid
    }
    # $test_ecl = ($passport.ecl)
    # $test_eyr = ($passport.eyr)
    # $test_hcl = ($passport.hcl)
    # $test_hgt = ($passport.hgt)
    # $test_iyr = ($passport.iyr)
    # $test_pid = ($passport.pid)

}

$counter