class Solution:

    def encode(self, strs: List[str]) -> str:

        lengths = [str(len(s)) for s in strs]

        all_submitted_strings = "".join(strs)

        lengths_str = ".".join(lengths)

        full_encoded_str = lengths_str + "#" + all_submitted_strings

        print(full_encoded_str)

        return full_encoded_str


    def decode(self, s: str) -> List[str]:

        counts, string = s.split("#", maxsplit=1)

        if len(string) == 0:

            if len(counts) == 0:

                return []

            if len(counts) == 1:

                return [""]


        counts = counts.split(".")

        position = 0

        all_substrings = []

        for x in counts:

            sub_str = string[position: position + int(x)]

            # print(x)
            # print(position)

            position += int(x)

            # print(sub_str)

            all_substrings.append(sub_str)

        return all_substrings




