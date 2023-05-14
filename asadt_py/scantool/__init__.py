import os
import PySimpleGUI as sg
import tomllib
import subprocess
from termcolor import colored
import re


def verify_module_integrity():

    global modroot; modroot = os.getcwd() + "/asadt_py/scantool"



def get_cnf(toolname):

    global cnf_dir; cnf_dir= os.getcwd() + "/config"
    global cnf_fileid; cnf_fileid = cnf_dir + "/scantool/" + toolname + ".toml"

    with open(cnf_fileid, 'rb') as cnf_currenttool:

        global current_script_configuration; current_script_configuration = tomllib.load(cnf_currenttool)

    if toolname == "nmap":

        ## Script Info Parse ##
        global script_name_nmap; script_name_nmap = current_script_configuration["ScriptInfo"]["script_id"]
        global script_version_nmap; script_version_nmap = current_script_configuration["ScriptInfo"]["script_version"]

        ## Script Enablers Parse ##
        global scriptenabler_nmap; scriptenabler_nmap = current_script_configuration["ScriptEnablers"]["nmap_enable"]
        global scriptenabler_updatedb; scriptenabler_updatedb = current_script_configuration["ScriptEnablers"]["nmap_updatedb"]
        global scriptenabler_fastscan; scriptenabler_fastscan = current_script_configuration["ScriptEnablers"]["nmap_fastscan_enable"]
        global scriptenabler_traceroute; scriptenabler_traceroute = current_script_configuration["ScriptEnablers"]["nmap_traceroute_enable"]
        global scriptenabler_fullscan; scriptenabler_fullscan = current_script_configuration["ScriptEnablers"]["nmap_fullscan_enable"]
        global scriptenabler_nsescriptscan; scriptenabler_nsescriptscan = current_script_configuration["ScriptEnablers"]["nmap_nsescriptscan_enable"]
        global scriptenabler_nsedebug; scriptenabler_nsedebug = current_script_configuration["ScriptEnablers"]["nmap_nsedebug_enable"]
        
        ## Script Output Parse ##
        global scriptoutput_fastscan; scriptoutput_fastscan = current_script_configuration["ScriptOutput"]["nmap_fastscan_output_filename"]
        global scriptoutput_traceroute; scriptoutput_traceroute = current_script_configuration["ScriptOutput"]["nmap_traceroute_output_filename"]
        global scriptoutput_fullscan; scriptoutput_fullscan = current_script_configuration["ScriptOutput"]["nmap_fullscan_output_filename"]
        global scriptoutput_nsescriptscan; scriptoutput_nsescriptscan = current_script_configuration["ScriptOutput"]["nmap_nsescriptscan_output_filename"]

    if toolname == "assetfinder":

        ## Script Info Parse ##
        global script_name_assetfinder; script_name_assetfinder = current_script_configuration["ScriptInfo"]["script_id"]
        global script_version_assetfinder; script_version_assetfinder = current_script_configuration["ScriptInfo"]["script_version"]

        ## Script Enablers Parse ##
        global scriptenabler_assetfinder; scriptenabler_assetfinder = current_script_configuration["ScriptEnablers"]["assetfinder_enable"]

    if toolname == "dmitry":

        ## Script Info Parse ##
        global script_name_dmitry; script_name_dmitry = current_script_configuration["ScriptInfo"]["script_id"]
        global script_version_dmitry; script_version_dmitry = current_script_configuration["ScriptInfo"]["script_version"]

        ## Script Enabler Parse ##
        global scriptenabler_dmitry; scriptenabler_dmitry = current_script_configuration["ScriptEnablers"]["dmitry_enable"]

        ## Script Output Parse ##
        global scriptoutput_dmitrydefault; scriptoutput_dmitrydefault = current_script_configuration["ScriptOutput"]["dmitry_default_output"]

    if toolname == "dnsmap":

        ## Script Info Parse ##
        global script_name_dnsmap; script_name_dnsmap = current_script_configuration["ScriptInfo"]["script_id"]
        global script_version_dnsmap; script_version_dnsmap = current_script_configuration["ScriptInfo"]["script_version"]

        ## Script Enabler Parse ##
        global scriptenabler_dnsmap; scriptenabler_dnsmap = current_script_configuration["ScriptEnablers"]["dnsmap_enable"]
        global scriptenabler_dnsmap_usewl; scriptenabler_dnsmap_usewl = current_script_configuration["ScriptEnablers"]["dnsmap_wordlists_enable"]

        ## Script Output Parse ##
        global scriptoutput_dnsmapformat; scriptoutput_dnsmapformat = current_script_configuration["ScriptOutput"]["dnsmap_output_format"]
        global scriptoutput_dnsmapdefault; scriptoutput_dnsmapdefault = current_script_configuration["ScriptOutput"]["dnsmap_default_output"]

    if toolname == "nikto":

        ## Script Info Parse ##
        global script_name_nikto; script_name_nikto = current_script_configuration["ScriptInfo"]["script_id"]
        global script_version_nikto; script_version_nikto = current_script_configuration["ScriptInfo"]["script_version"]

        ## Script Enabler Parse ##
        global scriptenabler_nikto; scriptenabler_nikto = current_script_configuration["ScriptEnablers"]["nikto_enable"]
        global scriptenabler_nikto_defaultdisplay; scriptenabler_nikto_defaultdisplay = current_script_configuration["ScriptEnablers"]["nikto_defaultdisplay"]
        global scriptenabler_nikto_follow3xredir; scriptenabler_nikto_follow3xredir = current_script_configuration["ScriptEnablers"]["nikto_follow3xredir"]
        global scriptenabler_nikto_maxscantime; scriptenabler_nikto_maxscantime = current_script_configuration["ScriptEnablers"]["nikto_maxscantime"]
        global scriptenabler_nikto_forcessl; scriptenabler_nikto_forcessl = current_script_configuration["ScriptEnablers"]["nikto_forcessl"]
        global scriptenabler_nikto_disablednslookup; scriptenabler_nikto_disablednslookup = current_script_configuration["ScriptEnablers"]["nikto_disablednslookup"]
        global scriptenabler_nikto_conntimeout; scriptenabler_nikto_conntimeout = current_script_configuration["ScriptEnablers"]["nikto_conntimeout"]
        global scriptenabler_nikto_usecookies; scriptenabler_nikto_usecookies = current_script_configuration["ScriptEnablers"]["nikto_usecookies"]
        global scriptenabler_nikto_nointeractive; scriptenabler_nikto_nointeractive = current_script_configuration["ScriptEnablers"]["nikto_nointeractive"]
        global scriptenabler_nikto_no404guess; scriptenabler_nikto_no404guess = current_script_configuration["ScriptEnablers"]["nikto_no404guess"]
        
        ## Script Output Parse ##
        global scriptoutput_niktoformat; scriptoutput_niktoformat = current_script_configuration["ScriptOutput"]["nikto_output_format"]
        global scriptoutput_niktodefault; scriptoutput_niktodefault = current_script_configuration["ScriptOutput"]["nikto_default_output"]



