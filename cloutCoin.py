#Author: Foster C. Williams fosterclarksonwilliams@gmail.com
#Basic program to pull down data from google trends with a crude GUI
import coinTrends 
from os import system
import sys
import datetime
import time



def main():
  print("#######################################");
  print("#       Welcome to CloutCoin          #");
  print("#                                     #");
  print("#   Google Trends CLI Tool By FosDos  #");
  print("#######################################");
  cont = True;

  while(cont):
    print("$$$$$$$$");
    print("$ Menu $");
    print("$$$$$$$$");
    print("1) Get data about a topic between two dates");
    print("2) Get data about a topic for the past 5 years");
    print("3) Input a file of numerous topics to get data on");
    print("4) Exit");
    option = input("Select an option \n");

    if(option == "1"):
      getData();
    if(option == "2"):
      getFiveYearData();
    elif(option == "3"):
      bigData();
    elif(option == "4"):
      cont = False;
  exit();
    
    
def getData():
  print("Input search term");
  searchTerm = input("Input search term: ");
  startDate = input("Input Start Date in YYYY-MM-DD format: ");
  endDate = input("Input End Date in YYYY-MM-DD format: ");
  try:
    data = coinTrends.getPayload(searchTerm,startDate,endDate);
  except:
    print("######## ERROR ##########");
    print("Please insure you are using the correct formatting for the date and try again");
    return;
  newFileName = searchTerm + "_data.txt";
  dataEnter = open(newFileName,'w');
  dataEnter.write(data);
  dataEnter.close();
  print("Data has been written to " + newFileName);


def getFiveYearData():
  searchTerm = input("Enter Search Term: ");
  data = coinTrends.getPayload(searchTerm,'today','5-y');
  newFileName = searchTerm + "_five_year_data.txt";
  dataEnter = open(newFileName,'w');
  dataEnter.write(data);
  dataEnter.close();
  print("Data has been written to " + newFileName);
  return;


def bigData():
  startDate = input("Enter start date in YYYY-MM-DD format: ");
  endDate = input("Enter end date in YYYY-MM-DD format: ");
  inputFile = input("Enter input file name: ");
  outputFile = input("Enter output file name or press enter to get default name: ");
  if(outputFile == ""):
    outputFile = "big_data_output.txt";
  source = open(inputFile,'r');
  writer = open(outputFile, 'w');
  lines = source.readlines();
  start = "";
  end = "";
  toReturn = "";
  print("Starting data compilation loop...");
  for line in lines:
    try:
      data = coinTrends.getPayload(line,startDate,endDate);
    except:
      print("Error pulling data, make sure you have the dates formatted correctly");
      return;
    writer.write(data);
    writer.write(" ");
  source.close();
  writer.close();
  return;
  
main();


