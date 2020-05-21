reading some data files with information on employees and then generate a report.

improving the performance of the script:
  instead of downloading the whole file and then going over it for each date
  which will  takes almost 2 minutes to complete for 2019-01-01. 
  An optimized script should generate reports for the same date within a few seconds.
  To check the execution time of a script  time ./start_date_report.py

to fix this issue:
1. Download the file only once from the URL.
2.pre-process it so that the same calculation doesn't need to be done over and over again. 
   and This can be done in two ways. You can choose any one of them:
	- To create a dictionary with the start dates and then use the data in the dictionary instead of the complicated calculation.
	- To sort the data by start_date and then go date by date.
