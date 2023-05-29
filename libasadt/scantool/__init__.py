
global module_name
global module_version

module_name = 'scantool'
module_version = 'v1.1.0'



try:

    import os
    import PySimpleGUI as guihandler
    import tomllib
    import subprocess
    from termcolor import colored
    import math

except:

    excepttext = ' Module Error: Module' + module_name + " " + module_version + ' Failed To Load!'
    print("")
    print(excepttext)
    print("")

    raise SystemExit(2)


def get_tool_configuration(tool_name):

    config_file_id = os.getcwd() + "/config/" + module_name + "/" + tool_name + ".toml"

    global script_name
    global script_version

    with open(config_file_id, 'rb') as cnf_currenttool:

        global current_script_configuration
        
        current_script_configuration = tomllib.load(cnf_currenttool)

    if tool_name == "nmap":



        script_name = current_script_configuration["ScriptInfo"]["script_id"]
        script_version = current_script_configuration["ScriptInfo"]["script_version"]

        global scriptenabler_nmap_host
        global scriptenabler_nmap_updatedb
        global scriptenabler_nmap_nsescriptscan
        global scriptenabler_nmap_nsedebug
        global scriptenabler_nmap_permuser
        global scriptoutput_nmap_fullscan

        scriptenabler_nmap_host = current_script_configuration["ScriptEnablers"]["nmap_enable"]
        scriptenabler_nmap_updatedb = current_script_configuration["ScriptEnablers"]["nmap_updatedb"]
        scriptenabler_nmap_nsescriptscan = current_script_configuration["ScriptEnablers"]["nmap_nsescriptscan_enable"]
        scriptenabler_nmap_nsedebug = current_script_configuration["ScriptEnablers"]["nmap_nsedebug_enable"]
        scriptenabler_nmap_permuser = current_script_configuration["ScriptEnablers"]["nmap_assumesudoperms_enable"]
        scriptoutput_nmap_fullscan = current_script_configuration["ScriptOutput"]["nmap_fullscan_output_filename"]

def check_output(errorid):

    if errorid == "missingdir":

        if not output_directory:

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
                        
        if os.path.isdir(output_directory):

            pathdir = "Output Steam @ " + output_directory + " Is Usable!"
                            
            print("")
            print(colored(pathdir, color="green", attrs=["bold"]))
            print("")

        else:

            pathdir = "Output Steam @ " + output_directory + " Is Non Existent!"
            makepath = "mkdir -p " + output_directory

            print("")
            print(colored(pathdir, color="red", attrs=["bold"]))
            print(colored('Input "yes" To Create Missing Directory, Or "exit" To Quit.', color="blue", attrs=["bold"]))
            print("")

            dirinput = input(colored('Input "yes" or "exit" To Continue: ', color="red", attrs=["bold"]))

            if dirinput == "yes":

                pathdir = "Output Steam @ " + output_directory + " Is Now Created"

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
    
    if errorid == "noport":

        print("")
        print(colored('Script Exec Error: No Port(s) Were Specified!', color="red", attrs=["bold"]))
        print("")

        raise SystemExit(2)
    
def edit_tool_configuration(tool_name):

    config_file_id = os.getcwd() + "/config/" + module_name + "/" + tool_name + ".toml"

    command_to_execute = "nano --nonewlines +5 " + config_file_id
    subprocess.call(command_to_execute, shell=True)

    raise SystemExit(0)

