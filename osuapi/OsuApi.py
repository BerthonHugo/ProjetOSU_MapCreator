from ossapi import Ossapi, BeatmapsetSearchCategory, BeatmapsetSearchMode, Cursor, RankingType
import requests
import os
import ChimuApi as chimu

client_id = 20938
client_secret = "vgYhZHQD4dkXDJwhxT1JkzF8bhFzuEXtA43QYuMx"
token_key = "16a58360c5aebb296658e289e1517e1368f21d87"
callbackURL = ""
mode = BeatmapsetSearchMode.OSU
category = BeatmapsetSearchCategory.RANKED
requestNumber = 10_000
BASE_URL_V2 = "https://osu.ppy.sh/api/v2"
BASE_URL_V1 = "https://api.chimu.moe/v1/download"

api = Ossapi(client_id, client_secret)


# def write_beatmapset_file(filename, data):
#     file_path = os.path.join("C:/Users/hugob/dev/python/OSU_AI/", f"{filename}.osz")
#     print(file_path)
#
#     with open(file_path, "wb") as outfile:
#         outfile.write(data)
#         print("success?")


# def request(method, URL):
#     header={
#         'accept: application/json'
#     }
#     return api.session.request(method, URL,headers=header
#                                client_id=client_id,
#                                client_secret=client_secret)


# def downloadBeatmapsetsV2(beatmapsetId):
#     return request("GET",
#                    f"{BASE_URL_V2}/beatmapsets/{beatmapsetId}/download?noVideo=1")
#
#
# def downloadBeatmapsetsV1(beatmapsetId):
#     return request("GET", f"{BASE_URL_V1}/{beatmapsetId}")


response = api.search_beatmapsets(mode=mode, category=category)


for index,res in enumerate(response.beatmapsets):
    print("{}: {}".format(index,res.id))


    ###################################################################

# response = downloadBeatmapsetsV1(1886691)
# if response.status_code == requests.codes.ok:
#     write_beatmapset_file("test", response.content)
#     print("ok")
# else:
#     print("error")


###################################################################

def download():

    api = chimu.ChimuAPI()

    file_bytes = api.download_file(1, token_key, state="hcaptcha")

    with open("map.osz", "wb") as filea:
        filea.write(file_bytes)

download()
