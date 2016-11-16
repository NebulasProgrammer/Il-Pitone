#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sixsixsix.py
#  
#  Copyright 2016
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import os, socket, sys, time #Importiamo le librerie

#Questo crea un oggetto socket


#Alcune variabili globali

f=0

#Ho creato questa funzione per fare il tamarro
def wall():
    os.system("clear")
    print '''
     (                (    (               )      )       
 )\ )  (          )\ ) )\ )  *   )  ( /(   ( /(       
(()/(  )\        (()/((()/(` )  /(  )\())  )\()) (    
 /(_))((_)  ___   /(_))/(_))( )(_))((_)\  ((_)\  )\   
(_))   _   |___| (_)) (_)) (_(_())   ((_)  _((_)((_)  
|_ _| | |        | _ \|_ _||_   _|  / _ \ | \| || __| 
 | |  | |        |  _/ | |   | |   | (_) || .` || _|  
|___| |_|        |_|  |___|  |_|    \___/ |_|\_||___| 
                                                                                                                                   
                             
                            '''
                             
def continuare():
    yorn=raw_input("\n########## Premere invio per continuare ##########")

		
def client_tcp():
    target_host=raw_input("Inserire il target Host (prova inizialmente con www.google.it): ")
    target_port=80
    client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_host,target_port))
    client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
    response=client.recv(4056)
    print response
	
	
def main():
    while (f==0):
        wall()
        print"1)Client-TCP"
        print"9)Versione"
        print"0)Esci"
        scelta=input("Scelta: ")
        if scelta==1:
            client_tcp()
            continuare()
            time.sleep(2)
        elif scelta==0:
            os.system("exit")
            time.sleep(2)
        elif scelta==9:
            print"La versione attuale è la 0.1"
            time.sleep(2)

if __name__ == "__main__":
    main()
