#DO NOT RUN THIS AGAIN!!!!!!
#THIS WILL RESET THE KEYS FOR PI1 IF YOU DO!!!!!
#MEANING WE WILL HAVE TO CHANGE ALL THE KEYS!!!
#STOP!
#CEASE!
#HALT!
#Thanks :)

import os  
import time
from time import sleep 
import datetime
import hashlib
from hashlib import sha256
import hmac
#import rsa
from Cryptodome.PublicKey import RSA

class Block:
    def __init__(self, timestamp, event, statusFlag, prevHash, curHash):
        #self.key = key
        self.timestamp = timestamp
        self.statusFlag = statusFlag
        self.event = event
        self.prevHash = prevHash
        self.curHash = curHash

#private key is converted to bytearray to be fed into hmac function
#private key
testKey = 'MIICWgIBAAKBgHN7B9VchVdFz0g/aKwpDHjAAHiMIUUh0fWIQ0k6yhgTzxWr7QpZoJWj5JSXkk5j8XhwJa3PzJ0g33VP/U8d2Kocq8lqz/XshXOK+fKkBnZZzo8MZM7HJYfuKMgE/zXqgO3uS2VFMIsgfN5OQw8FIGth1Jpo9IsDzKUdOPURTjc5AgMBAAECgYBB6eRzvSaCxN7mbwLw2VE8DuN16w4GZqJv0gIN51d43L2jsglPkg7durl6svUYd2VZiDGJfwVcXmoNjMWaBgAne/IwFfL0xzMKgOUy8KmEt3xf12WKCpvQGrpn+GcmADi799Z2zKA+SuHeY8hR3xD7j1wKMqbUmykVzpBxtdeNsQJBALmNUXlIjdEwLAJ0FRo3xL3lO/OXFAT/7qpt5w/c09keKXP3Xmvt5H7vYzLoCeM54TOtvTG/F/NdS9ZoWtb6520CQQCfUyMPlf4JQOMtuTpfi3dUHTs6U/iqOPYYRreFR/OvMDETXNuHH2nfVD7kXm/5AQN1/gK4jamGo/E8NJtOorN9AkAt645dQJpwScaqeMX8Lg8Pm9qhZyM6NYiAPyCu6Uy4b+F8ZJzGgyJIU8AuCgTgaiOUoYuv8wXfYZhyIHNSvtdlAkAJta1bU87JjZTKwpEWJY++JpHnehqbdSE6VYT1sG7fbFZxUaVnVLjFDYNPs5mrWS520GYmDSwZsoAPJT2ZyzyZAkAiK1GsBQ7HNlelh4Ei9r1vHiCafdHzv/FwKVW+UaSjtgzHVbrt/BpZ5tfk4fgMwYptQl4e9DHLrqYGf34RvWeL'
#public key
publicKey = 'MIGeMA0GCSqGSIb3DQEBAQUAA4GMADCBiAKBgHN7B9VchVdFz0g/aKwpDHjAAHiMIUUh0fWIQ0k6yhgTzxWr7QpZoJWj5JSXkk5j8XhwJa3PzJ0g33VP/U8d2Kocq8lqz/XshXOK+fKkBnZZzo8MZM7HJYfuKMgE/zXqgO3uS2VFMIsgfN5OQw8FIGth1Jpo9IsDzKUdOPURTjc5AgMBAAE='
byteKey = bytearray()
byteKey.extend(map(ord,testKey))


#(pi1_pub, pi1_priv) = rsa.newkeys(2048) 

# generating keys
keyPair = RSA.generate(bits=2048)
keyPair2 = RSA.generate(bits=2048)
keyPair3 = RSA.generate(bits=2048)
keyPair4 = RSA.generate(bits=2048)
keyPair5 = RSA.generate(bits=2048)

with open("cheatKeys.csv", "w") as keyFile:
        #keyFile.write(pi1_pub.save_pkcs1().decode('utf-8'))
        keyFile.write(str(keyPair.d))
        keyFile.write('\n')
        keyFile.write(str(keyPair.n))
        keyFile.write('\n')
        keyFile.write(str(keyPair.e))
        keyFile.write('\n')
        keyFile.write(str(keyPair2.d))
        keyFile.write('\n')
        keyFile.write(str(keyPair2.n))
        keyFile.write('\n')
        keyFile.write(str(keyPair2.e))
        keyFile.write('\n')
        keyFile.write(str(keyPair3.d))
        keyFile.write('\n')
        keyFile.write(str(keyPair3.n))
        keyFile.write('\n')
        keyFile.write(str(keyPair3.e))
        keyFile.write('\n')
        keyFile.write(str(keyPair4.d))
        keyFile.write('\n')
        keyFile.write(str(keyPair4.n))
        keyFile.write('\n')
        keyFile.write(str(keyPair4.e))
        keyFile.write('\n')
        keyFile.write(str(keyPair5.d))
        keyFile.write('\n')
        keyFile.write(str(keyPair5.n))
        keyFile.write('\n')
        keyFile.write(str(keyPair5.e))

