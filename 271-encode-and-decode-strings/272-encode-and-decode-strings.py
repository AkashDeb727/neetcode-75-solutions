class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for word in strs:
            word_len = len(word)
            encoded_string = encoded_string + str(word_len) + "#" + word
            #encoded_string += f"{len(word)}#{word}"

        return encoded_string

        '''
        parts = []

        for word in strs:
            parts.append(f"{len(word)}#{word}")

        return "".join(parts)
        '''



    def decode(self, s: str) -> List[str]:
        decoded_string = []
        i = 0

        while i < len(s):
            word_len = 0
            j = i

            while j < len(s):
                if s[j] == '#':
                    word_len = int(s[i:j])

                    start = j+1
                    end = start + word_len

                    decoded_string.append(s[start : end])
                    break

                j += 1

            i = j + 1 + word_len
                
        
        return decoded_string
