#!/usr/bin/env python3

###########################
## ASADT Mark III Python ##
###########################

#############################################################################
#      This Repository Utilizes The GNU General Public License v3           #
#                                                                           #
#     As a sole actor, you are authorized to redistribute the data          #
#    of this repository as long as you follow the proper guidelines         #
# of the GNU GPLv3 License, and you do not redistribute for the purpose     #
# of financial, commerciality, marketability, or otherwise profitable gain  #
#############################################################################

##################################################################################################
## Author: @odf-community                                                                       ##
##                                                                                              ##
## ODFSEC Developer ID's: 9990909 (secops@odfsec.org)                                           ##
## Signed GPG ID's: 685619EDCE460E26 (secops@odfsec.org)                                        ##
##################################################################################################



## Import Local Modules ##
##################################################################################################

try:

    import os
    import tomllib
    import argparse
    from termcolor import colored

    from libasadt import prog_main as asadt3
    from libasadt import scantool 

except:

    print("")
    print(colored('Python3 Import Error!', color='red', attrs=["bold"]))
    print(colored('There was an error importing one or more required script modules!', color='red', attrs=["bold"]))
    print("")
    print(colored('Error Information: Execute setup.sh To Fix This Issue', color='blue', attrs=["bold"]))
    print("")

    raise SystemExit(2)

##################################################################################################



## Parse Script Host Configuration ##
##################################################################################################

asadt3.checkperms() # Check SUID Status (UID On Execution Must = 0)
                    # Comment This Line Out To Enable Sudo Disengage Mode
                    # This Will Disable The Requirement Of The Sudo Flag

global hostscript_name
global hostscript_version
global hostscript_description
global hostscript_readmefile
global hostscript_authors
global version_output

hostscript_name, hostscript_version, hostscript_description, hostscript_readmefile, hostscript_authors = asadt3.get_host_configuration()

version_output = hostscript_name + " | v" + hostscript_version + ' [GPG SIG: ' + hostscript_authors + "]"

##################################################################################################



## Parse Script Arguments ##
##################################################################################################

global argument_parser

argument_parser = argparse.ArgumentParser(
                                          description='Assistive Search And Discovery Tool Mark 3',
                                          epilog='Thank You For Using the ASADT MK III Beta Script'
                                         )


argument_parser.add_argument(

    "--scantool",
    action="store_true",
    help="Selects (tool_name) In The 'scantool' Module For Execution"

)

argument_parser.add_argument(

    "--tools",
    action="store_true",
    help="List Available Tools By Module Name"

)

argument_parser.add_argument(

    "--updatechk",
    action="store_true",
    help="Checks For Updates By Downloading The Newest ScriptInfo Configuration"

)

argument_parser.add_argument(

    "tool_name",
    nargs="*",
    help="Utility/Script To be Executed (Used In Conjunction With --module_name)"

)

argument_parser.add_argument(

    "-v",
    action="store_true",
    help="Shows Program Version With Our Cool Banner :)"

)

argument_parser.add_argument(

    "--version",
    action="version",
    version=version_output,
    help="Show Program's Name, Version & Authors"

)

args = argument_parser.parse_args()

if args.v:

    asadt3.showbanner(hostscript_version, formattype="normal")

    raise SystemExit(0)

if args.scantool:

    if not args.tool_name:

        asadt3.showbanner(hostscript_version, formattype="short")

        print(colored('Error: Missing Positional Arg @ args.tool_name', color="red", attrs=["bold"]))
        print(colored('Help: Execute asadt.py -h or --help', color="blue", attrs=["bold"]))

        raise SystemExit(2)
    
    else:

        asadt3.showbanner(hostscript_version,formattype="short")

    if args.tool_name[0] == "nmap":

        scantool.execute(args.tool_name[0])

    elif args.tool_name[0] == "assetfinder":

        scantool.execute(args.tool_name[0])

    elif args.tool_name[0] == "dmitry":

        scantool.execute(args.tool_name[0])

    elif args.tool_name[0] == "dnsmap":

        scantool.execute(args.tool_name[0])

    elif args.tool_name[0] == "nikto":

        scantool.execute(args.tool_name[0])

    else:

        asadt3.showbanner(hostscript_version, formattype="short")

        errortext = " Error: Module 'scantool' Does Not Accept Positional Arg {tool_name}: " + args.tool_name[0]
        print(colored(errortext, color="red", attrs=["bold"]))
        print(colored(' Help: Use Switch "--tools" To Se Viable Tool Names!', color="blue", attrs=["bold"]))

        raise SystemExit(2)
    
if args.tools:

    if args.tool_name:

        asadt3.showbanner(hostscript_version, formattype="short")

        errortext = " Error: Switch '--tools' Does Not Accept Positional Arg {toolname}: " + args.tool_name[0]
        print(colored(errortext, color="red", attrs=["bold"]))
        print(colored(' The Switch "--tools" Does Not Accept Any Positional Arguments, Please Remove Positional Arguments!', color="blue", attrs=["bold"]))

        raise SystemExit(2)
    
    else:
        
        asadt3.showbanner(hostscript_version, formattype="short")
        asadt3.listtools(hostscript_version)

        raise SystemExit(1)
    
if args.updatechk:

    if args.tool_name:

        asadt3.showbanner(hostscript_version, formattype="short")

        errortext = " Error: Argument '--updatechk' Does Not Accept args.tool_name: " + args.tool_name[0]
        print(colored(errortext, color="red", attrs=["bold"]))

        raise SystemExit(2)
    
    else:

        asadt3.showbanner(hostscript_version, formattype="short")

        asadt3.DownloadUpdate("https://raw.githubusercontent.com/odf-community/ASADT3/main/config/scriptinfo.toml")

        global newchkfile; newchkfile= os.getcwd() + "/.newversion_scriptinfo.toml"
        
        try:

            checkfile_configurations = open(newchkfile, "r")

        except:

            print("")
            print(colored('Prog Error: Failed To Capture Script Main Configuration @ .newversion_scriptinfo.toml', color="red", attrs=["bold"]))
            print("")

            raise SystemExit(2)

        else:

            global scriptversion_new

            with open(newchkfile, 'rb') as newchkfile_update:

                try:

                    scriptinfo_new = tomllib.load(newchkfile_update)

                    scriptversion_new = scriptinfo_new["script_data"]["script_version"]
                
                except:

                    print("")
                    print(colored(' Update Check: Unable To Parse New Configuration... Not ".toml"???', color="red", attrs=["bold"]))
                    print("")

                    os.remove(newchkfile)

                    raise SystemExit(2)

            if scriptversion_new == hostscript_version:

                print("")
                print(colored(' Update Check: No Updates Were Reported From Github!', color="green", attrs=["bold"]))
                print("")

                os.remove(newchkfile)

                raise SystemExit(0)
            
            else:

                versionupdate = " Update Check: An Update For ASADT MK III Is Available! " + "v" + hostscript_version + " => " + "v" + scriptversion_new
                downloadid = " Download Here: " + "https://github.com/odf-community/ASADT3/archive/refs/tags/v" + scriptversion_new + ".zip"
                infolink = " Read More: " + "https://github.com/odf-community/ASADT3/releases/tag/v" + scriptversion_new
                repolink = " Clone Me!: git clone https://github.com/odf-community/ASADT3.git"
                
                print("")
                print(colored(versionupdate, color="yellow", attrs=["bold"]))
                print("")
                print(colored(downloadid, color="green", attrs=["bold"]))
                print(colored(repolink, color="green", attrs=["bold"]))
                print(colored(infolink, color="blue", attrs=["bold"]))

                os.remove(newchkfile)

                raise SystemExit(0)