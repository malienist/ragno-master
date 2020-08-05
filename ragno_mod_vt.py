#!/usr/bin/env python3
#
__author__ = "Vishal Thakur"
__copyright__ = "Copyright 2020, Vishal Thakur"
__license__ = "Apache2"
__version__ = "1.0"
__email__ = "vt@hack.sydney"
__status__ = "Prod"

import requests
import json
import time
class ExecuteIP:
    from config_reader import apiKeyVT
    global apiKeyVT
    def ioc_ip_single():
        ipAddress=input('Please provide IP for lookup: \n\n')
        relationship = input('Please select one option: \n\n'
                             ' Press 1 for Communicating Files: \n'
                             ' Press 2 for Downloaded Files: \n')

        if relationship == '1':
            # Create the ioc-list file
            from ragno_ops_file import ExecuteFileOpsComm
            ExecuteFileOpsComm.createList()

            relationship='communicating_files'
            url = "https://www.virustotal.com/api/v3/ip_addresses/" + ipAddress + '/' + relationship
            headers = {'x-apikey': apiKeyVT}
            params = {"limit": "10"}
            response = requests.get(url, headers=headers, params=params)
            json_response = response.json()

            # Start launching the webs
            print("Ragno is now casting 10 webs...\n")
            print("...wait for results.\n")
            time.sleep(1)

            print('Casting Web 1...\n')
            try:
                if 'network_infrastructure' in json_response['data'][0]['attributes']:
                    web = json_response['data'][0]['attributes']['network_infrastructure']
                    print('Web 1 results: \n')
                    print(json_response['data'][0]['attributes']['network_infrastructure'])
                    with open('IOC-list-communicating.txt', 'a+') as file:
                        json.dump(web, file)
                else:
                    print('Web did not find any Network-specific IOC.\n')
            except IndexError:
                print("Web didn't return any results. \n")

            print('Casting Web 2...\n')
            try:
                if 'network_infrastructure' in json_response['data'][1]['attributes']:
                    web = json_response['data'][1]['attributes']['network_infrastructure']
                    print('Web 2 results: \n')
                    print(json_response['data'][1]['attributes']['network_infrastructure'])
                    with open('IOC-list-communicating.txt', 'a+') as file:
                        json.dump(web, file)
                else:
                    print('Web did not find any Network-specific IOC.\n')
            except IndexError:
                print("Web didn't return any results. \n")

            print('Casting Web 3...\n')
            try:
                if 'network_infrastructure' in json_response['data'][2]['attributes']:
                    web = json_response['data'][2]['attributes']['network_infrastructure']
                    print('Web 3 results: \n')
                    print(json_response['data'][2]['attributes']['network_infrastructure'])
                    with open('IOC-list-communicating.txt', 'a+') as file:
                        json.dump(web, file)
                else:
                    print('Web did not find any Network-specific IOC.\n')
            except IndexError:
                print("Web didn't return any results. \n")

            print('Casting Web 4...\n')
            try:
                if 'network_infrastructure' in json_response['data'][3]['attributes']:
                    web = json_response['data'][3]['attributes']['network_infrastructure']
                    print('Web 4 results: \n')
                    print(json_response['data'][3]['attributes']['network_infrastructure'])
                    with open('IOC-list-communicating.txt', 'a+') as file:
                        json.dump(web, file)
                else:
                    print('Web did not find any Network-specific IOC.\n')
            except IndexError:
                print("Web didn't return any results. \n")

            print('Casting Web 5...\n')
            try:
                if 'network_infrastructure' in json_response['data'][4]['attributes']:
                    web = json_response['data'][4]['attributes']['network_infrastructure']
                    print('Web 5 results: \n')
                    print(json_response['data'][4]['attributes']['network_infrastructure'])
                    with open('IOC-list-communicating.txt', 'a+') as file:
                        json.dump(web, file)
                else:
                    print('Web did not find any Network-specific IOC.\n')
            except IndexError:
                print("Web didn't return any results. \n")

            print('Casting Web 6...\n')
            try:
                if 'network_infrastructure' in json_response['data'][5]['attributes']:
                    web = json_response['data'][5]['attributes']['network_infrastructure']
                    print('Web 6 results: \n')
                    print(json_response['data'][5]['attributes']['network_infrastructure'])
                    with open('IOC-list-communicating.txt', 'a+') as file:
                        json.dump(web, file)
                else:
                    print('Web did not find any Network-specific IOC.\n')
            except IndexError:
                print("Web didn't return any results. \n")

            print('Casting Web 7...\n')
            try:
                if 'network_infrastructure' in json_response['data'][6]['attributes']:
                    web = json_response['data'][6]['attributes']['network_infrastructure']
                    print('Web 7 results: \n')
                    print(json_response['data'][6]['attributes']['network_infrastructure'])
                    with open('IOC-list-communicating.txt', 'a+') as file:
                        json.dump(web, file)
                else:
                    print('Web did not find any Network-specific IOC.\n')
            except IndexError:
                print("Web didn't return any results. \n")

            print('Casting Web 8...\n')
            try:
                if 'network_infrastructure' in json_response['data'][7]['attributes']:
                    web = json_response['data'][7]['attributes']['network_infrastructure']
                    print('Web 8 results: \n')
                    print(json_response['data'][7]['attributes']['network_infrastructure'])
                    with open('IOC-list-communicating.txt', 'a+') as file:
                        json.dump(web, file)
                else:
                    print('Web did not find any Network-specific IOC.\n')
            except IndexError:
                print("Web didn't return any results. \n")

            print('Casting Web 9...\n')
            try:
                if 'network_infrastructure' in json_response['data'][8]['attributes']:
                    web = json_response['data'][8]['attributes']['network_infrastructure']
                    print('Web 9 results: \n')
                    print(json_response['data'][8]['attributes']['network_infrastructure'])
                    with open('IOC-list-communicating.txt', 'a+') as file:
                        json.dump(web, file)
                else:
                    print('Web did not find any Network-specific IOC.\n')
            except IndexError:
                print("Web didn't return any results. \n")

            print('Casting Web 10...\n')
            try:
                if 'network_infrastructure' in json_response['data'][9]['attributes']:
                    web = json_response['data'][9]['attributes']['network_infrastructure']
                    print('Web 10 results: \n')
                    print(json_response['data'][9]['attributes']['network_infrastructure'])
                    with open('IOC-list-communicating.txt', 'a+') as file:
                        json.dump(web, file)
                else:
                    print('Web did not find any Network-specific IOC.\n')
            except IndexError:
                print("Web didn't return any results. \n")

            # Fix the output file - re-format for easy-reading
            from ragno_ops_file import ExecuteFileOpsComm
            ExecuteFileOpsComm.formatList_1()
            ExecuteFileOpsComm.formatList_2()
            ExecuteFileOpsComm.formatList_3()

            output_results = input(
                'Results from all webs have been writen to IOC-list-communicating.txt in working directory.\n Press 1 to print the results to console: \n Press 2 to return to Main Menu: \n\n')
            if output_results == '1':
                with open('IOC-list-communicating.txt', 'r') as IOC:
                    print(IOC.read())
                    from ragno import Main
                    Main.main_menu()
            elif output_results == '2':
                from ragno import Main
                Main.main_menu()
            else:
                print('Invalid selection, exiting...')
                exit()
            return
        elif relationship =='2':
            relationship='downloaded_files'
            url = "https://www.virustotal.com/api/v3/ip_addresses/" + ipAddress + '/' + relationship

            headers = {'x-apikey': apiKeyVT}
            params = {"limit": "10"}
            response = requests.get(url, headers=headers, params=params)
            json_response = response.json()

            # Create the ioc-list file
            from ragno_ops_file import ExecuteFileOpsDownld
            ExecuteFileOpsDownld.createList()
            # Start the function
            print("Ragno is now casting 10 webs...\n")
            print("...wait for results.\n")
            time.sleep(1)

            print('Casting Web 1...\n')
            try:
                if 'names' in json_response['data'][0]['attributes']:
                    web = json_response['data'][0]['attributes']['names']
                    print('Web 1 results: \n')
                    print(json_response['data'][0]['attributes']['names'])
                    with open('IOC-list-downloaded.txt', 'a+') as file:
                        json.dump(web, file)
                else:
                    print('Web did not find any Network-specific IOC.\n')
            except IndexError:
                print("Web didn't return any results. \n")

            print('Casting Web 2...\n')
            try:
                if 'network_infrastructure' in json_response['data'][1]['attributes']:
                    web = json_response['data'][1]['attributes']['network_infrastructure']
                    print('Web 2 results: \n')
                    print(json_response['data'][1]['attributes']['network_infrastructure'])
                    with open('IOC-list-downloaded.txt', 'a+') as file:
                        json.dump(web, file)
                else:
                    print('Web did not find any Network-specific IOC.\n')
            except IndexError:
                print("Web didn't return any results. \n")

            print('Casting Web 3...\n')
            try:
                if 'network_infrastructure' in json_response['data'][2]['attributes']:
                    web = json_response['data'][2]['attributes']['network_infrastructure']
                    print('Web 3 results: \n')
                    print(json_response['data'][2]['attributes']['network_infrastructure'])
                    with open('IOC-list-downloaded.txt', 'a+') as file:
                        json.dump(web, file)
                else:
                    print('Web did not find any Network-specific IOC.\n')
            except IndexError:
                print("Web didn't return any results. \n")

            print('Casting Web 4...\n')
            try:
                if 'network_infrastructure' in json_response['data'][3]['attributes']:
                    web = json_response['data'][3]['attributes']['network_infrastructure']
                    print('Web 4 results: \n')
                    print(json_response['data'][3]['attributes']['network_infrastructure'])
                    with open('IOC-list-downloaded.txt', 'a+') as file:
                        json.dump(web_2, file)
                else:
                    print('Web did not find any Network-specific IOC.\n')
            except IndexError:
                print("Web didn't return any results. \n")

            print('Casting Web 5...\n')
            try:
                if 'network_infrastructure' in json_response['data'][4]['attributes']:
                    web = json_response['data'][4]['attributes']['network_infrastructure']
                    print('Web 5 results: \n')
                    print(json_response['data'][4]['attributes']['network_infrastructure'])
                    with open('IOC-list-downloaded.txt', 'a+') as file:
                        json.dump(web, file)
                else:
                    print('Web did not find any Network-specific IOC.\n')
            except IndexError:
                print("Web didn't return any results. \n")

            print('Casting Web 6...\n')
            try:
                if 'network_infrastructure' in json_response['data'][5]['attributes']:
                    web = json_response['data'][5]['attributes']['network_infrastructure']
                    print('Web 6 results: \n')
                    print(json_response['data'][5]['attributes']['network_infrastructure'])
                    with open('IOC-list-downloaded.txt', 'a+') as file:
                        json.dump(web, file)
                else:
                    print('Web did not find any Network-specific IOC.\n')
            except IndexError:
                print("Web didn't return any results. \n")

            print('Casting Web 7...\n')
            try:
                if 'network_infrastructure' in json_response['data'][6]['attributes']:
                    web = json_response['data'][6]['attributes']['network_infrastructure']
                    print('Web 7 results: \n')
                    print(json_response['data'][6]['attributes']['network_infrastructure'])
                    with open('IOC-list-downloaded.txt', 'a+') as file:
                        json.dump(web, file)
                else:
                    print('Web did not find any Network-specific IOC.\n')
            except IndexError:
                print("Web didn't return any results. \n")

            print('Casting Web 8...\n')
            try:
                if 'network_infrastructure' in json_response['data'][7]['attributes']:
                    web = json_response['data'][7]['attributes']['network_infrastructure']
                    print('Web 8 results: \n')
                    print(json_response['data'][7]['attributes']['network_infrastructure'])
                    with open('IOC-list-downloaded.txt', 'a+') as file:
                        json.dump(web, file)
                else:
                    print('Web did not find any Network-specific IOC.\n')
            except IndexError:
                print("Web didn't return any results. \n")

            print('Casting Web 9...\n')
            try:
                if 'network_infrastructure' in json_response['data'][8]['attributes']:
                    web = json_response['data'][8]['attributes']['network_infrastructure']
                    print('Web 9 results: \n')
                    print(json_response['data'][8]['attributes']['network_infrastructure'])
                    with open('IOC-list-downloaded.txt', 'a+') as file:
                        json.dump(web, file)
                else:
                    print('Web did not find any Network-specific IOC.\n')
            except IndexError:
                print("Web didn't return any results. \n")

            print('Casting Web 10...\n')
            try:
                if 'network_infrastructure' in json_response['data'][9]['attributes']:
                    web = json_response['data'][9]['attributes']['network_infrastructure']
                    print('Web 7 results: \n')
                    print(json_response['data'][9]['attributes']['network_infrastructure'])
                    with open('IOC-list-downloaded.txt', 'a+') as file:
                        json.dump(web, file)
                else:
                    print('Web did not find any Network-specific IOC.\n')
            except IndexError:
                print("Web didn't return any results. \n")

            # Fix the output file - re-format for easy-reading
            from ragno_ops_file import ExecuteFileOpsDownld
            ExecuteFileOpsDownld.formatList_1()
            ExecuteFileOpsDownld.formatList_2()
            ExecuteFileOpsDownld.formatList_3()

            output_results = input(
                'Results from all webs have been writen to IOC-list-downloaded.txt in working directory.\n Press 1 to print the results to console: \n Press 2 to return to Main Menu: \n\n')
            if output_results == '1':
                with open('IOC-list-downloaded.txt', 'r') as IOC:
                    print(IOC.read())
            elif output_results == '2':
                from ragno import Main
                Main.main_menu()
            else:
                print('Invalid selection, exiting...')
                exit()
            return
        else:
            print('Invalid selection, please try again: \n')
            from ragno import Main
            Main.main_menu()
            return

