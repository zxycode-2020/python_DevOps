#coding:utf8
import os

def nginx_install():
    cmd = 'tar xzvf nginx.tar.gz'
    os.system(cmd)
    if os.path.exists('nginx-1.10.2'): #文件夹存在
        pcre_dir = '../pcre-8.39'
        ssl_dir = '../openssl-1.1.0c'
        zlib_dir = '../zlib-1.2.8'
        os.chdir('nginx-1.10.2')
        os.system('groupadd nginx')
        os.system('useradd -g nginx nginx -s /sbin/nologin')
        cmd = './configure --prefix=/usr/local/nginx1.10.2 ' \
              '--with-http_dav_module ' \
              '--with-http_stub_status_module ' \
              '--with-http_addition_module ' \
              '--with-http_sub_module ' \
              '--with-http_flv_module ' \
              '--with-http_mp4_module ' \
              '--with-pcre=' + pcre_dir + ' ' \
              '--with-openssl=' + ssl_dir + ' ' \
              '--with-zlib=' + zlib_dir + ' ' \
              '--with-http_gzip_static_module ' \
              '--user=nginx --group=nginx'
        os.system('chmod +x configure')
        os.system(cmd)
        os.system('make && make install')
        os.system('ln -s /usr/local/nginx1.10.2/sbin/nginx /usr/local/sbin/nginx')

        os.chdir('../')
        os.system('rm -rf nginx* pcre* zlib* open*')
def nginx_start():
    os.system('chown - R nginx:nginx /usr/local/nginx1.10.2/html')
    cmd = 'nginx'
    os.system(cmd)

def nginx_restart():
    os.system('nginx -s reload')

def nginx_stop():
    os.system('nginx -s stop')


if __name__ == '__main__':
    nginx_install()
    nginx_start()