$data = Get-Content -Path ".\Day2-test.txt"
Write-Host $data.Split(",")[0..4]