#while(1):
    #creates the block
    #ct = datetime.datetime.now()
    #ctString = ct.strftime("%m/%d/%Y, %H:%M:%S")
    #curBlock = Block(ctString, "Check", 0, 0, 0)
 
    #prepares data to be fed into hmac function
    #dataString = str(curBlock.timestamp) + curBlock.event + str(curBlock.statusFlag)
    #byteDataString = bytearray()
    #byteDataString.extend(map(ord, dataString))

    #creates and saves the current hash
    #hashBlock = hmac.new(byteKey, byteDataString, md5)
    #val = hashBlock.digest()
    #curBlock.curHash = hashBlock.hexdigest()

    #with open("prevHash.csv", "r") as hashFile:
    #    readHash = hashFile.read()
    #curBlock.prevHash = readHash

    #with open("prevHash.csv", "w") as hashFile:
    #    hashFile.write(curBlock.curHash)

    #saves data in a csv
    #with open("data_logV2.csv", "a") as file:
    #    file.write("PrevHash: " + curBlock.prevHash + 
    #        " \tTimeStamp: " + curBlock.timestamp + " \tEvent: " + curBlock.event + 
    #            " \tStatus: " + str(curBlock.statusFlag) + " \tHash: " + curBlock.curHash + "\n")

    #dataString = str(curBlock.prevHash) + dataString + str(curBlock.curHash)
    #message = dataString.encode('utf8')
    #cryptMessage = rsa.encrypt(message, publicKey)
        #Send message over network. Other Pis decode this and use the raw data to make their own hash. Compare it to the sent hash to see if data changed.
    
    
    
    
    #time.sleep(60)
        


ct = datetime.datetime.now()
ctString = ct.strftime("%m/%d/%Y, %H:%M:%S")
curBlock = Block(ctString, "Check", 0, 0, 0) #currently test data. Need to make it real
    
    #find previous hash
with open("prevHash.csv", "r") as hashFile:
    readHash = hashFile.read()
curBlock.prevHash = readHash
    
    #turn data into a string of data
dataString = readHash + ' ' + str(curBlock.timestamp) + ' ' + curBlock.event + ' ' + str(curBlock.statusFlag)
dataStringEnc = dataString.encode('utf-8')

    #generate hash
hashBlock = int.from_bytes(sha256(dataStringEnc).digest(), byteorder='big')
#hashBlock = hashlib.sha256()
#hashBlock.update(dataStringEnc)
#val = hashBlock.digest()
curBlock.curHash = str(hashBlock)

signature = pow(hashBlock, keyPair.d, keyPair.n)

with open("prevHash.csv", "w") as hashFile:
    hashFile.write(curBlock.curHash)

    #saves data in a csv
with open("data_logV2.csv", "a") as file:
    file.write("PrevHash: " + curBlock.prevHash + 
        " \tTimeStamp: " + curBlock.timestamp + " \tEvent: " + curBlock.event + 
            " \tStatus: " + str(curBlock.statusFlag) + " \tHash: " + curBlock.curHash + "\n")

#dataString = dataString + ' ' + str(curBlock.curHash)
#message = dataString.encode('utf8')
#cryptMessage = rsa.encrypt(message, pi1_priv)

with open("cheatKeys.csv", "r") as keyFile:
    recvkeyd = keyFile.readline()
    recvkeyn = keyFile.readline()
    recvkeye = keyFile.readline()


cmpHash = int.from_bytes(sha256(dataStringEnc).digest(), byteorder='big')
decrMsg = pow(signature, int(recvkeye), int(recvkeyn))
print("\nSignature Valid: ", cmpHash == decrMsg)
print(hex(cmpHash) + '\n')
print(hex(decrMsg))
#DECRYPT

#pubKey = rsa.PublicKey.load_pkcs1(recvkey)
#messageDec = rsa.decrypt(cryptMessage, pubKey)

#with open("captureOutput.csv", "a") as outFile:
#    outFile.write(messageDec)