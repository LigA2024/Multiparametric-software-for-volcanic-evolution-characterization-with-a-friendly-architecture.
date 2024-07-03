# Multiparametric-software-for-volcanic-evolution-characterization-with-a-friendly-architecture.

In the process of developing scientific research, vulcanological and seismological observatories, as well as current research institutes, require reliable and secure technological tools. Tools that are easy to use, represent a low learning curve for users, and provide reliable assistance to the operator in reading information from various seismic formats used worldwide and integrating various scientific calculation and analysis processes, as well as commonly employed digital filters. 
Tools that allow for more efficient analysis of seismic record databases, obtaining a more quantified benefit from the scientific information of the various seismic-volcanic events being monitored. This will enable the performance of significant, reliable, and optimal analyses, to build excellent recognition and early warning systems.

In this works, we develop a set of technological tools developed in the Python language. These set tools represent Secure, scalable software applications that can be deployed in real-time to handle large volumes of seismic data, enabling the creation of efficient early warning models. The standardization of metrics and methods that validate studies during the analysis process of eruptive episodes. The learning curve and use of software tools for users must be quick for optimal performance. Metric like Shannon entropy has proven to be a very effective parameter for quantifying the eruptive state of a volcano. In this work, the use of this metric is implemented from different perspectives in which its defining values can be adjusted. Observatories and seismological research centers need user-friendly, simple-to-use tools that meet their research needs.




## Toolkit Description

This set of software applications consists of three individual tools or modules that, in a user-friendly manner, provide calculation and analysis methods through graphical user interfaces (GUIs). In addition to these three modules, the system begins with a welcome or home module, which includes access to each of the working modules. Furthermore, the system includes a user manual written in Spanish and English, as well as basic instructions for installing the libraries and Python software needed for the system to function properly.

The three analysis tools described in this work are the following:
  
1. - Performs the read, filtering and plot the seismic signals.
2. - Entropy estimator for Characterization of Volcanic Seismic Signals.
3. - Performs the read, filtering and plot the entropy envelope with various frequencies.

Among the main functionalities and utilities that this set of tools provides to researchers and observatories, the following can be mentioned:

(a)	Reading seismic records in various formats commonly used in national and international seismological centers (MSEED, SAC, WAV, GSE2, EVT, GCF, among others).
 
(b)	Performing commonly used analyses in observatories, involving the use of various digital filters with one or three components (North-South, East-West, and Vertical). 

(c)	Calculating Shannon Entropy, Kurtosis, and Frequency Index with their respective smoothed function, using analysis windows of 10 minutes, one hour, or 24 hours. Applying different smoothing filters with width sizes such as 50, 100, 300, etc. 

(d)	Comparing, calculating, and plotting Shannon Entropy smoothed function using various frequency values of a specific filter, defined by the user. At the same time, the possibility to present the results of the analyses graphically and store them in various formats (PNG, JPG, GIF, SVG, among others) is offered. Each of the modules includes various data input validation windows to check for user input errors and prevent the system from crashing as a result.



## Data-repositories


It is important to highlight that the raw data corresponding to the Colima and La Palma volcanoes analyzed for this study can be found online at ZENODO:

[https://zenodo.org/records/10781903]
[https://zenodo.org/records/10781515] 

Please, to run properly, the code should be modified including the path where these files are located locally.

