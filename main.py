#Encrypt by SC Ismail Djaini

import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode('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'))))