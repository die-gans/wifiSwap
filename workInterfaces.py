from wlanAPI import*
from netshCommands import*


def main():
    if __name__ == '__main__':

        #print get_interface()
        import time
        test = get_BSSI()
        for i in range(0,3):
            time.sleep(0.5)
            oldTest = test
            test = get_BSSI()
            print ("Test: "+str(i))

            print (test)
    print ("End")

    connect_to_network("ASUS")  #connect to network using BSSID



main()