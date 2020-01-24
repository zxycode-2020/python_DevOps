import os

def nginx_install():
    os.system('tar -xvf nginx.tar.gz')
    cmd = 'groupadd nginx && useradd -r -g nginx -s /bin/false nginx'
    os.system(cmd)
    if os.path.exists('nginx-1.10.2'):
        os.chdir('nginx-1.10.2')
    else:
        print 'dir does not exists'
        exit()
    pcre_dir = '../pcre-8.39'
    zlib_dir = '../zlib-1.2.8'
    ssl_dir = '../openssl-1.1.0c'

    cmd = './configure ' \
                  '--prefix=/usr/local/nginx ' \
                  '--conf-path=/etc/nginx.conf ' \
                  '--user=nginx --group=nginx ' \
                  '--with-pcre=' + pcre_dir + ' --with-zlib=' + zlib_dir + ' ' \
                  '--with-http_ssl_module --with-openssl=' + ssl_dir + ' ' \
                  '&& make ' \
                  '&& make install'
    os.system('chmod +x configure')

    os.system(cmd)
    file = '/usr/local/nginx/sbin/nginx'
    if os.path.exists(file):return True
    return False

def nginx_start():
    os.system("ln -sf /usr/local/nginx/sbin/nginx /usr/local/sbin/")
    os.system("nginx -s stop")
    cmd = "nginx"
    os.system(cmd)

def nginx_delete():
    rm_dir = "rm -rf nginx-1.10.2 openssl* pcre* zlib*"
    os.system(rm_dir)

if __name__ == '__main__':
    res = nginx_install()
    if res:
        print "Nginx install is ok"
        nginx_start()
        nginx_delete()
    else:
        print "Error!"