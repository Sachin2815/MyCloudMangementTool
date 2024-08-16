#!/usr/bin/python3
print("Access-Control-Allow-Origin: *")
print("Access-Control-Allow-Methods: POST, GET, OPTIONS")
print("Content-type: text/html")
print()
import subprocess

command = "sudo docker ps -a"

exitcode, output = subprocess.getstatusoutput(command)

if exitcode==0:
    totalcontainer= output.split('\n')[1:]
    #print(totalcontainer)
    print("<table width='80%' align = 'center' border=5>")
    print("""<tr bgcolor='grey'>
        <th>ID</th>
        <th>Image</th>
        <th>Status</th>
        <th>Name</th>
    </tr>""")

    for container in totalcontainer:
        print("<tr>" )
        print( "<td>"+ container.split()[0]+"</td>")
	print( "<td>"+ container.split()[1]+"</td>")
        print( "<td>"+ container.split()[6]+"</td>")
        print( "<td>"+ container.split()[-1]+"</td>")
        print("</tr>" )
    print("</table>")
else :
    print("retry")