-------------------------------------------------------------------------------------------------------------------------------------------
Shannon Entropy estimator for Characterization of Volcanic Seismic Signals
                  Version 1.1
-------------------------------------------------------------------------------------------------------------------------------------------
          Theoretical Physics and the Cosmos Department
      Signal Theory, Telematics and Communications Department
---- Andalusian Institute of Geophysics and Prevention of Seismic Disasters ----------
      Granada University (Ugr), Granada, Spain
-------------------------------------------------------------------------------------------------------------------------------------------

    Author: Ligdamis Gutiérrez PhD (1, 2), Rey Devesa Pablo (1,2), Ibañez Jesús (1,2)
    Granada, Spain 2023-2024

Institutions associated:

(1) Department of Theoretical Physics and Cosmos. Science Faculty. Avd. Fuentenueva s/n. University of Granada. 18071. Granada. Spain.

(2) Andalusian Institute of Geophysiscs. Campus de Cartuja. University of Granada. C/Profesor Clavera 12. 18071. Granada. Spain.

'' WARNING: Do not modify or edit the code without permission of the author.
    In case of using this software, indicate and refer to the author and the institution he represents.
    The University of Granada, Ugr ''

-------------------------------------------------------------------------------------------------------------------------------------------

Acknowledgment:

This software is the product of the research by the Spanish projects:

a)	PID2022-143083NB-I00, “LEARNING”, funded by MCIN/AEI /10.13039/501100011033
b)	JMI and LG were partially funded by the Spanish project PROOF-FOREVER (EUR2022.134044)
c)	PRD was funded by the Ministerio de Ciencia e Innovación del Gobierno de España (MCIN), Agencia Estatal de Investigación (AEI), Fondo Social Europeo (FSE), 
        and Programa Estatal de Promoción del Talento y su Empleabilidad en I+D+I Ayudas para contratos predoctorales para la formación de doctores 2020 (PRE2020-092719).
d)	Spanish Project PID2022-143083NB-100 founded by MCIN/AEI/10.13039/501100011033 and by FEDER (EU) “Una manera de hacer Europa”.
e)	PLEC2022-009271“"DigiVolCa”", funded by MCIN/AEI, funded by MCIN/AEI/10.13039/501100011033 and by EU «NextGenerationEU/PRTR», 10.13039/501100011033.

-------------------------------------------------------------------------------------------------------------------------------------------

Introduction:

Dear User:

This file contains information related to the Application.
Please read it carefully before starting work.

In the same way, it is recommended to review the contents of the manual attached to the documents, in order to become familiar with the different actions that can be carried 
out, through the elements of system management.

The system was developed in version 3.8.6. of the Python language.
The software is open source and can be downloaded from the website:

https://www.python.org/downloads/release/python-386/

***(However, it can operate without problems in Python, version 10.10)***

Since Python a multiplatform lenguaje, it works the same on Windows, Linux, Mac systems, or Android for Tablets and mobile phones (after adapting Python for these devices).

It works on 32 and 64 Bit Systems (x86, win64), under Windows (7, 8, 10, 11).
This Software has been tested on Linux systems on Ubuntu 20 and the macOS for Mac System.
Additionally, should work without problems in other similar Linux systems like: Debian, Ret Hat, Fedora, SUSE, etc.

The version of Python in which the interface has been programmed is 3.8.6. However, it can operate without problems in Python, version 10.10
Any modification of the Python codes in a different version can be cause alterations in the functioning of the system.
The Python documentation must be revised to adapt the code to the correct version.

For the reading and manipulation of common file formats, access data centers and seismological signal processing routines the ObsPy library is used. ObsPy is a Python 
framework for Seismology, is an open-source. The documentation can be downloaded from the website:

https://docs.obspy.org/

To represent the graphs, the Matplotlib library is used. The documentation and terms of the use of the license of the Matplotlib by the user
can be read and downloaded from the website:

https://matplotlib.org/stable/users/index.html

The main interfaces of the programs are designed only in English. But, the user manual document is written in English and Spanish.

a) User_manual_Entropy_System_EN1.PDF - English version
b) User_manual_Entropy_System_ES1.PDF - Spanish version

-------------------------------------------------------------------------------------------------------------------------------------------
GENERAL CONTENT INDEX
-------------------------------------------------------------------------------------------------------------------------------------------
1.- Main system objective.
2.- General structure and folders organization.
3.- Description of the Folders and elements containing.
4.- Prerequisites (installing Python and Pip on windows)
5.- System installation and running under windows
6.- System installation and running under Linux and Mac System
7.- Installation comments.
8.- Modules under construction.