def edit_cnf(cnf_fileid):

    command_to_execute = "nano --nonewlines +5 " + cnf_fileid
    subprocess.call(command_to_execute, shell=True)

    SystemExit(1)



def execerror(errorid):

    if errorid == "missingdir":

        if not diroutpath:

            print("")
            print(colored('Error, No Output Directory Was Defined Via The GUI!', color="red", attrs=["bold"]))
            print("")

            raise SystemExit(2)

    if errorid == "notarget":

        print("")
        print(colored('Error, No Target Address Was Defined Via The GUI!', color="red", attrs=["bold"]))
        print("")

        raise SystemExit(2)

    if errorid == "checkdirlock":
                        
        if os.path.isdir(diroutpath):

            pathdir = "Output Steam @ " + diroutpath + " Is Usable!"
                            
            print("")
            print(colored(pathdir, color="green", attrs=["bold"]))
            print("")

        else:

            pathdir = "Output Steam @ " + diroutpath + " Is Non Existent!"
            makepath = "mkdir -p " + diroutpath

            print("")
            print(colored(pathdir, color="red", attrs=["bold"]))
            print(colored('Input "yes" To Create Missing Directory, Or "exit" To Quit.', color="blue", attrs=["bold"]))
            print("")

            dirinput = input(colored('Input "yes" or "exit" To Continue: ', color="red", attrs=["bold"]))

            if dirinput == "yes":

                pathdir = "Output Steam @ " + diroutpath + " Is Now Created"

                try:

                    print("")
                    print(colored(pathdir, color="blue", attrs=["bold"]))
                
                    subprocess.call(makepath, shell=True)

                except:

                    print("")
                    print(colored('Error: Could Not Create Directory Using "mkdir -p"... Missing Perms???', color="red", attrs=["bold"]))

                    raise SystemExit(3)

            else:

                raise SystemExit(1)

    if errorid == "dnsmap_formaterror":

        print("")
        print(colored('Script Exec Error: Cannot Parse Current Output Format!', color="red", arrts=["bold"]))
        print("")

        raise SystemExit(3)
    
    if errorid == "noport":

        print("")
        print(colored('Script Exec Error: Cannot Parse Current Output Format!', color="red", arrts=["bold"]))
        print("")

        raise SystemExit(2)



