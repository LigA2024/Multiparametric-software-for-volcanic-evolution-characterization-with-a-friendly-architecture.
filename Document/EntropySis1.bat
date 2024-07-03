@echo off

REM "Shannon Entropy estimator for Characterization of Volcanic Seismic Signals"
REM  "Shannon Entropy estimator for Characterization of Volcanic Seismic Signals, Vers. 1.1"
REM  Granada University (Ugr).
REM  Granada, Spain. 2024.
REM  Developed by: Ligdamis A. Gutiérrez E. PhD.
Title Shannon Entropy estimator for Characterization of Volcanic Seismic Signals (Vers. 1.1)
color 1F
echo.
echo.
echo     ==============================================================================
echo     =                                                                            =
echo     =  Welcome to:                                                               =
echo     =                                                                            =
echo     = Shannon Entropy estimator for Characterization of Volcanic Seismic Signals =
echo     =                                   (Vers. 1.1)                              =
echo     =                   Theoretical Physics and Cosmos Department                =
echo     =           Signal Theory, Telematics and Communications Department          =
echo     =                        Andalusian Institute of Geophysics                  =
echo     =                              Granada University (Ugr)                      =
echo     =                                                                            =
echo     =                              Developed in Python 3.8.6                     =
echo     =                       Execution for Windows and Linux System               =
echo     =                               Granada, Spain. 2024                         =
echo     ==============================================================================
echo.            
echo        Please, Minimize the CMD from the Python.exe window (in black).
echo            (Don't close it, because the system also closes).           
echo        When you exit the system, this window closes automatically. 
echo.           
echo          	    To Continue, please press a key.
echo.
echo               *** Please, press a key to Start the System . ***        
echo.
pause>nul

CD "%USERPROFILE%\Documents\EntropySis1\"
cls
START python Menu1.py