-------------------------------------------------------------------------------------------------------------------------------------------
1.- MAIN OBJECTIVE OF THE SYSTEM
-------------------------------------------------------------------------------------------------------------------------------------------

Through friendly and easy-to-use interfaces, this system represents the first version of a software that provides tools for reading seismic-volcanic signals, 
filtering, Entropy calculation algorithms and graphs that help the human operator to:
 
a) In the preparation and analysis of seismic-volcanic signals, of different formats
   (SAC, MSEED, GSE2, EVT, WAV among others),
    through the process of filtering the signals with filters:
     (Lowpass, Highpass, Bandpass and Bandstop).

b) In the analysis of filtered seismic-volcanic signals, through the use of various techniques such as:
   - Calculation of Shannon Entropy and its envelope, through the use of several analysis windows of both the Entropy and the envelope.
   - Calculation the frequency index and its envelope, through the use of several analysis windows of the envelope and digital filters.
   - Calculation of Kurtosis and its envelope, through the use of several analysis windows of the envelope and digital filters.
 
   * Period analysis of records of one year or user-defined time intervals.

c) In the performs the comparison, calculation and plots the Shannon entropy envelopes, using various user-defined filter frequencies.
   
-------------------------------------------------------------------------------------------------------------------------------------------
2.- GENERAL STRUCTURE AND ORGANIZATION OF FOLDERS
-------------------------------------------------------------------------------------------------------------------------------------------

Main items to download: Two compressed files in ".Rar" format, containing the following:

a) Structure of the content to download (Two files in:
     1.- Document folder (Compressed folder with WinRar)
          1.1.- User_manual_Entropy_System_ES1.pdf (Spanish version)
          1.2.- User_manual_Entropy_System_EN1.pdf (English version)
          1.2.- README.txt
          1.3.- EntropySis1.bat (download and copy to windows desktop)
          1.4.- Initial_requeriments.txt
     2.- EntropySis1 folder, main software folder (Compressed folder with WinRar)
           2.1.- Images folder: (Icons and images, Folder must be inside the main folder)
           (Analysis, Back, Clean, Exit, Filter, IAG, Load, Next, Ugr).gif
            Masaya_Volcanoe.JPG, etc.
           2.2.- class_canvas1.py program (program must be inside the main folder)
           2.3.- ReadSignals1.py program (program must be inside the main folder)
           2.3.- EntropySis1.py program (program must be inside the main folder)
           2.4.- EnvelopeFilter.py program (program must be inside the main folder)
           2.5.- Menu1.py program (program must be inside the main folder)
                 Welcome interface to access the programs interfaces.
    
-------------------------------------------------------------------------------------------------------------------------------------------
3.- DESCRIPTION OF THE FOLDERS AND ELEMENTS CONTAINNING
-------------------------------------------------------------------------------------------------------------------------------------------

- In the main part there are the necessary programs for the operation of the Volcano-Seismic signals entropy analysis system. Located in the two compressed folders.
- The content is as follows:

1) Document folder

   a) The user manual (PDF). System user manual, written in English and Spanish. (User_manual_Entropy_System_EN1 and User_manual_Entropy_System_ES1)
       It contains the necessary instructions for handling the system and the elements that make it up.
   b) The file README.txt. Contains the basic instructions for installing the software and all items
        that make up the system
   c) The file "Initial_requeriments.txt" contains the list of necessary libraries that python uses to run this system.
       It is recommended to execute each line in a console or "CMD" window, for the installation of the libraries                  
       through "Pip", after installing Python.
   d) The ".bat" file (EntropySis1.bat), that facilitate the start of the system in Windows System.
        These files present a Welcome screen change to the working directory
        where the programs are located and run python with the startup program: "Menu1.py" to start the system.         
        
2) EntropySis1 folder

   e) "Menu1.py" Program of the interface. Welcome and start the system. This interface, contains the command buttons that give access to the three modules of which the system is composed.
   f) "ReadSignals1.py" Program of the interface. This interface, contains the process of reading, filtering and plot the seismic-volcanic records in one or three components.
       The main objective is to know in advance which records or components are most viable to analyze using Shannon Entropy.
   g) "class_canvas1.py" Program. This Program is the which contains part of the initial canvas of the interface to the ReadSignals1.py.
   h) "EntropySis1.py" Program of the interface. This interface contains the process of reading, filtering, calculating and plotting seismic-volcanic records of Shannon Entropy, Frequency Index, Kurtosis and their envelopes.
       Several analysis window sizes are used (10 minutes, one hour and 24 hours) and the user can also configure various window sizes when calculating the envelope. 
       Also, the calculation can be established using time intervals established by the user. All this, using each of the types of filters available (Lowpas, Highpass, Bandpass and Bandstop).
   i) "EnvelopeFilter.py" Program of the interface. Module that performs the comparison, calculation and plot the Shannon Entropy envelopes, using various filter frequencies.

   j) "Images" folder, which contains the icons and images of the interfaces. It must be located in the same place as the all interface programs. This is in the "My Documents" folder. 

