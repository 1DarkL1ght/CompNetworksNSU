import subprocess
import re
import csv


def main(): 
    hostnames = ["google.com", "cloudflare.com", "stackoverflow.com", "github.com", "discord.com", 
        "steampowered.com", "aeza.net", "yandex.com", "yahoo.com", "chess.com"]
    rtt_array = []
    regular_expression = r'\d+'

    for hostname in hostnames:
        response = str(subprocess.run(f"ping -n 1 {hostname}", 
            capture_output=True, shell=True, text=True, encoding='cp866').stdout)
        regexp_output = re.findall(regular_expression, response)
        if len(regexp_output) < 1:
            regexp_output = [-1]
        rtt_array.append(regexp_output[-1])

    csv_to_write = zip(hostnames, rtt_array)

    with open('task_1/rtts.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, dialect='excel')
        for hostname, rtt in csv_to_write:
            writer.writerow([hostname, rtt])


main()