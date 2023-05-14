#!/usr/bin/env python3

###########################
## ASADT Mark III Python ##
###########################

##################################################################################################
## Authors:                                                                                     ##
## @odf-community - Authors_ID: 1728984 9990909                                                 ##
##################################################################################################



## Import External Modules ##
##############################################################

try:

    import os
    import tomllib
    import argparse
    from termcolor import colored

    from asadt_py import prog_main as asadt3
    from asadt_py import scantool
    
except:

    errortext = "Prog Error: Failed To Import Required Dependencies!"
    print("")
    print(colored(errortext, 'red', attrs=["bold", ]))

##############################################################



## Capture Configuration ##
##############################################################

asadt3.checkperms() # Check SUID Status (UID On Execution Must = 0)
                    # Comment This Line Out To Disable SUID Checking
                    # This Will Disable The Requirement Of The Sudo Flag

global configfile; configfile = os.getcwd() + "/config/scriptinfo.toml"
global argument_parser; argument_parser = argparse.ArgumentParser()

try:

    checkfile_configurations = open(configfile, "r")

except:

    print("")
    print(colored('Prog Error: Failed To Capture Script Main Configuration @ config/scriptinfo.toml', color="red", attrs=["bold"]))
    print("")

    raise SystemExit(2)

else:

    with open(configfile, 'rb') as cnf_scriptinfo:

        global scriptinfo; scriptinfo = tomllib.load(cnf_scriptinfo)

        global scriptname_global; scriptname_global = scriptinfo["script_data"]["script_name"]
        global scriptversion_global; scriptversion_global = scriptinfo["script_data"]["script_version"]
        global scripttitle_global; scripttitle_global = scriptname_global + ' ' + "Version " + scriptversion_global
        global scriptdesc_global; scriptdesc_global = scriptinfo["script_data"]["script_desc"]
        global scriptdesc_vcmd; scriptdesc_vcmd = scriptdesc_global + " " + scriptversion_global


try:

    # Verify Module Root (scantool)
    scantool.verify_module_integrity

except:

    print("")
    print(colored('Prog Error: Could Not Verify Modules Integrity', color="red", attrs=["bold"]))
    print("")

    raise SystemExit(2)

##############################################################



## Argument Parser ##
##############################################################

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
    version=scriptdesc_vcmd,
    help="Show Program's Version Number + Name"

)

args = argument_parser.parse_args()

if args.v:

    asadt3.showbanner(scriptversion_global)

    raise SystemExit(1)

if args.scantool:

    if not args.tool_name:

        asadt3.showbanner(scriptversion_global)

        print(colored('Error: Missing Positional Arg @ args.tool_name', color="red", attrs=["bold"]))
        print(colored('Help: Execute asadt.py -h or --help', color="blue", attrs=["bold"]))

        raise SystemExit(2)

    if args.tool_name[0] == "nmap":

        scantool.execute(args.tool_name[0])
    
    else:

        if args.tool_name[0] == "assetfinder":

            scantool.execute(args.tool_name[0])

        else:

            if args.tool_name[0] == "dmitry":

                scantool.execute(args.tool_name[0])

            else:

                if args.tool_name[0] == "dnsmap":

                    scantool.execute(args.tool_name[0])

                else:

                    if args.tool_name[0] == "nikto":

                        scantool.execute(args.tool_name[0])

                    else:

                        asadt3.showbanner(scriptversion_global)

                        errortext = " Error: Module 'scantool' Does Not Accept Positional Arg {toolname}: " + args.tool_name[0]
                        print(colored(errortext, color="red", attrs=["bold"]))

                        raise SystemExit(2)
    
if args.tools:

    if args.tool_name:

        asadt3.showbanner(scriptversion_global)

        errortext = " Error: Switch '--tools' Does Not Accept Positional Arg {toolname}: " + args.tool_name[0]
        print(colored(errortext, color="red", attrs=["bold"]))

        raise SystemExit(2)
    
    else:
        
        asadt3.showbanner(scriptversion_global)
        asadt3.listtools(scriptversion_global)

        raise SystemExit(1)

if args.updatechk:

    if args.tool_name:

        asadt3.showbanner(scriptversion_global)

        errortext = " Error: Argument '--updatechk' Does Not Accept args.tool_name: " + args.tool_name[0]
        print(colored(errortext, color="red", attrs=["bold"]))

        raise SystemExit(2)
    
    else:

        asadt3.showbanner(scriptversion_global)

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

                    raise SystemExit(3)

            if scriptversion_new == scriptversion_global:

                print("")
                print(colored(' Update Check: No Updates Were Reported From Github!', color="green", attrs=["bold"]))
                print("")

                os.remove(newchkfile)

                raise SystemExit(1)
            
            else:

                versionupdate = " Update Check: An Update For ASADT MK III Is Available! " + scriptversion_global + " => " + scriptversion_new
                downloadid = " Download Here: " + "https://github.com/odf-community/ASADT3/releases/tag/v" + scriptversion_new

                print("")
                print(colored(versionupdate, color="yellow", attrs=["bold"]))
                print(colored(downloadid, color="blue", attrs=["bold"]))

                os.remove(newchkfile)

                raise SystemExit(1)

##############################################################