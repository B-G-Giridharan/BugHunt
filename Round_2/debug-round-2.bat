@echo off
setlocal EnableExtensions EnableDelayedExpansion

set "ROOT=%cd%"
set "TARGET=%~1"
if "%TARGET%"=="" set "TARGET=questions"

set "SOLUTIONS=%ROOT%\%TARGET%"
set "TESTS=%ROOT%\tests"

if not exist "%SOLUTIONS%" (
    echo Missing folder: %SOLUTIONS%
    exit /b 1
)

if not exist "%TESTS%" (
    echo Missing folder: %TESTS%
    exit /b 1
)

powershell -NoProfile -ExecutionPolicy Bypass -Command "& { $root = '%ROOT%'; $target = '%TARGET%'; $solutions = $root + '\' + $target; $tests = $root + '\tests'; $total = 0; for ($n = 1; $n -le 5; $n++) { $name = ('q{0:d2}' -f $n); $script = $solutions + '\' + ('q{0:d2}.py' -f $n); $testFile = $tests + '\' + ('q{0:d2}.txt' -f $n); $filePass = $true; if (-not (Test-Path -LiteralPath $script)) { Write-Host ($name + ': missing script'); $filePass = $false } elseif (-not (Test-Path -LiteralPath $testFile)) { Write-Host ($name + ': missing test file'); $filePass = $false } else { foreach ($line in Get-Content -LiteralPath $testFile) { if ([string]::IsNullOrWhiteSpace($line)) { continue }; $parts = $line -split ':', 2; if ($parts.Count -lt 2) { $filePass = $false; continue }; $caseInput = $parts[0]; $expected = $parts[1]; $job = Start-Job -ScriptBlock { param($caseInput, $script) $caseInput | & py -3 $script 2>$null | Out-String } -ArgumentList $caseInput, $script; $job | Wait-Job -Timeout 10 | Out-Null; if ($job.State -eq 'Completed') { $actual = Receive-Job $job } else { $actual = 'timeout'; Stop-Job $job }; $actual = $actual.Trim(); if ($actual -cne $expected) { $filePass = $false } } }; if ($filePass) { $total++; Write-Host ($name + ': pass') } else { Write-Host ($name + ': fail') } }; Write-Host ('Total score: {0}/5' -f $total) }"

endlocal
pause