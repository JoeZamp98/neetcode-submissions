class Solution:

    def encode(self, strs: List[str]) -> str:

        return ".".join([str(len(s)) for s in strs]) + "#" + "".join(strs)


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

            int_x = int(x)

            sub_str = string[position: position + int_x]
            position += int_x
            all_substrings.append(sub_str)

        return all_substrings
