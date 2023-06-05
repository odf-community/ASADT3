###########################
## ASADT Mark III Python ##
###########################

#############################################################################
# This Repository Utilizes The GNU General Public License v3                #
#                                                                           #
# As a sole actor, you are authorized to redistribute the data              #
# of this repository as long as you follow the proper guidelines listed     #
# within the GNU GPLv3 License, and you do not redistribute for the purpose #
# of financial, commerciality, marketability, or otherwise profitable gain  #
#############################################################################

##################################################################################################
## Author: @odf-community                                                                       ##
##                                                                                              ##
## ODFSEC Developer ID's: 9990909 (secops@odfsec.org)                                           ##
## Signed GPG ID's: 685619EDCE460E26 (secops@odfsec.org)                                        ##
##################################################################################################



try:

    import os
    import subprocess
    import requests
    import tomllib
    from termcolor import colored

except:

    print("")
    print(colored('Python Import Error!', color='red', attrs=["bold"]))
    print(colored('There was an error importing one or more required script modules!', color='red', attrs=["bold"]))
    print("")
    print(colored('Error Information: Please ensure the Python dependencies "argparse" "termcolor" and "PySimpleGUI" have been properly met!', color='blue', attrs=["bold"]))
    print("")

    raise SystemExit(2)



def checkperms():

    if os.getuid() == 0:

       global admin_bool
       
       admin_bool = "True"

       return admin_bool

    else:
        
        print("")
        print(colored('Warning: It Is Suggested To Use SUID When Executing This Script', color="red", attrs=["bold", ]))
        print(colored('         Failure To Do So May Result In Unsuccessful Tool Execution', color="red", attrs=["bold", ]))
        print("")
        print(colored('Suggested Fix: Execute With "sudo" Flag', color="blue", attrs=["bold", ]))
        print(colored('               Ex: sudo ./asadt.py --help', color="blue", attrs=["bold", ]))
        print("")
        print(colored('               Or Comment Out Line "asadt3.checkperms()" In "asadt.py" ', color="blue", attrs=["bold", ]))
        print(colored('               To Disengange Sudo Mode (Not Suggested)', color="blue", attrs=["bold", ]))
        print("")
        
        editmodemsg = colored('Press Enter To Exit Script OR Type "edit" To Disengage Sudo Mode... ', color="red", attrs=["bold"])
        editmode_input = input(editmodemsg)

        if editmode_input == "edit":

            localscript = os.getcwd() + "/asadt.py"

            command_to_execute = "nano  --linenumbers --nonewlines --softwrap +56 " + str(f'"{localscript}"')
            subprocess.call(command_to_execute, shell=True)

            os.chmod(localscript, 0o751)

            raise SystemExit(0)

        else:

            raise SystemExit(2)



def get_host_configuration():

    config_fileid = os.getcwd() + "/config/scriptinfo.toml"

    with open(config_fileid, 'rb') as host_configuration_file:

        host_config = tomllib.load(host_configuration_file)

        hostscript_name = host_config['script_data']['script_name']
        hostscript_version = host_config['script_data']['script_version']
        hostscript_description = host_config['script_data']['script_desc']
        hostscript_readmefile = host_config['script_data']['script_readme']
        hostscript_authors = host_config['script_data']['script_authors']

    return hostscript_name, hostscript_version, hostscript_description, hostscript_readmefile, hostscript_authors



def showbanner(currentversion, formattype):

    if formattype == "normal":

        scriptversion_oncreate = '  ║        [v' + currentversion + '] [MARK III BETA]        ║'
        print("")
        print(colored('             (                ( ', color="red", attrs=["bold"]))
        print(colored('     (       )\ )     (       )\ )     *   ) ', color="red", attrs=["bold"]))
        print(colored('     )\     (()/(     )\     (()/(     )  /( ', color="red", attrs=["bold"]))
        print(colored('  ((((_)(    /(_)) ((((_)(    /(_))   ( )(_))  ⌠A⌡ssistive M', color="red", attrs=["bold"]))
        print(colored('   )\ _ )\  (_))    )\ _ )\  (_))_   (_(_())   ⌠S⌡earch    A', color="red", attrs=["bold"]))
        print(colored('   (_)_\(_) / __|   (_)_\(_)  |   \  |_   _|   ⌠A⌡nd       R', color="red", attrs=["bold"]))
        print(colored('    / _ \   \__ \    / _ \    | |) |   | |     ⌠D⌡iscovery K', color="red", attrs=["bold"]))
        print(colored('   /_/ \_\  |___/   /_/ \_\   |___/    |_|     ⌠T⌡ool      3', color="red", attrs=["bold"]))
        print(colored(' ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━', color="red", attrs=["bold"]))
        print(colored(' ⌠PROTECT THE INNOCENT⌡ ⌠PROTECT THE INTERNET⌡', color="red", attrs=["bold"]))
        print(colored('            ⌠PROTECT THE FUTURE⌡', color="red", attrs=["bold"]))
        print("")
        print(colored('  ╔════════════════════════════════════════╗', color="red", attrs=["bold"]))
        print(colored('  ║       Script Developed By ODFSEC       ║', color="red", attrs=["bold"]))
        print(colored(scriptversion_oncreate, color="red", attrs=["bold"]))
        print(colored('  ║                                        ║', color="red", attrs=["bold"]))
        print(colored('  ║           https://odfsec.org           ║', color="red", attrs=["bold"]))
        print(colored('  ║      W3 4R3 0DFS3C • iloveu=true       ║', color="red", attrs=["bold"]))
        print(colored('  ╚════════════════════════════════════════╝', color="red", attrs=["bold"]))

    if formattype == "short":

        scriptversion_oncreate = '  Assistive Search And Discovery Tool v' + currentversion

        print("")
        print(colored('   █████╗  ███████╗  █████╗  ██████╗  ████████╗', color="red", attrs=["bold"]))
        print(colored('  ██╔══██╗ ██╔════╝ ██╔══██╗ ██╔══██╗ ╚══██╔══╝', color="red", attrs=["bold"]))
        print(colored('  ███████║ ███████╗ ███████║ ██║  ██║    ██║', color="red", attrs=["bold"]))
        print(colored('  ██╔══██║ ╚════██║ ██╔══██║ ██║  ██║    ██║', color="red", attrs=["bold"]))
        print(colored('  ██║  ██║ ███████║ ██║  ██║ ██████╔╝    ██║', color="red", attrs=["bold"]))
        print(colored('  ╚═╝  ╚═╝ ╚══════╝ ╚═╝  ╚═╝ ╚═════╝     ╚═╝', color="red", attrs=["bold"]))
        print(colored(scriptversion_oncreate, color="red", attrs=["bold"]))
        print("")



def listtools(currentversion):

    toolavail =  " Available Tools (As of v" + currentversion + ")"

    print("")
    print(colored(toolavail, color="red", attrs=["bold"]))
    print("")
    print(colored(' Scantool Module (--scantool)', color="red", attrs=["bold"]))
    print(colored(' ┣ nmap', color="red", attrs=["bold"]))
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