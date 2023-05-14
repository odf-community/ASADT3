import os
import subprocess
from termcolor import colored
import requests



def showbanner(scriptversion_true):

    scriptversion_oncreate = "  🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹  ASADT3-v" + scriptversion_true 
    print("")
    print(colored('             (                ( ', color="red", attrs=["bold"]))
    print(colored('     (       )\ )     (       )\ )     *   ) ', color="red", attrs=["bold"]))
    print(colored('     )\     (()/(     )\     (()/(     )  /( ', color="red", attrs=["bold"]))
    print(colored('  ((((_)(    /(_)) ((((_)(    /(_))   ( )(_))  ⌠A⌡ssistive M', color="red", attrs=["bold"]))
    print(colored('   )\ _ )\  (_))    )\ _ )\  (_))_   (_(_())   ⌠S⌡earch    A', color="red", attrs=["bold"]))
    print(colored('   (_)_\(_) / __|   (_)_\(_)  |   \  |_   _|   ⌠A⌡nd       R', color="red", attrs=["bold"]))
    print(colored('    / _ \   \__ \    / _ \    | |) |   | |     ⌠D⌡iscovery K', color="red", attrs=["bold"]))
    print(colored('   /_/ \_\  |___/   /_/ \_\   |___/    |_|     ⌠T⌡ool      3', color="red", attrs=["bold"]))
    print(colored(scriptversion_oncreate, color="red", attrs=["bold"]))
    print(colored(' ⌠PROTECT THE INNOCENT⌡ ⌠PROTECT THE INTERNET⌡', color="red", attrs=["bold"]))
    print(colored('            ⌠PROTECT THE FUTURE⌡', color="red", attrs=["bold"]))
    print("")



def checkperms():

    if os.getuid() == 0:

       global _admin_bool; _admin_bool = "True"

    else:
        
        print("")
        print(colored('Warning: It Is Suggested To Use SUID When Executing This Script', color="red", attrs=["bold", ]))
        print(colored('         Failure To Do So May Result In Unsuccessful Tool Execution', color="red", attrs=["bold", ]))
        print("")
        print(colored('Suggested Fix: Execute With "sudo" Flag', color="blue", attrs=["bold", ]))
        print(colored('               Ex: sudo python asadt.py --help', color="blue", attrs=["bold", ]))
        print("")
        print(colored('               Or Comment Out Line "asadt3.checkperms()" In "asadt.py" ', color="blue", attrs=["bold", ]))
        print(colored('               To Disengange Sudo Mode (Not Suggested)', color="blue", attrs=["bold", ]))
        print("")
        
        editmodemsg = colored('Press Enter To Exit Script OR Type "edit" To Disengage Sudo Mode... ', color="red", attrs=["bold"])
        editmode_input = input(editmodemsg)

        if editmode_input == "edit":

            localscript = os.getcwd() + "/asadt.py"

            command_to_execute = "nano --nonewlines --softwrap +40 " + localscript
            subprocess.call(command_to_execute, shell=True)

            raise SystemExit(3)

        else:

            raise SystemExit(2)



def listtools(scriptversion_true):

    toolavail =  " Available Tools (As of v" + scriptversion_true + ")"

    print("")
    print(colored(toolavail, color="red", attrs=["bold"]))
    print("")
    print(colored(' Scantool Module (--scantool)', color="red", attrs=["bold"]))
    print(colored(' ┣ nmap', color="red", attrs=["bold"]))
    print(colored(' ┣ assetfinder', color="red", attrs=["bold"]))
    print(colored(' ┣ dmitry', color="red", attrs=["bold"]))
    print(colored(' ┣ dnsmap', color="red", attrs=["bold"]))
    print(colored(' ┣ nikto', color="red", attrs=["bold"]))
    print("")



def DownloadUpdate(url):

    local_filename = ".newversion_" + url.split('/')[-1]
    r = requests.get(url)
    f = open(local_filename, 'wb')

    for chunk in r.iter_content(chunk_size=512 * 1024): 

        if chunk:

            f.write(chunk)

    f.close()
    
    return