** IMPORTANT NOTE ***

This software represents a new version (1.1) of the previous one "Shannon Entropy estimator for Characterization of Volcanic Seismic Signals" version (1.0) DOI (https://zenodo.org/records/10784737). 
An update that includes new analysis tools such as Frequency index and Kurtosis. 
In addition, it extends the parameters of the envelope values, adding a smoothness value and another for tolerance of null values (NaN).            
        
** At future, this Software may be expanded by adding new modules, containing other analysis tools, and volcano-Seismic signals classification. **
    
-------------------------------------------------------------------------------------------------------------------------------------------
4.- PREREQUISITES (INSTALLING PYTHON AND PIP ON WINDOWS)
-------------------------------------------------------------------------------------------------------------------------------------------

It's recommended to have at least 8 GB or more (16 GB would be perfect) of memory in the system.

Python and its package manager (Pip) are native to Linux languages. That is, when Linux is installed, both the Python language and its package manager (Pip) are installed. 
Although it is always recommended to have the most up-to-date version, both of Python and pip. what in Linux is done almost automatically with the application manager and that, in addition, Linux generally communicates to the user.

In the Windows system, it must be installed before using the system. Because the system itself has been created with this language. The good thing is that Python can run without problems on Windows operating systems.

There is an easy way to do this.

a) Download the appropriate version from the Python distribution web page, located at the following web address:
             https://www.python.org/downloads/

    On the Web, the correct version must be selected, according to the type of operating system
    that is in the computer, including if it is 32 or 64 bits.

    On the Web, both the executable version (.exe) and the compressed file version (.zip) or (.tz) for Linux are available for download.

Once this version is downloaded, it is installed in the operating system (as administrator). When starting the installation, a screen of the installation assistant is presented, which indicates the steps to follow to install the language.

You just have to follow the steps. It is important to leave the box to add to the windows "path" the installation path where the Python files are located. If you skip this step, you have to do this manually. Because if it is not set, Python is not recognized by the system to run.

Manually, this can also be set from the system environment variables. Manually found in: Control Panel/System/Advanced System Settings/Environment Variables/Edit

Here you set where the Python scripts and programs are located on the system. But the easiest and most prudent thing to do is to simply check the box that allows this during the Python installation.

Once Python and pip are installed on the system, check that they work. To do this, you just have to see this in a windows command window (CMD), using the following commands.

> python –V

And to verify the “pip” the following command is typed:

> pip –V

After typing “pip – V”, it is usually seen that the version of pip is “20.2.1”. At this point, it is recommended to update that version, since by default "pip" is installed together with "Python", 
but it does not install the latest or most updated version. To do this, in the CMD window or console, type the following command in: (Windows/Linux).

     Windows: > python –m pip install –upgrade pip    |   Linux: $ sudo python3 –m pip install –upgrade pip

This indicates that the "pip" will be updated to its latest version (In Linux, as "superuser", that is, "sudo" at startup). Note that for Windows, you type "python", but on Linux you must type "python3".

Once Python is installed and the "pip" is updated, you must proceed to install the additional packages and libraries that Python needs to run the system. This is done using the "pip". To do this, the file "Initial_requeriments.txt" is used, which is found with supplied files.

Proceed in the console or command window "Cmd" to install each recommended library.

Once this is done, the operating system is ready to run both python and the main program.

-------------------------------------------------------------------------------------------------------------------------------------------
5.- SYSTEM INSTALLATION AND RUNNING UNDER WINDOWS
-------------------------------------------------------------------------------------------------------------------------------------------

After downloading the items and once both the Python and the necessary additional libraries have been installed.

To install the system on Windows systems (either 32 or 64 bits), do the following:

a)  Copy the (all) folder containing the Python and data files.
     This is according to the "English" version 1.0
     Path to "Documents\EntropySis1\"
     Remember, these folders (Data and EntropySis1), should be copied to "My Documents" on the computer.

