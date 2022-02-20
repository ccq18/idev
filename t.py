import os
import re


def parse_v(nowkv, v):
    matchObj = re.match(r'\$\{(.*)\}', v, re.M | re.I)
    if matchObj:
        envname = matchObj.group(1)
        if envname in nowkv:
            v = nowkv[envname]
        else:
            v = os.getenv(envname)
    return v


nowkv = {'hello': "hi"}
v = "hello"
print(parse_v(nowkv,v))
