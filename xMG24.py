import requests , json , binascii , time , urllib3 , base64 , datetime , re ,socket , threading , random , os , asyncio
from protobuf_decoder.protobuf_decoder import Parser
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad , unpad
from datetime import datetime
from google.protobuf.timestamp_pb2 import Timestamp
from MG24xC4 import *

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


async def Mg24CreateRoom(room_name, K, V):  
    fields = {  
        1: 2,  
        2: {  
            1: 1,  
            2: 15,  
            3: 3,  
            4: room_name,  
            6: 8,  
            7: 30,  
            8: 1,  
            9: 1,  
            11: 1,  
            12: 2,  
            14: 36981056,  
            15: [  
                {  
                    1: "IDC1",  
                    2: 3000,  
                    3: "BD"  
                },  
                {  
                    1: "IDC2",  
                    2: 3000,  
                    3: "BD"  
                }  
            ]  
        }  
    }  

    proto = await CrEaTe_ProTo(fields)   # ✔️ IMPORTANT FIX  
    return await GeneRaTePk(proto.hex(), '0e0b', K, V)

#Global Auth And Join

async def AutH_GlobAl(K, V):
    fields = {
    1: 3,
    2: {
        2: 5,
        3: "fr"
    }
    }
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex() , '1215' , K , V)

#Global Join
async def GenJoinGlobaL(owner , code , K, V):
    fields = {
    1: 4,
    2: {
        1: owner,
        6: 1,
        8: 1,
        13: "en",
        15: code,
        16: "OR",
    }
    }
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex() , '0515' , K , V)

async def Mg24LeaveRoom(uid,key,iv):
    fields = {
        1: 6,
        2: {
            1: uid
        }
        }
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), '0E15', key , iv)

async def Mg24JoinRomm(uid,password,key,iv):
    fields = {
  1: 3,
  2: {
    1: int(uid),
    2: str(password),
    8: {
      1: "IDC3",
      2: 149,
      3: "ME"
    },
    9: "\u0001\u0003\u0004\u0007\t\n\u000b\u0012\u000e\u0016\u0019 \u001d",
    10: 1,
    12: {},
    13: 1,
    14: 1,
    16: "en",
    22: {
      1: 21
    }
  }
}
    print(fields)
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex() , '0E15' , key , iv)

async def Mg24RoomInv(K, V, uid):
    fields = {1: 22, 2: {1: int(uid)}}
    return GeneRaTePk(CrEaTe_ProTo(fields).hex(), '0E15', K, V)
