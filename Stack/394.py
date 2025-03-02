class Solution:
    def decodeString(self, s: str):

        stack = []
        curr_str = ''
        curr_num = ''
        for patern in s:

            if patern != ']':
                stack.append(patern)
            else:
                print(f'--------{stack}--------')
                while stack[-1] != '[':
                    curr_str = stack.pop() + curr_str

                stack.pop()
                print(stack, curr_str)
                while stack and stack[-1].isdigit():
                    curr_num = stack.pop() + curr_num

                stack.append(int(curr_num) * curr_str)
                curr_str = ''
                curr_num = ''



        return ''.join(stack)





if __name__ == '__main__':
    s = Solution()
    letter = "3[a]2[bc]"
    letter = "3[a2[c]]"
    letter = "2[abc]3[cd]ef"
    print(s.decodeString(letter))