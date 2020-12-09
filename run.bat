@REM After adding the Bot token in the "discord_token.txt" file
@REM You can run this bot using this Batch(.bat) file

@echo off

echo Initialising...

@REM Installing the "requirements.txt" file automatically

pip install requirements.txt
pause

echo Running
python Cookie.py