class ExecuteFileC2Infra:
    from config_reader import apiKeyVT
    global apiKeyVT
    def ioc_file_C2():
        id = input('Please provide File Hash for lookup: \n\n')
        print('\n\nExtracting Network IOC... \n')
        from ragno_ops_file import ExecuteFileOpsFileC2
        ExecuteFileOpsFileC2.createList()

        relationship = 'similar_files'

        # Extract network infra from similar files and append to output file
        url = "https://www.virustotal.com/api/v3/files/" + id + '/' + relationship
        headers = {'x-apikey': apiKeyVT}
        params = {"limit": "30"}
        response = requests.get(url, headers=headers, params=params)
        json_response = response.json()

        f = open('IOC-list-file_C2.txt', 'a+')
        f.write("\n\nC2 Information for the campaign - based on files similar to the one submitted:\n")
        f.close()
        # run the loop function to extract IOC - Similar Files
        for i in range(30):
            try:
                if 'network_infrastructure' in json_response['data'][i]['attributes']:
                    ioc = json_response['data'][i]['attributes']['network_infrastructure']
                    # print(json_response['data'][i]['attributes']['network_infrastructure'])
                    print('\n')
                    with open('IOC-list-file_C2.txt', 'a+') as file:

                        json.dump(ioc, file)
                else:
                    pass
            except IndexError:
                pass
        # Fix the output file - re-format for easy-reading
        from ragno_ops_file import ExecuteFileOpsFileC2
        ExecuteFileOpsFileC2.formatList_1()
        ExecuteFileOpsFileC2.formatList_2()
        ExecuteFileOpsFileC2.formatList_3()
        ExecuteFileOpsFileC2.formatList_4()
        ExecuteFileOpsFileC2.formatList_5()
        ExecuteFileOpsFileC2.formatList_6()

        output_results = input(
            'Extraction Complete! \n\nResults from all webs have been writen to IOC-list-file_C2.txt in working directory.\n Press 1 to view the results: \n Press 2 to return to Main Menu: \n\n')
        if output_results == '1':
            with open('IOC-list-file_C2.txt', 'r') as IOC:
                print(IOC.read())
                from ragno import Main
                Main.main_menu()
        elif output_results == '2':
            from ragno import Main
            Main.main_menu()
        else:
            print('Invalid selection, exiting...')
            exit()
        return