b) Copy the ".bat" file (EntropySis1.bat), to the desktop of the computer.

c) In the desktop, run this file as "administrator" (right click on the file and choose this option)
     The Welcome screen will be displayed:

---------------------------------------------------------------------------------------------------------

                ==============================================================================
		=                                                                            =
		=  Welcome to:                                                               =
		=                                                                            =
		= Shannon Entropy estimator for Characterization of Volcanic Seismic Signals =
		=                                   (Vers. 1.1)                              =
		=                   Theoretical Physics and Cosmos Department                =
		=           Signal Theory, Telematics and Communications Department          =
		=                        Andalusian Institute of Geophysics                  =
		=                              Granada University (Ugr)                      =
		=                                                                            =
		=                              Developed in Python 3.8.6                     =
		=                       Execution for Windows and Linux System               =
		=                               Granada, Spain. 2024                         =
		==============================================================================

           		Please, Minimize the CMD from the Python.exe window (in black).
               		(Don't close it, because the system also closes).           
           		When you exit the system, this window closes automatically.
           
                       		To continue, please press a key.

                  		*** Please, press a key to Start the System. ***

----------------------------------------------------------------------------------------------------------   
    
Pressing any key will present two screens. One in black, which is the Python command window (cmd).
This must be minimized, so that it does not disturb the view of the system.

The start and welcome screen of the "Menu1.py" system will be presented. This screen is the presentation and entry to the system.
You can exit here by clicking the "Exit" button or continue by clicking any of the three available command buttons (one for each module in the system).

Clicking the command button of the selected module presents the main interface of that module.

This will present the main screen of the interface. This is where the actions of the process are carried out: 
loading of the seismic-volcanic records, filter analysis, calculation of entropy and its envelope, saving resulting files, etc. 
In addition, presenting the resulting graphics. Please refer to the user manual attached in the documentation.

To return to the main menu from an interface, click the "Back" button. This action will close the current interface screen and open the main menu module again, to select a different module.

To exit, click the "Exit" button. In the dialog window, type "Ok" to accept the output. Otherwise "Cancel" to continue in the system.

-------------------------------------------------------------------------------------------------------------------------------------------
6.- SYSTEM INSTALLATION AND RUNNING UNDER LINUX
-------------------------------------------------------------------------------------------------------------------------------------------

Installation on Linux systems is similar to Windows. The main folder is copied either to the desktop, or to the personal folder, etc.

This is according to the "English" version 1.0
    Path to "Documents\EntropySis1\"

From that location (inside the main folder, where the "Menu1.py", class_canvas1.py, EntropySis1.py, Images folders are located), open a window or command console and type:

“$ python3 Menu1.py”

This command is to start the system and proceed to perform the analysis normally.
The output is similar to Windows System, must be clicking in the "Exit" button.

Remember:
Once Python is installed and the "pip" is updated, you must proceed to install the additional packages and libraries that Python needs to run the system. 
This is done using the "pip". To do this, the file "Initial_requeriments.txt" is used, which is found with supplied files.

-------------------------------------------------------------------------------------------------------------------------------------------
7.- INSTALLATION COMMENTS
-------------------------------------------------------------------------------------------------------------------------------------------

The system works fine on Windows (XP, 7, 8, 10, 11) 32-bit and 64-bit systems.

The system it’s designed to work in multiplatform.
It is allowed by programming in Python 3.8.6. On Windows, Linux and Mac systems without problems.

Warning: Other higher versions of Python may cause problems in some libraries, check their manual to ensure proper operation.
         However, it can operate without problems in Python, version 10.10

---------------------------------------------------------------------------------------------------------------------------------------------

Warning: It is recommended not to make alterations, changes, or eliminations of part or the complete content of the codes and programs that comprise the system, 
without the necessary knowledge, since it can seriously affect its operation.

-------------------------------------------------------------------------------------------------------------------------------------------
8.- MODULES UNDER CONSTRUCTION
-------------------------------------------------------------------------------------------------------------------------------------------

Soon, in a new version or update of the current version (1.1), extra algoruthms and new module may be added, containing several types of analysis, functionalities or more methods, 
other analysis tools, and volcano-Seismic signals classification which provide an improvement in the study and research of the scientific community.


** THEY WILL BE AVAILABLE FOR DOWNLOAD IN THE FUTURE **
Sincerely, Best Regards. Ligdamis A. Gutiérrez E. PhD.

-------------------------------------------------------------------------------------------------------------------------------------------
