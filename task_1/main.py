import subprocess
import re
import csv


def main(): 
    hostnames = ["google.com", "cloudflare.com", "stackoverflow.com", "github.com", "discord.com", 
                 "steampowered.com", "aeza.net", "yandex.com", "yahoo.com", "chess.com"]
    timeout_time = 0.1
    rtt_arr = []
    r_exp = r'\d+'

    for hostname in hostnames:
        response = str(subprocess.run(f"ping -n 1 {hostname}", 
                                      capture_output=True, shell=True, text=True, encoding='cp866').stdout)
        regexp_output = re.findall(r_exp, response)
        if len(regexp_output) < 1:
            regexp_output = [-1]
        rtt_arr.append(regexp_output[-1])

    csv_to_write = zip(hostnames, rtt_arr)

    with open('rtts.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, dialect='excel')
        for hostname, rtt in csv_to_write:
            writer.writerow([hostname, rtt])


main()