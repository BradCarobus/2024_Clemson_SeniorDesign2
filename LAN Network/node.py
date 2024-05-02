import socket
import multiprocessing
import threading
import csv
import time
import random
import os  
import datetime
import hashlib
from hashlib import sha256
from Cryptodome.PublicKey import RSA

class Block:
    def __init__(self, timestamp, event, statusFlag, prevHash, curHash):
        self.timestamp = timestamp
        self.statusFlag = statusFlag
        self.event = event
        self.prevHash = prevHash
        self.curHash = curHash


host = "172.16.202.18"
port = 65432
Id = 0

def Consensus_Algorithm(nums):
    try:
        with open("consensus.csv", 'a+', newline='') as csvfile:
            csvfile.write(nums + '\n')
            #writer = csv.writer(csvfile)
            #writer.writerow([nums])
    except Exception as e:
        print(f"Error Occured {e}")

    


def handle_incoming(conn, addr):
    print(f"Connected by {addr}")
    #will have to specify whether its recieving a block or just the check num, this is where it will
    #intake data and do something with it.
    data = conn.recv(5)
    #if not data:
    print(f"Connection closed by {addr}")
   
    
    if data.decode() == 'conse':
        data = conn.recv(5)
        Consensus_Algorithm(data.decode())
    elif data.decode() == 'block':
        data = conn.recv(1)
        #see which public key we need to use based on which pis id we get
        with open("cheatKeys.csv", "r") as keyFile:
            for i in range(int(data) + 1):
                pubKeyn = keyFile.readline()
                pubKeye = keyFile.readline()
        
        dataVar = ''
        countDetect = 0
        while countDetect < 3:
            data = conn.recv(1)
            if data.decode() == ' ':
                countDetect = countDetect + 1
            else:
                countDetect = 0
            if countDetect < 2:
                dataVar = dataVar + data.decode()

        dataVarEnc = dataVar.encode('utf-8')
        hashBlock = int.from_bytes(sha256(dataVarEnc).digest(), byteorder='big')

        with open("prevHash.csv", "w") as hashFile:
            hashFile.write(str(hashBlock))

        data = conn.recv(2048)
        decrData = pow(int(data.decode()), int(pubKeye), int(pubKeyn))

        with open("signatureList.csv", "a") as sigFile:
            sigFile.write(str(data.decode()) + '\n')

        if hashBlock == decrData:
            dataVar = dataVar + str(decrData)
            with open("data_logV2.csv", "a") as file:
                file.write(dataVar + ' \n')
        else:
            print("Warning: Signature cannot be verified.")
            with open("data_logV2.csv", "a") as file:
                file.write("Verification failed.\n")
        
        

    print(f"Recieved data: {data.decode()}")
    conn.sendall(b"Thanks")
    conn.close()

def recieve_connection(sock):
    while True:
        conn, addr = sock.accept()
        process = multiprocessing.Process(target=handle_incoming, args=(conn, addr))
        process.start()



def Broadcast_Block(addresses, number):
    #block creation
    ct = datetime.datetime.now()
    severity = 0
    ctString = ct.strftime("%m/%d/%Y, %H:%M:%S")
    if number > -1: #if number is -1, a node is down
        if number > 0.8:
            severity = 2
        elif number > 0.5:
            severity = 1
        curBlock = Block(ctString, "Speed", severity, 0, 0)
    else:
        curBlock = Block(ctString, "Node", 2, 0, 0)
    
    #find previous hash
    with open("prevHash.csv", "r") as hashFile:
        readHash = hashFile.read()
    curBlock.prevHash = readHash
    if curBlock.prevHash == '':
        curBlock.prevHash = 'None'
    
    #turn data into a string of data
    dataString = curBlock.prevHash + ' ' + str(curBlock.timestamp) + ' ' + curBlock.event + ' ' + str(curBlock.statusFlag) + ' ' #may need to change back to whitespace rather than tabs
    dataStringEnc = dataString.encode('utf-8')

    #generate hash
    hashBlock = int.from_bytes(sha256(dataStringEnc).digest(), byteorder='big')
    curBlock.curHash = str(hashBlock)

    with open("prevHash.csv", "w") as hashFile:
        hashFile.write(curBlock.curHash)

    with open("pi1PrivateKey.csv", "r") as keyFile:
        pi1PrivKeyd = keyFile.readline()
        pi1PrivKeyn = keyFile.readline()

    signature = pow(hashBlock, int(pi1PrivKeyd), int(pi1PrivKeyn))

    with open("signatureList.csv", "a") as sigFile:
        sigFile.write(str(signature) + '\n')

    #saves data in a csv
    with open("data_logV2.csv", "a") as file:
        file.write(curBlock.prevHash + " " + curBlock.timestamp + " " + curBlock.event + 
                " " + str(curBlock.statusFlag) + " " + curBlock.curHash + " \n")
    
    for add in addresses:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            try:
                client_socket.connect((add, port))
                client_socket.sendall(bytes('block', "utf-8"))
                client_socket.sendall(bytes(str(Id), "utf-8"))
                client_socket.sendall(dataStringEnc)
                client_socket.sendall(bytes('  ', "utf-8"))
                client_socket.sendall(bytes(str(signature), "utf-8"))
                client_socket.close()
            except ConnectionRefusedError:
                print("Connection to other node failed")

def Broadcast_Consensus(message, addresses):
    for add in addresses:

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            try:
                client_socket.connect((add, port))
                client_socket.sendall(bytes('conse', "utf-8"))
                client_socket.sendall(message)
                client_socket.close()
            except ConnectionRefusedError:
                print("Connection to other node failed")

def consensus_calc(orig):
    sum = round(orig, 2)
    print(orig)
    with open("consensus.csv", 'r', newline='') as csvfile:
        for x in range(4):     #change back to 4!!!!!!
            num = csvfile.readline()
            print(num)
            sum = sum + float(num)
        remain = sum % 5               #change back to 5!!!!!!
    return int(remain)

def main():

    #Emulated Broadcasting
    addresses = ['172.16.202.14', '172.16.202.13', '172.16.202.12', '172.16.202.11']

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host,port))
        s.listen()
        print(f"Server Listening on {host}:{port}")

        #creates a thread to handle accepting connections
        accept_thread = threading.Thread(target=recieve_connection, args=(s,))
        accept_thread.start()

        while True:
        #sending broadcast data here
            
            #This is where we will send the number to all the pis
            #message = input("Enter Message to send: ")
            try:
                with open("belt_speed.txt", newline='') as beltfile:
                    strNum = beltfile.readline()
                    try:
                        number = float(strNum)
                        if number > 0.5:
                            #Danger Zone, Generate Consensus number then send that number out to all the pis
                            consensus_num = random.uniform(1.0, 100.0)
                            byte_message = bytes(str(consensus_num), "utf-8")
                            Broadcast_Consensus(byte_message, addresses)
                            time.sleep(20)
                            consId = consensus_calc(consensus_num)
                            time.sleep(2)
                            with open("consensus.csv", 'w', newline='') as csvfile:
                                csvfile.write("")
                            print('\n' + str(consId) + '\n')
                            
                            if consId == Id:
                                Broadcast_Block(addresses, number)
                        else:
                            message = 'all good'
                    except ValueError:
                        #print("ValueError")
                        print("")

            except FileNotFoundError:
                print("File Not Found")



if __name__ == "__main__":
    main()
