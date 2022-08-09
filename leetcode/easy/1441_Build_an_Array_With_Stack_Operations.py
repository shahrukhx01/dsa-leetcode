class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:

        arr = []
        output = []

        for num in range(1, n + 1):

            if num in target:
                arr.append(num)
                output.append("Push")

            else:
                arr.append(num)
                arr.pop()

                output.append("Push")
                output.append("Pop")

            if arr == target:
                break

        return output
