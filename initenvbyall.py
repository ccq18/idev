import os
import re


def file_get_contents(file):
    with open(file, 'r') as f:
        contents = f.read()
    return contents


def file_put_contents(file, contents):
    with open(file, 'w') as f:
        f.write(contents)


#
#
# def parse_env(contents):
#     lines = contents.split('\n')
#     envmap = {}
#     for line in lines:
#         kv = line.split('=')
#         if len(kv) == 2:
#             k = kv[0].strip()
#             v = kv[1].strip()
#             envmap[k] = v
#     return envmap
#
#
# def get_env(kv):
#     rs = ''
#     for k in kv:
#         rs += k + "=" + kv[k] + "\n"
#     return rs
#
#
# def replace_kv(source, to):
#     rs = {}
#     for k in to:
#         if k in source:
#             rs[k] = source[k]
#         else:
#             rs[k] = to[k]
#     return rs
# todo 自解析
# import os
# os.getenv('ENV_PORT')


# 该数据结构可以保存注释
class Env:
    env = None

    def __init__(self, env):
        self.env = env

    def parse_env(contents):
        lines = contents.split('\n')
        rskv = {}
        rslist = []
        for line in lines:
            kv = line.split('=')
            if len(kv) == 2:
                k = kv[0].strip()
                v = kv[1].strip()
                rskv[k] = v
                rslist.append({'k': k, 'v': v, 'type': 'map'})
            else:
                rslist.append({'v': line, 'type': 'text'})
        return Env({'kv': rskv, 'list': rslist})

    def parse_v(nowkv, v):
        matchObj = re.match(r'\$\{(.*)\}', v, re.M | re.I)
        if matchObj:
            envname = matchObj.group(1)
            if envname in nowkv:
                v = nowkv[envname]
            else:
                v = os.getenv(envname)
        return v

    def parse_real(self):
        rslist = []
        rskv = {}
        for item in self.env['list']:
            if item['type'] == 'map':
                k = item['k']
                v= Env.parse_v(rskv,item['v'])
                item['v'] = v
                rskv[k] =v
                rslist.append(item)
            else:
                rslist.append(item)
        self.env = {'kv': rskv, 'list': rslist}

    def exist(self, k):
        return k in self.env['kv']

    def getV(self, k):
        return self.env['kv'][k]

    def setV(self, k, v):
        if not self.exist(k):
            self.env['kv'][k] = v
            self.env['list'].append({'k': k, 'v': v, 'type': 'map'})
            return
        self.env['kv'][k] = v
        rslist = []
        for item in self.env['list']:
            if item['type'] == 'map' and item['k'] == k:
                item['v'] = v
                rslist.append(item)
            else:
                rslist.append(item)
        self.env['list'] = rslist

    def apply(self, data):
        source = data.env
        to =  self.env

        sourcekv = source['kv']
        tokv = to['kv']

        rslist = []
        rskv = {}
        for item in to['list']:
            if item['type'] == 'map':
                k = item['k']
                v = tokv[k]
                if k in sourcekv:
                    v = sourcekv[k]
                item['v'] = v
                rskv[k] = item['v']
                rslist.append(item)
            else:
                rslist.append(item)
        return Env({'kv': rskv, 'list': rslist})

    def get_env_str(self):
        envlist = self.env['list']
        rs = ''
        for item in envlist:
            if item['type'] == 'map':
                rs += item['k'] + "=" + item['v'] + "\n"
            else:
                rs += item['v'] + '\n'
        return rs


# def replace_env(source_str, to_str):
#     sourceenv = Env.parse_env(source_str)
#     toenv = Env.parse_env(to_str)
#     rsenv = sourceenv.replace_kv(toenv)
#     return rsenv.get_env_str()


# allenv = file_get_contents('./allenv')
# sourceenv = Env.parse_env(allenv)
# sourceenv.parse_real()
# print(sourceenv.get_env_str())
# simpleenv = file_get_contents('./sample.env')

# rs = replace_env(allenv, simpleenv)

#
apps = ['apollo', 'elasticsearch', 'elk', 'fastdfs', 'kafka', 'laravel', 'mongo', 'mysql', 'nacos', 'nginxphp',
        'postgres', 'redis', 'rocketmq', 'xxljob']
if not os.path.isfile('./allenv'):
    exit("not find env")
allenv_str = file_get_contents('./allenv')
allenv = Env.parse_env(allenv_str)
allenv.parse_real()
for app in apps:
    appenvpath = './' + app + '/sample.env'
    if not os.path.isfile(appenvpath):
        exit("not find env" + appenvpath)
    tpl_str = file_get_contents(appenvpath)
    tplenv = Env.parse_env(tpl_str)
    rsenv = tplenv.apply(allenv).get_env_str()
    file_put_contents('./' + app + '/.env', rsenv)

# allenv = parse_env(source_str)
# simpleenv = parse_env(simpleenv_str)
# simpleenv = replace_kv(allenv,simpleenv)
# print(get_env(simpleenv))