def execute(tool_name):

    global output_directory
    global targetaddress
    global targetport
    global host_command
    global traceroute_cmd

    host_command = tool_name + " "

    get_tool_configuration(tool_name)

    print("")
    print(colored('Happy Hacking! :P', color='red', attrs=["bold"]))
    print("")

    if tool_name == "nmap":

        nmap_scantype_dropdown_layout = ["TCP Syn Scan","Connect() Scan","ACK Scan","Window Scan","Maimon Scan", "UDP Scan", "TCP Null Scan", "FIN Scan", "Xmas Scan"]

        nmap_scrn1_layout = [

            [

                guihandler.Text(
                    
                    text='TARGET SPECIFICATION',
                    text_color='red',
                    background_color='black',
                    expand_x=True,
                    justification="center",
                    
                )

            ],
            [

                guihandler.Text(
                    
                    text='Enter Target Address*:',
                    text_color='red',
                    background_color='black',
                    expand_x=True,
                    justification="left",
                    tooltip='(Required) Accepted Parameters: \n\nIP Address: Ex. 10.0.0.1 \nIP Range: Ex. 10.0.0-255.1-254 \nHostname: Ex. scanme.nmap.org / odfsec.org \nNetBlock: Ex. 10.0.0.1/24'
                    
                ),

                guihandler.Input(
            
                    text_color='red',
                    background_color='black',
                    border_width=2,
                    justification="left"
                    
                )

            ],
            [

                guihandler.Text(
                    
                    text='Enter Target Port or Port Range*:',
                    text_color='red',
                    background_color='black',
                    expand_x=True,
                    justification="left",
                    tooltip='(Required) Accepted Parameters: \n\nSingular Port Number: Ex. 443 \nPort Selection: Ex. 80,443,53,22,21 \nPort Range: Ex. 1-65535 \n\nYou Can Also Specify Port Type:  \n"U:" for UDP \n"T:" for TCP \n"S:" for SCTP \nEx. U:22 or T:443. \nEx.T:443,80,22,8080,9090 etc.'
                    
                ),

                guihandler.Input(
            
                    text_color='red',
                    background_color='black',
                    border_width=2,
                    
                )

            ],
            [
                guihandler.Text(
                
                text="\n ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n SCAN TUNING OPTIONS",
                text_color='red',
                background_color='black',
                expand_x=True,
                justification="center",

                )

            ],
            [

                guihandler.Text(
            
                    text='NSE Script Scan Method(s):',
                    text_color='red',
                    background_color='black',
                    expand_x=True,
                    justification="left",
                    tooltip='Accepted Parameters: \n\nSingular Catagory:        By Script Type:        By Script Type Exclusion: \nauth                               intrusive                   not intrusive\nbroadcast                      safe                          not safe \nbrute                             default                       not default \ndiscovery \ndos \nexploit \nexternal \nfuzzer \nmalware \nversion \nvuln \n\nNote: Multi Catagory Execution Is Possible; Ex. vuln,dos,fuzzer \n(Must Include Comma "," Seperator)'

                ),

                guihandler.Input(
            
                    text_color='red',
                    background_color='black',
                    border_width=2,
                    justification="left"
                    
                )

            ],
            [

                guihandler.Text(
            
                    text='NSE Script Arguments (filename):',
                    text_color='red',
                    background_color='black',
                    expand_x=True,
                    justification="left",
                    tooltip='Accepted Parameters: \n\n Filename of arguments file for NSE Script Scan Methods. \nEx. /home/user/Documents/argfile.txt'

                ),

                guihandler.Input(
            
                    text_color='red',
                    background_color='black',
                    border_width=2,
                    justification="left"
                    
                )

            ],
            [

                guihandler.Checkbox(
            
                    text=' Enable Traceroute Scan',
                    checkbox_color='black',
                    background_color='black',
                    tooltip='alias nmap --traceroute {targetip} (On Screen Only - No Output)',
                    text_color='red'

                ),

                guihandler.Checkbox(
            
                    text=' Enable IPV6 Scanning',
                    checkbox_color='black',
                    background_color='black',
                    tooltip='alias -6',
                    text_color='red'

                ),

                guihandler.Checkbox(
            
                    text=' Enable OS Detection Guessing',
                    checkbox_color='black',
                    background_color='black',
                    tooltip='alias -O Switch',
                    text_color='red'

                )

            ],
            [

                guihandler.Text(
            
                    text='Service Version Scan Intesity:',
                    text_color='red',
                    background_color='black',
                    expand_x=False,
                    justification="left",
                    tooltip='Accepted Parameters: \n\nNumerical Option: \n-1   = DISABLED \n0-9 = Light Scan - Intense Scan \n\nDefault Value: 5'

                ),

                guihandler.Slider(
            
                    range=(-1,9),
                    text_color='red',
                    background_color='black',
                    trough_color='red',
                    orientation='horizontal',
                    default_value=5,
                    size=(40,20)

                )

            ],
            [

                guihandler.Text(
            
                    text='Scan Timing Preset:',
                    text_color='red',
                    background_color='black',
                    expand_x=False,
                    justification="left",
                    tooltip='Accepted Parameters: \n\nNumerical Option: \n0   = Slow Packet Send Speed \n5 = Send Packets As Fast As Possible \n\nDefault Value: 3'

                ),

                guihandler.Slider(
            
                    range=(0,5),
                    text_color='red',
                    background_color='black',
                    trough_color='red',
                    orientation='horizontal',
                    default_value=3,
                    size=(48,20)

                )

            ],
            [

                guihandler.Text(
                
                    text="\n ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n SPOOFING AND EVASION OPTIONS",
                    text_color='red',
                    background_color='black',
                    expand_x=True,
                    justification="center",

                )

            ],
            [

                guihandler.Text(
            
                    text='Spoof Source Address (ipaddr):',
                    text_color='red',
                    background_color='black',
                    expand_x=True,
                    justification="left",
                    tooltip='Accepted Parameters: \n\nIP Address: Ex. 192.342.84.109'

                ),

                guihandler.Input(
            
                    text_color='red',
                    background_color='black',
                    border_width=2,
                    justification="left"
                    
                ),

            ],
            [

                guihandler.Text(
            
                    text='Use Specified Source Port (port):',
                    text_color='red',
                    background_color='black',
                    expand_x=True,
                    justification="left",
                    tooltip='Accepted Parameters: \n\nPort Number: Ex. 443 \n\nAccepts: Any Port 1-65535'

                ),

                guihandler.Input(
            
                    text_color='red',
                    background_color='black',
                    border_width=2,
                    justification="left"
                    
                )

            ],
            [

                guihandler.Text(
            
                    text='Use A Proxy URL (url):',
                    text_color='red',
                    background_color='black',
                    expand_x=True,
                    justification="left",
                    tooltip='Accepted Parameters: \n\nURL/Domain: Ex. https://nmap.org'

                ),

                guihandler.Input(
            
                    text_color='red',
                    background_color='black',
                    border_width=2,
                    justification="left"
                    
                )

            ],
            [

                guihandler.Text(
            
                    text='Spoof MAC Address (macaddr):',
                    text_color='red',
                    background_color='black',
                    expand_x=True,
                    justification="left",
                    tooltip='Accepted Parameters: \n\nMAC Address: Ex. 00:B0:D0:63:C2:26'

                ),

                guihandler.Input(
            
                    text_color='red',
                    background_color='black',
                    border_width=2,
                    justification="left"
                    
                )

            ],
            [

                guihandler.Text(
            
                    text='Use A Specified Interface',
                    text_color='red',
                    background_color='black',
                    expand_x=True,
                    justification="left",
                    tooltip='Accepted Parameters: \n\nNetwork Interface ID: \nEx. eth0 \nEx. wlan0'

                ),

                guihandler.Input(
            
                    text_color='red',
                    background_color='black',
                    border_width=2,
                    justification="left"
                    
                )

            ],
            [

                guihandler.Checkbox(
            
                    text='Enable Bad CheckSums',
                    checkbox_color='black',
                    background_color='black',
                    tooltip='alias --badsum \n\nSend Packets With Bogus TCP/UDP/SCTP CheckSums',
                    text_color='red'

                )

            ],
            [

                guihandler.Text(
                
                text="\n\n",
                text_color='red',
                background_color='black',
                expand_x=True,
                justification="center",

                )

            ],
            [

                guihandler.Text(
            
                    text='Output Directory',
                    text_color='red',
                    background_color='black',
                    expand_x=True,
                    justification="left",
                    tooltip='Accepted Parameters: \n\nDirectory Name: Ex. /home/user/output/scantool/nmap \n\nDo NOT use end slash. \n\nTo Change Output Filename, Press {Edit Configuration}'

                ),

                guihandler.Input(
            
                    text_color='red',
                    background_color='black',
                    border_width=2,
                    justification="left"
                    
                )

            ],
            [

                guihandler.Text(
                
                    text="\n ━━━━━━━━━━━━━━━━━━━━━━",
                    text_color='red',
                    background_color='black',
                    expand_x=True,
                    justification="left",

                )

            ],
            [

                guihandler.Button(
            
                    button_text='Execute "NMAP"',
                    border_width=0,
                    button_color=["red","black"],
                    mouseover_colors=["black","red"]

                ),

                guihandler.Button(
            
                    button_text='Edit Configuration',
                    border_width=0,
                    button_color=["red","black"],
                    mouseover_colors=["black","red"]

                ),

                guihandler.Button(
            
                    button_text='Quit Program',
                    border_width=0,
                    button_color=["red","black"],
                    mouseover_colors=["black","red"]

                ),

                guihandler.Listbox(
                    
                    values=nmap_scantype_dropdown_layout,
                    select_mode='LISTBOX_SELECT_MODE_SINGLE',
                    default_values="TCP Syn Scan",
                    sbar_trough_color="black",
                    sbar_arrow_color="red",
                    sbar_frame_color="black",
                    sbar_background_color="black",
                    expand_x=True,
                    size=(2,2),
                    text_color="red",
                    background_color="black",
                    
                )


            ]
            
        ]

        nmap_scrn1 = guihandler.Window(
            
                                      'Enter Nmap Scan Variables',
                                      nmap_scrn1_layout,
                                      background_color='black',
                                      titlebar_text_color='red',
                                      resizable=True
                                      
                                      )

        while True:
            
            event, values = nmap_scrn1.read()
            
            if event == "Quit Program" or event == guihandler.WIN_CLOSED:



                break

            elif event == "Edit Configuration":

                nmap_scrn1.close()

                edit_tool_configuration(tool_name)

            elif event == 'Execute "NMAP"':

                nmap_scrn1.close()

                values[7] = math.trunc(values[7])
                values[8] = math.trunc(values[8])

                output_directory = values[15]
                targetaddress = values[0]
                targetport = values[1]

                if not values[0]:

                    check_output(errorid='notarget')

                if not values[1]:

                    check_output(errorid='noport')

                if not values[15]:

                    check_output(errorid='missingdir')

                else:

                    check_output(errorid='checkdirlock')

                if not values[2]:

                    if scriptenabler_nmap_nsescriptscan == "True":

                        values[2] = 'default'
                        print(colored(f'Warning: Missing Values For NSE Method: Using Default Value: "{values[2]}"', color='yellow', attrs=["bold"]))
                        
                    else:
                        
                        values[2] = ''

                print(colored('Generating Command... Please Wait...', color='blue', attrs=["bold"]))
                print("")
                
                if values[1]:

                    host_command = host_command + '-p "' + targetport +'" '

                if values[2]:

                    if scriptenabler_nmap_nsescriptscan == "True":

                        host_command = host_command + '--script="' + values[2] + '" '

                    if scriptenabler_nmap_nsedebug == "True":

                        host_command = host_command + "--script-trace "

                if values[3]:

                    if scriptenabler_nmap_nsescriptscan == "True":

                        host_command = host_command + "--script-args-file=" + '"' + values[3] + '" '

                if str(values[4]) == "True":

                    traceroute_cmd = "True"

                else:
                    
                    traceroute_cmd = "False"

                if values[5]:

                    host_command = host_command + "-6 "

                if str(values[6]) == "True":

                    host_command = host_command + "-O "

                if str(values[7]) == "-1":

                    host_command = host_command

                else:

                    host_command = host_command + "-sV " "--version-intensity " + str(values[7]) + " "

                if values[8]:

                    host_command = host_command + "-T" + str(values[8]) + " "

                if values[9]:

                    host_command = host_command + "-S " + values[9] + " "

                if values[10]:

                    host_command = host_command + "--source-port " + values[10] + " "

                if values[11]:

                    host_command = host_command + "--proxies " + values[11] + " "

                if values[12]:

                    host_command = host_command + '--spoof-mac "' + values[12] + '" '

                if values[13]:

                    host_command = host_command + "-e " + values[13] + " "

                if str(values[14]) == "True":

                    host_command = host_command + "--badsum "

                if str(values[16]) == "['TCP Syn Scan']":

                    host_command = host_command + "-sS "
                
                elif str(values[16]) == "['Connect() Scan']":

                    host_command = host_command + "-sT "

                elif str(values[16]) == "['ACK Scan']":

                    host_command = host_command + "-sA "

                elif str(values[16]) == "['Window Scan']":

                    host_command = host_command + "-sW "
                
                elif str(values[16]) == "['Maimon Scan']":

                    host_command = host_command + "-sM"

                elif str(values[16]) == "['UDP Scan']":

                    host_command = host_command + "-sU "
                
                elif str(values[16]) == "['TCP Null Scan']":

                    host_command = host_command + "-sN "

                elif str(values[16]) == "['FIN Scan']":

                    host_command = host_command + "-sF "

                elif str(values[16]) == "['Xmas Scan']":

                    host_command = host_command + "-sX "

                else:

                    print(colored(f'\nError: Could Not Parse Selected Scan Type... Exiting (2)"{targetaddress}"', color='red', attrs=["bold"]))

                    SystemExit(2)

                if scriptenabler_nmap_permuser == "True":

                    host_command = host_command + "--privileged "

                else:

                    host_command = host_command + "--unprivileged "

                if values[15]:

                    host_command = host_command + "-oN " + values[15] + "/" + scriptoutput_nmap_fullscan + " "

                if targetaddress:

                    host_command = host_command + targetaddress

                nmap_scrn1.close()

                if scriptenabler_nmap_updatedb == "True":

                    print(colored(f'\nChecking For NSE Script Database Updates "{targetaddress}"', color='red', attrs=["bold"]))
                    print(colored(f'━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n', color='red', attrs=["bold"]))

                    command_to_execute = tool_name + " --script-updatedb"
                    subprocess.call(command_to_execute, shell=True)

                if traceroute_cmd == "True":

                    print(colored(f'\nGathering Traceroute Data For Target "{targetaddress}"', color='red', attrs=["bold"]))
                    print(colored(f'━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n', color='red', attrs=["bold"]))

                    command_to_execute = tool_name + " --traceroute " + targetaddress
                    subprocess.call(command_to_execute, shell=True)

                if scriptenabler_nmap_host == "True":

                    command_to_execute = host_command

                    print(colored(f'\nExecuting Full Scan Against "{targetaddress}"', color='red', attrs=["bold"]))
                    print(colored(f'━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n', color='red', attrs=["bold"]))
                    print(colored(f'{command_to_execute}\n', color='red', attrs=["bold"]))
                    
                    subprocess.call(command_to_execute, shell=True)

                raise SystemExit(0)