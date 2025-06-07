@REM Clear terminal
cls

@REM Build apk
flet build apk ^
    --description "YouTube-Video downloader" ^
    --project "YT-Downloader" ^
    --product "YT-Downloader" ^
    --org "ajservers.site" ^
    --clear-cache ^
    --module-name main.py ^
    -v
