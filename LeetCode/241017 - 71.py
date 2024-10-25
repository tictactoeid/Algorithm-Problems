# Simplify Path
# Medium

class Solution:
    def simplifyPath(self, path: str) -> str:
        answer = []
        for directory in path.split("/"):
            if directory == ".." and answer:
                answer.pop()
            elif directory not in [".", "", ".."]:
                answer.append(directory)

        return "/" + "/".join(answer)
