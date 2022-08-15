import string


class Solution:
    def decodeMessage(self, key: str, message: str) -> str:

        key = key.replace(" ", "")
        map_ = {}
        for idx in range(len(key)):
            if key[idx] not in map_:
                map_[key[idx]] = string.ascii_lowercase[len(map_)]
        decrypted = ""
        for message_char in message:
            if message_char == " ":
                decrypted += " "
                continue

            decrypted += map_[message_char]

        return decrypted
