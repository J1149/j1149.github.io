import os
import subprocess
import time

from rpcauth import password_to_hmac, generate_salt

home_dir  = os.path.expanduser('~')
PAICOIN_CFG = os.path.join(home_dir, '.paicoin', 'paicoin.conf')
RPC_AUTH_PREFIX  = 'rpcauth'

def rpcauth_str_in_cfg():
    '''
    Function to check if the RPC_AUTH_PREFIX string is in 
    the paicoin.conf file.
    '''
    # if the file doesn't exist.
    if not os.path.exists(PAICOIN_CFG):
        return False
    # check if the rpcauth string is in the file
    with open(PAICOIN_CFG, 'r') as f:
        for line in f:
            # remove beginning whitespace
            s_line = line.rstrip()
            # if any given line begins with 
            # the RPC_AUTH_PREFIX, the file
            # has it
            if line.startswith(RPC_AUTH_PREFIX):
                print("rpcauth line found : %s"%line)
                return True
    return False


if __name__ == '__main__':
    if not rpcauth_str_in_cfg():
        username = input("Username?")
        password = input("Password?")
        salt = generate_salt(16)
        hmac = password_to_hmac(salt, password)
        rpcauth_str = "\n{0}={1}:{2}${3}\n".format(RPC_AUTH_PREFIX, username, salt, 
                                               hmac)
        with open(PAICOIN_CFG, 'a') as f:
            f.write(rpcauth_str)
        print("The following was appended to the paicoin.conf file:")
        print(rpcauth_str)

    # We tried to fix this; it's time to give up.
    if not rpcauth_str_in_cfg():
        raise OSError("Couldn't add rpcauth_str to paicoin.conf")
    
    # Startup paicoind
    subprocess.Popen('paicoind', shell=True)
    subprocess.call('sh', shell=True)
    

    
     