def execute(toolname):

    ## Globalize Input Variables For Error Handling

    global diroutpath
    global targetaddr
    global scriptmethods

    get_cnf(toolname)

    if toolname == "nmap":

        layout_nmap = [
                      [sg.Text("Enter Target IP Address, NetBlock or IP Range", background_color="black", text_color="red")],     # Part 2 - The Layout
                      [sg.Input(background_color="black", text_color="red")],
                      [sg.Text("NSE Script Scan Method(s) [default='default']", background_color="black", text_color="red")],
                      [sg.Input(background_color="black", text_color="red")],
                      [sg.Text("Output Directory (directory)", background_color="black", text_color="red")],
                      [sg.Input(background_color="black", text_color="red")],
                      [sg.Text("🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹", background_color="black", text_color="red")],
                      [sg.Button('Execute', border_width="0px", mouseover_colors=["black","red"], button_color=["red","black"]),
                      sg.Button('Edit Configuration', border_width="0px", mouseover_colors=["black","red"], button_color=["red","black"]),
                      sg.Button('Quit', border_width="0px", mouseover_colors=["black","red"])]
                      ]

        # Create the window
        window = sg.Window(
                          'Enter "nmap" Script Variables',
                          layout_nmap,
                          titlebar_text_color="red",
                          titlebar_background_color="black",
                          background_color="black",
                          right_click_menu_text_color="red",
                          button_color=["red","black"],
                          auto_size_buttons=True,
                          )
        
        while True:

            event, values = window.read()

            if event == sg.WINDOW_CLOSED or event == 'Quit' or event == 'Edit Configuration':

                if event == 'Edit Configuration':

                    window.close()

                    edit_cnf(cnf_fileid)

                    break

                else:

                    break
            
            else:

                event, values = window.read()

                window.close()

                diroutpath = values[2]
                targetaddr = values[0]
                scriptmethods = values[1]

                if not values[0]:

                    execerror(errorid="notarget")

                if not values[1]:

                    if scriptenabler_nsescriptscan == "True":

                        values[1] = "default"

                        warningtext = "Value [1] Now Equals " + values[1]
                        print("")
                        print(colored('Warning, Value [1] Was Empty! Value [1] Is Required By "scriptenabler_nsescriptscan"', color="yellow", attrs=["bold"]))
                        print(colored(warningtext, color="yellow", attrs=["bold"]))
                        print("")

                if not values[2]:

                    execerror(errorid="missingdir")
                    
                else:
                        
                    execerror(errorid="checkdirlock")
                        
                if scriptenabler_nmap == "True":

                    if scriptenabler_updatedb == "True":

                        print("")
                        print(colored('Updating NSE Script Database', color="red", attrs=["bold"]))
                        print(colored('🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹', color="red", attrs=["bold"]))

                        subprocess.call('nmap --script-updatedb', shell=True)

                    if scriptenabler_fastscan == "True":

                        print("")
                        print(colored('Executing NMap Fast Scan Function', color="red", attrs=["bold"]))
                        print(colored('🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹', color="red", attrs=["bold"]))

                        outfile = values[2] + "/" + scriptoutput_fastscan
                        command_to_execute = "nmap -F -oN " + outfile + " " + values[0]
                        subprocess.call(command_to_execute, shell=True)

                    if scriptenabler_traceroute == "True":

                        print("")
                        print(colored('Executing NMap TraceRoute Scan Function', color="red", attrs=["bold"]))
                        print(colored('🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹', color="red", attrs=["bold"]))

                        outfile = values[2] + "/" + scriptoutput_traceroute
                        command_to_execute = "nmap --traceroute -oN " + outfile + " " + values[0]
                        subprocess.call(command_to_execute, shell=True)

                    if scriptenabler_fullscan == "True":

                        print("")
                        print(colored('Executing NMap FullScan Function', color="red", attrs=["bold"]))
                        print(colored('🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹', color="red", attrs=["bold"]))

                        outfile = values[2] + "/" + scriptoutput_fullscan
                        command_to_execute = "nmap -v -p 1-65535 -sV -O -sS -T5 -oN " + outfile + " " + values[0]
                        subprocess.call(command_to_execute, shell=True)

                    if scriptenabler_nsescriptscan == "True":

                        print("")
                        print(colored('Executing NMap NSE Script Scan Function', color="red", attrs=["bold"]))
                        print(colored('🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹', color="red", attrs=["bold"]))

                        outfile = values[2] + "/" + scriptoutput_nsescriptscan
                        command_to_execute = "nmap -v --script=" + values[1] + " -oN " + outfile + " " + values[0]
                        subprocess.call(command_to_execute, shell=True)

    if toolname == "assetfinder":

        layout_assetfinder = [
                             [sg.Text("Enter Domain Name or Hostname", background_color="black", text_color="red")],     # Part 2 - The Layout
                             [sg.Input(background_color="black", text_color="red")],
                             [sg.Checkbox(" Find Subdomains Only", default=False, checkbox_color="black", background_color="black", text_color="red")],
                             [sg.Text("🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹", background_color="black", text_color="red")],
                             [sg.Button('Execute', border_width="0px", mouseover_colors=["black","red"], button_color=["red","black"]),
                             sg.Button('Edit Configuration', border_width="0px", mouseover_colors=["black","red"], button_color=["red","black"]),
                             sg.Button('Quit', border_width="0px", mouseover_colors=["black","red"])]
                             ]

        # Create the window
        window = sg.Window(
                          'Enter "assetfinder" Script Variables',
                          layout_assetfinder,
                          titlebar_text_color="red",
                          titlebar_background_color="black",
                          background_color="black",
                          right_click_menu_text_color="red",
                          button_color=["red","black"],
                          auto_size_buttons=True,
                          )
        
        while True:

            event, values = window.read()

            if event == sg.WINDOW_CLOSED or event == 'Quit' or event == 'Edit Configuration':

                if event == 'Edit Configuration':

                    window.close()

                    edit_cnf(cnf_fileid)

                    break

                else:

                    break
            
            else:

                event, values = window.read()

                window.close()

                targetaddr = values[0]

                if not values[0]:

                    execerror(errorid="missingdir")

                if scriptenabler_assetfinder == "True":

                    if values[1] == "True":

                        print("")
                        print(colored('Executing AssetFinder (Subs Only) Scan Script', color="red", attrs=["bold"]))
                        print(colored('🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹', color="red", attrs=["bold"]))

                        command_to_execute = "assetfinder --subs-only " + values[0]
                        subprocess.call(command_to_execute, shell=True)

                    else:

                        print("")
                        print(colored('Executing AssetFinder Scan Script Script', color="red", attrs=["bold"]))
                        print(colored('🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹', color="red", attrs=["bold"]))
                            
                        command_to_execute = "assetfinder " + values[0]
                        subprocess.call(command_to_execute, shell=True)

    if toolname == "dmitry":

        layout_dmitry = [
                             [sg.Text("Enter Domain Name or Hostname", background_color="black", text_color="red")],     # Part 2 - The Layout
                             [sg.Input(background_color="black", text_color="red")],
                             [sg.Text("Output Directory (directory)", background_color="black", text_color="red")],     # Part 2 - The Layout
                             [sg.Input(background_color="black", text_color="red")],
                             [sg.Text("🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹", background_color="black", text_color="red")],
                             [sg.Button('Execute', border_width="0px", mouseover_colors=["black","red"], button_color=["red","black"]),
                             sg.Button('Edit Configuration', border_width="0px", mouseover_colors=["black","red"], button_color=["red","black"]),
                             sg.Button('Quit', border_width="0px", mouseover_colors=["black","red"])]
                             ]

        # Create the window
        window = sg.Window(
                          'Enter "dmitry" Script Variables',
                          layout_dmitry,
                          titlebar_text_color="red",
                          titlebar_background_color="black",
                          background_color="black",
                          right_click_menu_text_color="red",
                          button_color=["red","black"],
                          auto_size_buttons=True,
                          )
        
        while True:

            event, values = window.read()

            if event == sg.WINDOW_CLOSED or event == 'Quit' or event == 'Edit Configuration':

                if event == 'Edit Configuration':

                    window.close()

                    edit_cnf(cnf_fileid)

                    break

                else:

                    break
            
            else:

                event, values = window.read()

                diroutpath = values[1]
                targetaddr = values[0]

                window.close()

                if not values[0]:

                    execerror(errorid="notarget")

                if not values[1]:

                    execerror(errorid="missingdir")

                else:
                    
                    execerror(errorid="checkdirlock")

                if scriptenabler_dmitry == "True":

                    print("")
                    print(colored('Executing Dmitry Scan Script', color="red", attrs=["bold"]))
                    print(colored('🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹', color="red", attrs=["bold"]))

                    outfile = values[1] + "/" + scriptoutput_dmitrydefault
                    command_to_execute = "dmitry -winsep " + values[0] + " -o " + outfile
                    subprocess.call(command_to_execute, shell=True)

    if toolname == "dnsmap":

        layout_dnsmap = [
                             [sg.Text("Enter Domain Name or Hostname", background_color="black", text_color="red")],     # Part 2 - The Layout
                             [sg.Input(background_color="black", text_color="red")],
                             [sg.Text("Wordlist File (optional)", background_color="black", text_color="red")],     # Part 2 - The Layout
                             [sg.Input(background_color="black", text_color="red")],
                             [sg.Text("Output Directory (directory)", background_color="black", text_color="red")],     # Part 2 - The Layout
                             [sg.Input(background_color="black", text_color="red")],
                             [sg.Text("🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹", background_color="black", text_color="red")],
                             [sg.Button('Execute', border_width="0px", mouseover_colors=["black","red"], button_color=["red","black"]),
                             sg.Button('Edit Configuration', border_width="0px", mouseover_colors=["black","red"], button_color=["red","black"]),
                             sg.Button('Quit', border_width="0px", mouseover_colors=["black","red"])]
                             ]

        # Create the window
        window = sg.Window(
                          'Enter "dmitry" Script Variables',
                          layout_dnsmap,
                          titlebar_text_color="red",
                          titlebar_background_color="black",
                          background_color="black",
                          right_click_menu_text_color="red",
                          button_color=["red","black"],
                          auto_size_buttons=True,
                          )
        
        while True:

            event, values = window.read()

            if event == sg.WINDOW_CLOSED or event == 'Quit' or event == 'Edit Configuration':

                if event == 'Edit Configuration':

                    window.close()

                    edit_cnf(cnf_fileid)

                    break

                else:

                    break
            
            else:

                event, values = window.read()

                diroutpath = values[2]
                targetaddr = values[0]

                window.close()

                if not values[0]:

                    execerror(errorid="notarget")

                if not values[2]:

                    execerror(errorid="missingdir")

                else:
                    
                    execerror(errorid="checkdirlock")

                if values[1]:

                    try:

                        wlfile = open(values[1], "r")

                    except:

                        print("")
                        print(colored('Error: Could Not Access Specified Wordlist File! Missing Perms???', color="red", attrs=["bold"]))
                        print("")

                        raise SystemExit(3)

                    
                
                if scriptenabler_dnsmap == "True":

                    if scriptenabler_dnsmap_usewl == "True":

                        if values[1]:

                            if scriptoutput_dnsmapformat == "csv":

                                print("")
                                print(colored('Executing DNSMap Scan Script', color="red", attrs=["bold"]))
                                print(colored('🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹', color="red", attrs=["bold"]))

                                outfile = values[2] + "/" + scriptoutput_dnsmapdefault
                                command_to_execute = "dnsmap " + values[0] + " -w " + values[1] + " -c " + outfile
                                subprocess.call(command_to_execute, shell=True)

                            else:

                                if scriptoutput_dnsmapformat == "regular":

                                    print("")
                                    print(colored('Executing DNSMap Scan Script', color="red", attrs=["bold"]))
                                    print(colored('🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹', color="red", attrs=["bold"]))

                                    outfile = values[2] + "/" + scriptoutput_dnsmapdefault
                                    command_to_execute = "dnsmap " + values[0] + " -w " + values[1] + " -r " + outfile
                                    subprocess.call(command_to_execute, shell=True)

                                else:

                                    execerror(errorid="dnsmap_formaterror")

                        else:

                            if scriptoutput_dnsmapformat == "csv":

                                print("")
                                print(colored('Executing DNSMap Scan Script', color="red", attrs=["bold"]))
                                print(colored('🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹', color="red", attrs=["bold"]))

                                outfile = values[2] + "/" + scriptoutput_dnsmapdefault
                                command_to_execute = "dnsmap " + values[0] + " -c " + outfile
                                subprocess.call(command_to_execute, shell=True)

                            else:

                                if scriptoutput_dnsmapformat == "regular":

                                    print("")
                                    print(colored('Executing DNSMap Scan Script', color="red", attrs=["bold"]))
                                    print(colored('🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹', color="red", attrs=["bold"]))

                                    outfile = values[2] + "/" + scriptoutput_dnsmapdefault
                                    command_to_execute = "dnsmap " + values[0] + " -r " + outfile
                                    subprocess.call(command_to_execute, shell=True)

                                else:

                                    execerror(errorid="dnsmap_formaterror")
    if toolname == "nikto":

        layout_nikto = [
                      [sg.Text("Enter Target IP Address, Domain Name Or Hostname*", background_color="black", text_color="red")],     # Part 2 - The Layout
                      [sg.Input(background_color="black", text_color="red")],
                      [sg.Text("Evasion Tactic (1,2,3,4,5,6,7,8,A,B Or nothing)**]", background_color="black", text_color="red")],
                      [sg.Input(background_color="black", text_color="red")],
                      [sg.Text("Port Numer (80, 443 or Any: 1-65535)", background_color="black", text_color="red")],
                      [sg.Input(background_color="black", text_color="red")],
                      [sg.Text("Use A Proxy (http://server:port)", background_color="black", text_color="red")],
                      [sg.Input(background_color="black", text_color="red")],
                      [sg.Text("Output Directory (directory)", background_color="black", text_color="red")],
                      [sg.Input(background_color="black", text_color="red")],
                      [sg.Text("🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹", background_color="black", text_color="red")],
                      [sg.Text("* - Cannot Be 'http://', Specifiy Https With Port", background_color="black", text_color="red")],
                      [sg.Text("** - Read 'nikto.help' For More Information", background_color="black", text_color="red")],
                      [sg.Button('Execute', border_width="0px", mouseover_colors=["black","red"], button_color=["red","black"]),
                      sg.Button('Edit Configuration', border_width="0px", mouseover_colors=["black","red"], button_color=["red","black"]),
                      sg.Button('Quit', border_width="0px", mouseover_colors=["black","red"])]
                      ]

        # Create the window
        window = sg.Window(
                          'Enter "nikto" Script Variables',
                          layout_nikto,
                          titlebar_text_color="red",
                          titlebar_background_color="black",
                          background_color="black",
                          right_click_menu_text_color="red",
                          button_color=["red","black"],
                          auto_size_buttons=True,
                          )
        
        while True:

            event, values = window.read()

            if event == sg.WINDOW_CLOSED or event == 'Quit' or event == 'Edit Configuration':

                if event == 'Edit Configuration':

                    window.close()

                    edit_cnf(cnf_fileid)

                    break

                else:

                    break
            
            else:

                event, values = window.read()

                window.close()

                diroutpath = values[4]
                targetaddr = values[0]

                if not values[0]:

                    execerror(errorid="notarget")

                if not values[2]:

                    execerror(errorid="noport")

                if not values[4]:

                    execerror(errorid="missingdir")

                else:
                    
                    execerror(errorid="checkdirlock")



                if scriptenabler_nikto == "True":

                    global command_var
                    command_var = script_name_nikto

                    if values[2] == "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "A" or "B":

                        command_var = command_var + "-evasion " + values[2]

                    if values [3]:

                        command_var = command_var = "-useproxy " + values[3] + " "

                    if scriptenabler_nikto_defaultdisplay == "1" or "2" or "3" or "4" or "D" or "E" or "P" or "S" or "V":

                        command_var = command_var + "-Display " + scriptenabler_nikto_defaultdisplay + " "

                    if scriptenabler_nikto_follow3xredir == "True":

                        command_var = command_var + "-followredirects" + " "

                    if scriptenabler_nikto_conntimeout:

                        command_var = command_var + "-timeout" + " " + scriptenabler_nikto_conntimeout + " "

                    if scriptenabler_nikto_nointeractive == "True":

                        command_var = command_var + "-nointeractive" + " "

                    if scriptenabler_nikto_disablednslookup == "True":

                        command_var = command_var + "-nolookup" + " "

                    if scriptenabler_nikto_usecookies == "True":

                        command_var = command_var + "-usecookies" + " "

                    if scriptenabler_nikto_maxscantime:

                        command_var = command_var + "-maxtime " + scriptenabler_nikto_maxscantime + " "

                    if scriptenabler_nikto_no404guess == "True":

                        command_var = command_var + "-no404" + " "

                    if values[2] == "443":

                        command_var = command_var + "-ssl " + "-h " + values[0] + " -port " + values[2] + " "

                    else:

                        if scriptenabler_nikto_forcessl == "True":

                            command_var = command_var + "-ssl " + "-h " + values[0] + " -port " + values[2] + " "

                        else:

                            command_var = command_var + "-h " + values[0] + " -port " + values[2] + " "


                    print("")
                    print(colored('Executing Nikto Scan Script', color="red", attrs=["bold"]))
                    print(colored('🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹🭹', color="red", attrs=["bold"]))
                    print("")
                    print(colored(command_var, color="red", attrs=["bold"]))
                    outfile = "-output " + values[4] + "/" + scriptoutput_niktodefault + " -F " + scriptoutput_niktoformat
                    command_to_execute = "nikto" + " " + command_var + "-C all " + outfile

                    subprocess.call(command_to_execute, shell=True)