class ExecuteFileMultiAttr:
    from config_reader import apiKeyVT
    global apiKeyVT
    def ioc_file():
        id = input('Please provide File Hash for lookup: \n\n')
        from ragno_ops_file import ExecuteFileOpsFile
        ExecuteFileOpsFile.createList()

        relationship_1 = 'contacted_domains'
        relationship_2 = 'contacted_ips'
        relationship_3 = 'contacted_urls'
        relationship_4 = 'similar_files'
        relationship_5 = 'embedded_domains'


        # Extract contacted Domains and append to the output file
        url = "https://www.virustotal.com/api/v3/files/" + id + '/' + relationship_1
        headers = {'x-apikey': apiKeyVT}
        params = {"limit": "30"}
        response = requests.get(url, headers=headers, params=params)
        json_response = response.json()
        print('Contacted Domains: \n')
        #run the loop function to extract IOC - domains
        for i in range(30):
            try:
                if 'id' in json_response['data'][i]:
                    ioc = json_response['data'][i]['id']
                    #print(json_response['data'][i]['id'])
                    with open('IOC-list-file.txt', 'a+') as file:
                        json.dump(ioc, file)
                else:
                    pass
            except IndexError:
                pass

        #Extract contacted IPs and append to the output file


        url = "https://www.virustotal.com/api/v3/files/" + id + '/' + relationship_2
        headers = {'x-apikey': apiKeyVT}
        params = {"limit": "30"}
        response = requests.get(url, headers=headers, params=params)
        json_response = response.json()
        print('\n\nContacted IPs: \n')
        f = open('IOC-list-file.txt', 'a+')
        f.write("\n\n Contacted IPs: \n")
        f.close()
        #run the loop function to extract IOC - IPs
        for i in range(30):
            try:
                if 'id' in json_response['data'][i]:
                    ioc = json_response['data'][i]['id']
                    #print(json_response['data'][i]['id'])
                    with open('IOC-list-file.txt', 'a+') as file:

                        json.dump(ioc, file)
                else:
                    pass
            except IndexError:
                pass

        #Extract contacted URLs and append to output file
        url = "https://www.virustotal.com/api/v3/files/" + id + '/' + relationship_3
        headers = {'x-apikey': apiKeyVT}
        params = {"limit": "30"}
        response = requests.get(url, headers=headers, params=params)
        json_response = response.json()
        print('\n\nContacted URLs: \n')
        f = open('IOC-list-file.txt', 'a+')
        f.write("\n\n Contacted URLs: \n")
        f.close()
        # run the loop function to extract IOC - URLs
        for i in range(30):
            try:
                if 'url' in json_response['data'][i]['attributes']:
                    ioc = json_response['data'][i]['attributes']['url']
                    #print(json_response['data'][i]['attributes']['url'])
                    with open('IOC-list-file.txt', 'a+') as file:

                        json.dump(ioc, file)
                else:
                    pass
            except IndexError:
                pass

        # Extract similar files and append to output file
        url = "https://www.virustotal.com/api/v3/files/" + id + '/' + relationship_4
        headers = {'x-apikey': apiKeyVT}
        params = {"limit": "30"}
        response = requests.get(url, headers=headers, params=params)
        json_response = response.json()
        print('\n\nSimilar Files (sha256): \n')
        f = open('IOC-list-file.txt', 'a+')
        f.write("\n\n Similar files (sha256): \n")
        f.close()
        # run the loop function to extract IOC - Similar Files
        for i in range(30):
            try:
                if 'id' in json_response['data'][i]:
                    ioc = json_response['data'][i]['id']
                    #print(json_response['data'][i]['id'])
                    with open('IOC-list-file.txt', 'a+') as file:

                        json.dump(ioc, file)
                else:
                    pass
            except IndexError:
                pass

        # Extract embedded URLs and append to output file
        url = "https://www.virustotal.com/api/v3/files/" + id + '/' + relationship_5
        headers = {'x-apikey': apiKeyVT}
        params = {"limit": "30"}
        response = requests.get(url, headers=headers, params=params)
        json_response = response.json()
        print('\n\nSimilar Files (sha256): \n')
        f = open('IOC-list-file.txt', 'a+')
        f.write("\n\n Similar files (sha256): \n")
        f.close()
        # run the loop function to extract IOC - Similar Files
        for i in range(30):
            try:
                if 'id' in json_response['data'][i]:
                    ioc = json_response['data'][i]['id']
                    # print(json_response['data'][i]['id'])
                    with open('IOC-list-file.txt', 'a+') as file:

                        json.dump(ioc, file)
                else:
                    pass
            except IndexError:
                pass

        # Fix the output file - re-format for easy-reading
        from ragno_ops_file import ExecuteFileOpsFile
        ExecuteFileOpsFile.formatList_1()
        ExecuteFileOpsFile.formatList_2()
        ExecuteFileOpsFile.formatList_3()
        ExecuteFileOpsFile.formatList_4()
        ExecuteFileOpsFile.formatList_5()
        ExecuteFileOpsFile.formatList_6()

        output_results = input(
            '\nResults from all webs have been writen to IOC-list-file.txt in working directory.\n Press 1 to view the results: \n Press 2 to return to Main Menu: \n\n')
        if output_results == '1':
            with open('IOC-list-file.txt', 'r') as IOC:
                print(IOC.read())
                from ragno import Main
                Main.main_menu()
        elif output_results == '2':
            from ragno import Main
            Main.main_menu()
        else:
            print('Invalid selection, exiting...')
            exit()
        return