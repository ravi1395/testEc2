from flask import Flask, redirect, url_for, request
from checkIp import ip

host  = ip()
host_ip = host.getIp()

app = Flask(__name__)
app.config['SERVER_NAME'] = 'xboct.com:7000'

@app.route('/home/<name>')
def hello(name):
    return 'hello {}'.format(name)

@app.route('/getIp')
def getIp():
    conn = ip()
    return conn.getIp()

@app.route('/redirect')
def redirectip():
    return redirect(url_for('getIp'))

@app.route('/myIp', methods = ['GET'])
def getmyRequest():
    print(dir(request))
    #print(request.base_url)
    return request.remote_addr

def main():
    if __name__ == '__main__':
        app.run(debug = True, host = host_ip, port = 7000)
main()
